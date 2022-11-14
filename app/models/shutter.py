import math
from fractions import Fraction
from typing import List

from app.models.common import GoogleApiJsonBody, GoogleApiJson, StopNumberItem


class ShutterItem(StopNumberItem):
    pass


class ShutterBody(GoogleApiJsonBody):
    items: List[ShutterItem]


class ShutterList(GoogleApiJson):
    data: ShutterBody


def get_shutter():
    shutter_speeds = []

    # Nominal values are approximations established by an old convention,
    # so they don't really make sense in terms of computing
    nominal = 30
    precise = 32
    stop = 5
    while stop >= 0:
        item = StopNumberItem(nominal=nominal, precise=precise, stop_num=stop)
        shutter_speeds.append(item)
        stop -= 1
        nominal = math.ceil(nominal / 2)
        precise //= 2

    # For steps < 0 we will need to output fractions as nominal values.
    # This requires different kind of processing
    # Substitutes are needed to keep nominal values right
    substitute = {16: 15, 120: 125}
    denominator = nominal_d = 1
    for i in range(10):
        denominator *= 2
        nominal_d = substitute.get(nominal_d * 2, nominal_d * 2)

        precise = float(Fraction(1, denominator))
        nominal = str(Fraction(1, nominal_d))
        item = StopNumberItem(nominal=nominal, precise=precise, stop_num=stop)
        shutter_speeds.append(item)
        stop -= 1

    return shutter_speeds
