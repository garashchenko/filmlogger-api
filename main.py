from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware

from app import routes, exceptions


def get_application():
    app = FastAPI()
    app.include_router(routes.router)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_exception_handler(StarletteHTTPException, exceptions.http_exception_handler)
    app.add_exception_handler(
        RequestValidationError, exceptions.request_validation_handler
    )
    return app


app = get_application()
