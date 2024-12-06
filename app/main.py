from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from datetime import datetime, timezone
from pathlib import Path
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi import HTTPException

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
    submitted_time = datetime.now(timezone.utc)
    db.store(submission_id, language, code, "submitted", submitted_time)

    return RedirectResponse(url="/list-code", status_code=303)


@app.get("/list-code", response_class=HTMLResponse)
def list_code(request: Request):
    records = db.list_all()

    return templates.TemplateResponse(
        "list.html", {"request": request, "items": records, "count": len(records)}
    )


@app.get("/get-code/{uid}", response_class=HTMLResponse)
def get_code(uid: str, request: Request):
    try:
        record = db.get(uid)
    except KeyError:
        raise HTTPException(status_code=404, detail="Record not found")

    return templates.TemplateResponse(
        "code.html",
        {
            "request": request,
            "ID": record.ID,
            "Language": record.Language,
            "Status": record.Status,
            "Code": record.Code,
            "Logs": record.Logs,
            "SubmittedTime": record.SubmittedTime,
            "CompletedTime": record.CompletedTime,
        },
    )
