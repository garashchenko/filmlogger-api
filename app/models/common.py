from typing import Optional

from pydantic import BaseModel, Field


class GoogleApiJsonBody(BaseModel):
    pass


class GoogleApiJsonError(BaseModel):
    code: int
    message: str


class GoogleApiJson(BaseModel):
    api_version: str = Field(..., alias="apiVersion")
    data: Optional[GoogleApiJsonBody]
    error: Optional[GoogleApiJsonError] = None

    class Config:
        allow_population_by_field_name = True


class StopNumberItem(BaseModel):
    nominal: str
    precise: float
    stop_num: int


def build_google_json(
    body: Optional[GoogleApiJsonBody] = None, error: Optional[GoogleApiJsonError] = None
) -> dict:

    return GoogleApiJson(api_version="0.1", data=body, error=error).dict()
