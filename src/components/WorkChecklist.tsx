import { useEffect, useMemo, useState } from 'react';
import { Check, Circle, ListChecks, Play, Plus, RotateCcw, Trash2 } from 'lucide-react';

type ChecklistItem = {
  id: string;
  title: string;
  done: boolean;
  status: 'READY' | 'REQUESTED';
};

const DEFAULT_ITEMS: ChecklistItem[] = [
  { id: 'task-1', title: 'Define the current APEX Studio task', done: false, status: 'READY' },
  { id: 'task-2', title: 'Complete the implementation', done: false, status: 'READY' },
  { id: 'task-3', title: 'Run build / type checks', done: false, status: 'READY' },
  { id: 'task-4', title: 'Verify the result in the UI', done: false, status: 'READY' },
  { id: 'task-5', title: 'Record evidence / final state', done: false, status: 'READY' },
];

const STORAGE_KEY = 'apex-work-checklist-v1';

function loadItems(): ChecklistItem[] {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return DEFAULT_ITEMS;
    const parsed = JSON.parse(raw);
    return Array.isArray(parsed) && parsed.length ? parsed : DEFAULT_ITEMS;
  } catch {
    return DEFAULT_ITEMS;
  }
}

export function WorkChecklist() {
  const [items, setItems] = useState<ChecklistItem[]>(loadItems);
  const [draft, setDraft] = useState('');

  useEffect(() => {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(items));
  }, [items]);

  const completed = useMemo(() => items.filter((item) => item.done).length, [items]);
  const percent = items.length ? Math.round((completed / items.length) * 100) : 0;

  function toggleItem(id: string) {
    setItems((current) => current.map((item) => (
      item.id === id ? { ...item, done: !item.done, status: 'READY' } : item
    )));
  }

  function addItem() {
    const title = draft.trim();
    if (!title) return;
    setItems((current) => [...current, {
      id: crypto.randomUUID(),
      title,
      done: false,
      status: 'READY',
    }]);
    setDraft('');
  }

  function requestCheck(item: ChecklistItem) {
    window.dispatchEvent(new CustomEvent('apex:check-requested', { detail: item }));
    setItems((current) => current.map((entry) => (
      entry.id === item.id ? { ...entry, status: 'REQUESTED' } : entry
    )));
  }

  function resetChecklist() {
    setItems(DEFAULT_ITEMS);
  }

  function clearCompleted() {
    setItems((current) => current.filter((item) => !item.done));
  }

  return (
    <section className="work-checklist" aria-label="APEX Studio work checklist">
      <div className="checklist-head">
        <div className="checklist-title">
          <div className="checklist-icon"><ListChecks size={17} /></div>
          <div>
            <p className="eyebrow">GABBY / WORK MEMORY</p>
            <h3>Active Checklist</h3>
          </div>
        </div>
        <div className="checklist-progress">
          <strong>{completed}/{items.length}</strong>
          <span>{percent}% complete</span>
        </div>
      </div>

      <div className="checklist-meter"><span style={{ width: percent + '%' }} /></div>

      <div className="checklist-items">
        {items.map((item) => (
          <div key={item.id} className={item.done ? 'checklist-item done' : 'checklist-item'}>
            <button
              className="check-toggle"
              onClick={() => toggleItem(item.id)}
              aria-label={item.done ? 'Mark ' + item.title + ' incomplete' : 'Mark ' + item.title + ' complete'}
            >
              {item.done ? <Check size={14} /> : <Circle size={14} />}
            </button>
            <span className="check-text">{item.title}</span>
            <span className={item.status === 'REQUESTED' ? 'check-status requested' : 'check-status'}>{item.status}</span>
            <button className="check-run" onClick={() => requestCheck(item)} title="Request this check from the execution layer">
              <Play size={12} /> RUN
            </button>
          </div>
        ))}
      </div>

      <div className="checklist-footer">
        <div className="checklist-add">
          <input
            value={draft}
            onChange={(event) => setDraft(event.target.value)}
            onKeyDown={(event) => { if (event.key === 'Enter') addItem(); }}
            placeholder="Add the next thing..."
            aria-label="Add checklist item"
          />
          <button onClick={addItem} title="Add checklist item"><Plus size={15} /></button>
        </div>
        <div className="checklist-actions">
          <button onClick={clearCompleted} disabled={!completed}><Trash2 size={13} /> CLEAR DONE</button>
          <button onClick={resetChecklist}><RotateCcw size={13} /> RESET</button>
        </div>
      </div>
    </section>
  );
}
