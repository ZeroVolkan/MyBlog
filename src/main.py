from typing import Annotated

from fastapi import FastAPI, Query, Header
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()


@app.get("/blogs/{blog_id}", tags=["blogs"])
def blog(blog_id: int):
    return HTMLResponse()


@app.get("/blogs", tags=["blogs"])
def blogs():
    return HTMLResponse()


@app.get("/me", tags=["me"])
def me():
    return HTMLResponse()
