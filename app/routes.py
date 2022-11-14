from fastapi import APIRouter, UploadFile, Form

from app.models.aperture import ApertureList, ApertureBody
from app.models.common import build_google_json
from app.models.ev import EVList, EVBody
from app.models.iso import IsoList, IsoBody
from app.models.photo import process_photo, ExposureSettingsBody
from app.models.shutter import ShutterList, ShutterBody

from app.cache import cache

router = APIRouter()


@router.get(
    "/iso", status_code=200, response_model=IsoList, response_model_exclude_none=True
)
async def get_iso():
    return build_google_json(IsoBody(items=cache.iso))


@router.get(
    "/aperture",
    status_code=200,
    response_model=ApertureList,
    response_model_exclude_none=True,
)
async def get_aperture():
    return build_google_json(ApertureBody(items=cache.aperture))


@router.get(
    "/shutter",
    status_code=200,
    response_model=ShutterList,
    response_model_exclude_none=True,
)
async def get_shutter():
    return build_google_json(ShutterBody(items=cache.shutter))


@router.get(
    "/ev", status_code=200, response_model=EVList, response_model_exclude_none=True
)
async def get_ev_chart():
    return build_google_json(EVBody(items=cache.ev_chart_api))


@router.post("/photo", status_code=200, response_model_exclude_none=True)
async def upload_photo(file: UploadFile, iso: cache.iso_enum = Form()):
    settings = process_photo(file, int(iso.value))
    return build_google_json(ExposureSettingsBody(items=settings))
