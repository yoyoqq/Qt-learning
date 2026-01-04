# Copilot Instructions for FastAPI + Vue.js Playground

## Architecture Overview
This is a full-stack CRUD application with a FastAPI backend and Vue.js frontend. The backend uses in-memory data storage for simplicity, with separate routers for items and users. The frontend communicates via REST API calls to `http://127.0.0.1:8000`.

- **Backend Structure**: `playground/` contains FastAPI app, Pydantic schemas in `schemas.py`, CRUD operations in `crud.py`, and database simulation in `database.py`.
- **Frontend Structure**: `frontend/` uses Vue 3 with Vite, Pinia for state management, and Vue Router. API calls are centralized in `services/api.js`.
- **Data Flow**: Frontend fetches/creates items via `http://127.0.0.1:8000/items/`. CORS is configured for `localhost:5173`.

## Key Patterns
- **Backend**: Use Pydantic models from `schemas.py` for request/response validation. CRUD functions in `crud.py` handle data operations. Routers in `routers/` define endpoints.
- **Frontend**: Components in `components/` handle UI logic. Use `services/api.js` for all backend communication. Stores in `stores/` manage global state (e.g., Pinia stores like `counter.js`).
- **API Integration**: Fetch items with `fetchItems()`, create with `createItem(item)`, delete with `deleteItem(id)`. Handle errors with try/catch and display in UI.
- **Inconsistency Note**: `routers/items.py` uses a local `items_db` list with sample data, while `crud.py` operates on `database.py`'s lists. Prefer using CRUD functions for consistency.

## Development Workflows
- **Run Backend**: `cd playground && uvicorn main:app --reload` (starts on `http://127.0.0.1:8000`)
- **Run Frontend**: `cd frontend && npm run dev` (starts on `http://localhost:5173`)
- **Lint Frontend**: `cd frontend && npm run lint`
- **Format Frontend**: `cd frontend && npm run format`
- **Build Frontend**: `cd frontend && npm run build`

## Conventions
- **Imports**: Backend uses relative imports like `from playground.schemas import ...`. Frontend uses relative paths.
- **Error Handling**: Backend raises `HTTPException` for errors. Frontend catches fetch errors and displays messages.
- **Component Naming**: Components like `AddItem.vue` may handle multiple actions (e.g., listing and deleting).
- **State Management**: Use Pinia stores for shared state; currently only a counter store exists.

## Key Files
- `playground/main.py`: App setup with CORS and router inclusion.
- `frontend/src/services/api.js`: Centralized API functions.
- `frontend/src/components/ItemList.vue`: Example of fetching and displaying data.
- `playground/schemas.py`: Defines User and Item models.</content>
<parameter name="filePath">c:\Users\yagol\OneDrive\Escritorio\Qt-learning-\VueJS\fastapi-playground\.github\copilot-instructions.md