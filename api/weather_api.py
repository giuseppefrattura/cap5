from typing import Optional, List

import fastapi
from fastapi import Depends

from model.location import Location
from model.reports import Report, ReportSubmittal
from model.validation_error import ValidationError
from services import openweather_service, report_service

router = fastapi.APIRouter()


@router.get('/api/weather/{city}')
async def weather(loc: Location = Depends(),
                  units: Optional[str] = 'metric'):
    try:
        return await openweather_service.get_report_async(loc.city, loc.state, loc.country, units)
    except ValidationError as ve:
        return fastapi.Response(content=ve.error_msg, status_code=ve.status_code)


@router.get('/api/reports', name='all_reports')
async def report_get() -> List[Report]:
    return await report_service.get_reports()


@router.post('/api/reports', name='add_report', status_code=201)
async def report_post(report_submittal: ReportSubmittal) -> Report:
    desc = report_submittal.description
    loc = report_submittal.location
    rep = Report(desc, loc)
    return await report_service.add_report(rep)
