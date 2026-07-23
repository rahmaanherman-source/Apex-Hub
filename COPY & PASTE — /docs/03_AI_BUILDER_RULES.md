# AI BUILDER RULES
# Behavior for Coding Agents

## Purpose

This document defines how AI coding agents must behave when generating or modifying APEX Hub code.

---

## Core Rules

- Never create duplicate systems.  
- Never invent a second authentication engine.  
- Always reuse existing APIs.  
- Always reuse existing UI components.  
- Always search the repository before creating files.  
- Every button must perform work.  
- Every page must be connected to the rest of the platform.  
- Every API requires authentication unless explicitly public.  
- Customer Service routes to Adam AI.  
- If Adam AI cannot resolve an issue, escalate to the configured live support provider.  
- Never hardcode payment providers.  
- Always use adapters.  
- Always use environment variables.  
- Always support future providers.  
- Never build platform‑specific logic unless required.  
- Never bypass audit logging for state‑changing operations.  
- Always respect roles and permissions.  
- Always register new objects in the Global Object Registry.  
- Always integrate new features into Automation and Analytics when applicable.

---

## Repository Behavior

Before creating new code:

1. Search existing modules, services, and components.  
2. Reuse patterns and contracts already defined.  
3. Align with:
   - `00_CONSTITUTION.md`  
   - `01_ENGINEERING_STANDARD.md`  
   - `02_DESIGN_SYSTEM.md`  
   - `04_ARCHITECTURE.md`  

AI builders must treat these documents as law.  
Implementation must follow them.
