import itertools
import math
from typing import List

from pydantic import BaseModel

from app.models.aperture import get_aperture, ApertureItem
from app.models.common import GoogleApiJsonBody, GoogleApiJson
from app.models.shutter import get_shutter, ShutterItem


class EVSettings(BaseModel):
    aperture: ApertureItem
    shutter: ShutterItem


class EVItem(BaseModel):
    EV: float
    settings: List[EVSettings]


class EVBody(GoogleApiJsonBody):
    items: List[EVItem]


class EVList(GoogleApiJson):
    data: EVBody


def calculate_ev(aperture: float, shutter: float):
    return round(math.log2((aperture**2) / shutter))


def convert_ev_iso(ev, from_iso, to_iso):
    return round(ev + math.log2(to_iso / from_iso))


def get_ev_chart():
    ev_chart = {}
    aperture = get_aperture()
    shutter = get_shutter()

    for aperture, shutter in itertools.product(aperture, shutter):
        ev = calculate_ev(aperture.precise, shutter.precise)
        ev_chart.setdefault(ev, []).append((aperture, shutter))

    return ev_chart


def get_ev_chart_api(ev_chart):
    result = []
    for ev, options in ev_chart.items():
        settings = [
            EVSettings(aperture=settings[0], shutter=settings[1])
            for settings in options
        ]
        result.append(EVItem(EV=ev, settings=settings))
    return result
