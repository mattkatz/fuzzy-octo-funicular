from pathlib import Path
from datetime import datetime
import json

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

# serve static files from the static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")
data_path = Path("data.json")


@app.get("/")
async def timer_list(request: Request):
    """
    Returns a pretty page of countdown timers
    """
    data = get_data(data_path)
    return templates.TemplateResponse("index.html", {"request": request, "data": data})


def get_data(path: Path):
    data = json.load(path.open())
    return data


@app.get("/items/{item_id}", response_class=HTMLResponse)
def read_item(item_id: int, q: str = None):
    return f"""
<html>
<head>
<title>A specific item</title>
<body>
<h1>That Item number {item_id}</h1>
<div>
Looks like we have item number {item_id}!
</div>
</body>
</head>
</html>
"""


@app.get("/items/", response_class=HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """


class CountdownItem(BaseModel):
    name: str
    date: datetime
    text: str
    delta_in_ms: int


@app.get("/api/items/")
def list_items():
    """Get a list of what we are timing"""
    return get_data(data_path)


@app.get("/api/items/{item_id}", response_model=CountdownItem)
def read_item(item_id: int, q: str = None):
    """Get a single item and show the details"""
    data = get_data(data_path)
    item = data[item_id]
    item["date"] = datetime.fromisoformat(item["date"])
    now = datetime.now()
    delta_in_ms = item["date"] - now
    item["delta_in_ms"] = delta_in_ms.total_seconds()
    citem = CountdownItem(**item)
    return citem
