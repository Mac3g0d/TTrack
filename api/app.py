import json
from typing import Callable

from aredis_om import Migrator
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from .db import create_db
from .exceptions import ApiExceptionError
from .routes import api_router
from .settings import get_settings
from .utils import setup_logger

app = FastAPI()
settings = get_settings()


@app.on_event("startup")
async def on_startup() -> None:
    """Startup function, prepare db and logger."""
    await Migrator().run()
    await create_db()
    app.include_router(api_router)
    setup_logger()

app.add_middleware(SessionMiddleware, secret_key=settings.SESSION_SECRET_KEY)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)


@app.middleware("http")
async def error_middleware(request: Request, call_next: Callable) -> Response | None:
    """
    Return json of error except raise error.

    :param request: sent request.
    :param call_next: idn what is it.
    :return: Response of error.
    """
    try:
        return await call_next(request)
    except ApiExceptionError as error:
        return Response(json.dumps({"error": str(error)}), status_code=error.status_code)
