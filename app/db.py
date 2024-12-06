from datetime import datetime
from typing import Optional


class CodeRecord:
    def __init__(
        self,
        ID: str,
        language: str,
        code: str,
        status: str,
        submitted_time: datetime,
        logs: str = "",
        completed_time: Optional[datetime] = None,
    ):
        self.ID = ID
        self.Language = language
        self.Code = code
        self.Status = status
        self.Logs = logs
        self.SubmittedTime = submitted_time
        self.CompletedTime = completed_time


class CodeDB:
    def __init__(self):
        # Dictionary: {id: CodeRecord}
        self.items = {}

    def store(
        self, id_: str, language: str, code: str, status: str, submitted_time: datetime
    ):
        record = CodeRecord(
            ID=id_,
            language=language,
            code=code,
            status=status,
            submitted_time=submitted_time,
        )
        self.items[id_] = record

    def get(self, id_: str) -> CodeRecord:
        return self.items[id_]

    def list_all(self):
        return list(self.items.values())

    def update(
        self,
        id_: str,
        status: Optional[str] = None,
        logs: Optional[str] = None,
        completed_time: Optional[datetime] = None,
    ):
        record = self.items[id_]
        if status is not None:
            record.Status = status
        if logs is not None:
            record.Logs = logs
        if completed_time is not None:
            record.CompletedTime = completed_time
        self.items[id_] = record
