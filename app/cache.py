from enum import Enum

from app.models.aperture import get_aperture
from app.models.ev import get_ev_chart, get_ev_chart_api
from app.models.iso import get_iso
from app.models.shutter import get_shutter


class Cache:
    def __init__(self):
        self.iso = get_iso()
        self.aperture = get_aperture()
        self.shutter = get_shutter()
        self.ev_chart = get_ev_chart()
        self.ev_chart_api = get_ev_chart_api(self.ev_chart)
        self.iso_enum = Enum(
            "ISOEnum", {str(iso): str(iso) for iso in self.iso}, type=str
        )


cache = Cache()
