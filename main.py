from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
import json

app = FastAPI()

# serve static files from the static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def timer_list(request: Request):
    """
    Returns a pretty page of countdown timers
    """
    data = get_data(Path("data.json"))
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


@app.get("/api/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
