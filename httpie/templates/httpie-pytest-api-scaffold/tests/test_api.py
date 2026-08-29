# last_verified: 2026-08-29 · httpie 3.2.4

import json
import subprocess


def httpie(method: str, url: str, *args: str) -> subprocess.CompletedProcess:
    cmd = ["http", "--check-status", "--ignore-stdin", "--timeout", "10",
           "--print", "hb", method, url, *args]
    return subprocess.run(cmd, capture_output=True, text=True)


def test_list_items_empty(base_url):
    result = httpie("GET", f"{base_url}/items")
    assert result.returncode == 0
    body = json.loads(result.stdout.split("\r\n\r\n", 1)[1])
    assert body == []


def test_create_and_get_item(base_url):
    create = httpie("POST", f"{base_url}/items", "name=widget", "price:=19.99")
    assert create.returncode == 0
    parts = create.stdout.split("\r\n\r\n", 1)
    created = json.loads(parts[1])
    item_id = created["id"]

    get = httpie("GET", f"{base_url}/items/{item_id}")
    assert get.returncode == 0
    got = json.loads(get.stdout.split("\r\n\r\n", 1)[1])
    assert got["name"] == "widget"
    assert got["price"] == 19.99


def test_get_missing_item_returns_404(base_url):
    result = httpie("GET", f"{base_url}/items/99999")
    assert result.returncode == 4
