# last_verified: 2026-08-29 · httpie 3.2.4

from fastapi import FastAPI, HTTPException

app = FastAPI(title="Item Service")

_items: dict[int, dict] = {}
_next_id: int = 1


@app.get("/items")
def list_items():
    return list(_items.values())


@app.post("/items", status_code=201)
def create_item(body: dict):
    global _next_id
    item = {"id": _next_id, **body}
    _items[_next_id] = item
    _next_id += 1
    return item


@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in _items:
        raise HTTPException(status_code=404, detail="item not found")
    return _items[item_id]
