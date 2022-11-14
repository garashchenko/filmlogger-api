import decimal
import math
from typing import List

from app.models.common import GoogleApiJsonBody, GoogleApiJson, StopNumberItem


class ApertureItem(StopNumberItem):
    pass


class ApertureBody(GoogleApiJsonBody):
    items: List[ApertureItem]


class ApertureList(GoogleApiJson):
    data: ApertureBody


def get_aperture() -> List[StopNumberItem]:
    result = []
    decimal.getcontext().rounding = decimal.ROUND_DOWN
    stop_num = 0
    for i in range(11):
        precise = decimal.Decimal((math.sqrt(2)) ** i)
        places = 1 if precise < 10 else 0
        nominal = float(round(precise, places))
        result.append(
            StopNumberItem(
                nominal=f"f/{str(nominal)}",
                precise=round(precise, 4),
                stop_num=stop_num,
            )
        )
        stop_num += 1
    return result
