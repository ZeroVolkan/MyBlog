from typing import Annotated

from fastapi import FastAPI, Query, Header, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates =  Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )




@app.get("/blogs/{blog_id}", tags=["blogs"])
def blog(blog_id: int):
    return HTMLResponse()


@app.get("/blogs", tags=["blogs"])
def blogs():
    return HTMLResponse()


@app.get("/me", tags=["me"])
def me():
    return HTMLResponse()
