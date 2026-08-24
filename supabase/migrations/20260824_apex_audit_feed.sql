-- APEX Audit Feed + AI Model Fabric schema
-- Migration date: 2026-08-24
-- Runtime application is UNVERIFIED until applied and tested.

create table if not exists public.audit_events (
  id uuid primary key default gen_random_uuid(),
  seq bigint generated always as identity unique,
  event_id text not null unique,
  occurred_at timestamptz not null default now(),
  received_at timestamptz not null default now(),
  environment text not null check (environment in ('sandbox','live')),
  severity text not null default 'info' check (severity in ('debug','info','warn','error','critical')),
  source text not null,
  actor_type text not null check (actor_type in ('user','service','admin','system','provider_webhook')),
  actor_id text,
  action text not null,
  event_type text not null,
  resource_type text,
  resource_id text,
  provider text,
  country text,
  currency text,
  amount_minor bigint,
  correlation_id uuid,
  payload jsonb not null default '{}',
  canonical text not null,
  prev_hash text not null,
  hash text not null unique
);

create or replace function public.prevent_audit_mutation() returns trigger language plpgsql as $$
begin raise exception 'audit_events is append-only. seq=% is frozen.', old.seq; end;
$$;

drop trigger if exists trg_audit_append_only on public.audit_events;
create trigger trg_audit_append_only before update or delete on public.audit_events
for each row execute function public.prevent_audit_mutation();

create or replace function public.audit_chain_trigger() returns trigger language plpgsql as $$
declare prev text;
begin
  perform pg_advisory_xact_lock(hashtext('apex_audit_chain'));
  select hash into prev from public.audit_events order by seq desc limit 1;
  if prev is null then prev := repeat('0',64); end if;
  new.prev_hash := prev;
  new.canonical := jsonb_build_object(
    'event_id',new.event_id,'occurred_at',new.occurred_at,'severity',new.severity,
    'source',new.source,'event_type',new.event_type,'resource_type',new.resource_type,
    'resource_id',new.resource_id,'provider',new.provider,'correlation_id',new.correlation_id,
    'amount_minor',new.amount_minor,'currency',new.currency,'payload',new.payload
  )::text;
  new.hash := encode(sha256(convert_to(new.prev_hash || new.canonical,'UTF8')),'hex');
  return new;
end;
$$;

drop trigger if exists trg_audit_chain on public.audit_events;
create trigger trg_audit_chain before insert on public.audit_events
for each row execute function public.audit_chain_trigger();

create table if not exists public.audit_consumers (
  id uuid primary key default gen_random_uuid(), name text not null unique,
  last_seq bigint not null default 0, filter jsonb not null default '{}', updated_at timestamptz not null default now()
);

create table if not exists public.audit_alert_rules (
  id uuid primary key default gen_random_uuid(), name text not null, event_type text, severity text, provider text,
  match jsonb not null default '{}', channel text not null check (channel in ('slack','email','webhook','dashboard')),
  enabled boolean not null default true
);

create table if not exists public.audit_alert_deliveries (
  id uuid primary key default gen_random_uuid(), rule_id uuid not null references public.audit_alert_rules(id),
  event_id text not null references public.audit_events(event_id), delivered boolean not null default false,
  delivered_at timestamptz, attempts integer not null default 0, unique(rule_id,event_id)
);

create table if not exists public.ai_model_registry (
  id uuid primary key default gen_random_uuid(), model_key text not null unique, display_name text not null,
  family text not null, publisher text, version text, digest_sha256 text,
  execution_scope text not null check (execution_scope in ('local','lan','cloud','catalog_only')),
  runtime text not null check (runtime in ('ollama','llama_cpp','vllm','mlx','lm_studio','comfyui','diffusers','whisper_cpp','piper','coqui_tts','custom')),
  modalities jsonb not null default '[]', capabilities jsonb not null default '[]',
  installed boolean not null default false, healthy boolean not null default false, enabled boolean not null default false,
  model_size_bytes bigint, parameter_count_billions numeric, quantization text, context_window_tokens integer,
  min_system_ram_gb numeric, min_vram_gb numeric, required_accelerators jsonb not null default '[]',
  latency_p50_ms numeric, latency_p95_ms numeric, throughput_tokens_per_second numeric,
  benchmark_score numeric, benchmark_evidence jsonb not null default '[]',
  license_id text, license_url text, commercial_use_status text not null default 'unreviewed' check (commercial_use_status in ('unreviewed','allowed','restricted','prohibited','unknown')),
  privacy_class text not null default 'local_only' check (privacy_class in ('local_only','local_preferred','cloud_allowed')),
  source_url text, source_revision text, installed_path text, runtime_endpoint text,
  health_checked_at timestamptz, last_used_at timestamptz, last_error jsonb,
  evidence jsonb not null default '[]', created_at timestamptz not null default now(), updated_at timestamptz not null default now()
);

create table if not exists public.local_compute_nodes (
  id uuid primary key default gen_random_uuid(), node_key text not null unique, os text not null, hostname text,
  cpu_cores integer, system_ram_gb numeric, free_disk_gb numeric, gpu_inventory jsonb not null default '[]',
  accelerators jsonb not null default '[]', runtimes jsonb not null default '{}', last_probe_at timestamptz not null,
  health_status text not null default 'unknown' check (health_status in ('healthy','degraded','offline','unknown')),
  evidence jsonb not null default '[]', created_at timestamptz not null default now(), updated_at timestamptz not null default now()
);

create table if not exists public.ai_model_audit_events (
  id uuid primary key default gen_random_uuid(), event_id text not null unique,
  model_id uuid references public.ai_model_registry(id), node_id uuid references public.local_compute_nodes(id),
  event_type text not null, task_id text, decision jsonb not null default '{}', evidence jsonb not null default '[]',
  data_egress boolean not null default false, occurred_at timestamptz not null default now()
);

create index if not exists idx_ai_models_directory on public.ai_model_registry(execution_scope,installed,healthy,enabled,runtime);
create index if not exists idx_ai_audit_model_time on public.ai_model_audit_events(model_id,occurred_at desc);
create index if not exists idx_ai_audit_task_time on public.ai_model_audit_events(task_id,occurred_at desc);
create index if not exists idx_audit_event_time on public.audit_events(occurred_at desc);

-- Important: generated selectability is deliberately not persisted here; application policy must
-- require installed + healthy + enabled + local scope + evidence/license/hardware gates.
