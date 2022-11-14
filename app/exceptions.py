from fastapi.responses import JSONResponse

from app.models.common import build_google_json, GoogleApiJsonError


async def http_exception_handler(request, exc):
    json = build_google_json(
        error=GoogleApiJsonError(code=exc.status_code, message=str(exc.detail))
    )
    return JSONResponse(status_code=exc.status_code, content=json)


async def request_validation_handler(request, exc):
    errors = exc.errors()
    print(errors)
    try:
        message = errors[0]["msg"]
    except KeyError:
        message = "Verification Error"

    json = build_google_json(error=GoogleApiJsonError(code=422, message=message))
    return JSONResponse(status_code=422, content=json)
