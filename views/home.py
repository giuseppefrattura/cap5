import fastapi
from starlette.requests import Request
from starlette.templating import Jinja2Templates

router = fastapi.APIRouter()

template = Jinja2Templates('templates')


@router.get('/')
def index(request: Request):
    return template.TemplateResponse('home/index.html', {'request': request})


@router.get('/favicon.ico')
def favicon():
    return fastapi.responses.RedirectResponse(url='/static/g/favicon.ico')
