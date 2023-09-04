import datetime
import uuid
from typing import List

from model.location import Location
from model.reports import Report

__report: List[Report] = []


async def get_reports() -> List[Report]:
    return list(__report)


async def add_report(description: str, location: Location) -> Report:
    now = datetime.datetime.now()
    report = Report(id=str(uuid.uuid4()), description=description, location=location, created_date=now)

    __report.append(report)
    __report.sort(key=lambda r: r.created_date, reverse=True)

    return report
