from typing import List

import exifread
from fastapi import UploadFile, HTTPException
from pydantic import BaseModel

from app.cache import cache
from app.models.aperture import ApertureItem
from app.models.common import GoogleApiJsonBody, GoogleApiJson
from app.models.ev import calculate_ev, convert_ev_iso
from app.models.shutter import ShutterItem
from app.const import CORRECT_MIME

import magic


class ExposureSettingsItem(BaseModel):
    aperture: ApertureItem
    shutter: ShutterItem


class ExposureSettingsBody(GoogleApiJsonBody):
    items: List[ExposureSettingsItem]


class ExposureSettingsList(GoogleApiJson):
    data: ExposureSettingsBody


def process_photo(photo: UploadFile, target_iso: int):
    mime = magic.from_buffer(photo.file.read(), mime=True)
    if mime not in CORRECT_MIME:
        raise HTTPException(status_code=422, detail="Incorrect file extension")

    photo.file.seek(0)
    tags = exifread.process_file(photo.file)
    if not tags:
        raise HTTPException(status_code=422, detail="No EXIF data")

    try:
        aperture = float(tags["EXIF ApertureValue"].values[0])
    except (KeyError, IndexError):
        raise HTTPException(status_code=422, detail="No aperture EXIF tag found")

    try:
        shutter = float(tags["EXIF ExposureTime"].values[0])
    except (KeyError, IndexError):
        raise HTTPException(status_code=422, detail="No shutter speed EXIF tag found")

    try:
        iso = tags["EXIF ISOSpeedRatings"].values[0]
    except (KeyError, IndexError):
        raise HTTPException(status_code=422, detail="No ISO EXIF tag found")

    ev = calculate_ev(aperture, shutter)
    ev = convert_ev_iso(ev, iso, target_iso)
    return [
        ExposureSettingsItem(aperture=aperture, shutter=shutter)
        for aperture, shutter in cache.ev_chart[ev]
    ]
