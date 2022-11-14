from typing import List

from app.models.common import GoogleApiJsonBody, GoogleApiJson

ISO_LIST = [
    12,
    16,
    20,
    25,
    32,
    40,
    50,
    64,
    80,
    100,
    125,
    160,
    200,
    250,
    320,
    400,
    500,
    640,
    800,
    1000,
    1250,
    1600,
    2000,
    2500,
    3200,
    4000,
    5000,
    6400,
]


class IsoBody(GoogleApiJsonBody):
    items: List[int]


class IsoList(GoogleApiJson):
    data: IsoBody


def get_iso():
    return ISO_LIST
