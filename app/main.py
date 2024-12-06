from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from datetime import datetime
from pathlib import Path
from fastapi.templating import Jinja2Templates
from fastapi import Request

import uuid

from .db import CodeDB

app = FastAPI()
db = CodeDB()
templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))


@app.get("/submit-code-page", response_class=HTMLResponse)
def submit_code_page(request: Request):
    return templates.TemplateResponse("submit.html", {"request": request})


@app.post("/submit-code")
def submit_code(language: str = Form(...), code: str = Form(...)):
    submission_id = str(uuid.uuid4())
    submitted_time = datetime.utcnow()
    db.store(submission_id, language, code, "submitted", submitted_time)

    return RedirectResponse(url="/list-code", status_code=303)
