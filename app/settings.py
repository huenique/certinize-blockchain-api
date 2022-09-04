# pylint: disable=E1101,I1101
import typing
import uuid

import orjson
import pydantic
from blacksheep.plugins import json


def serialize(value: typing.Any) -> str:
    return orjson.dumps(value).decode("utf8")


json.use(  # type: ignore
    loads=orjson.loads,  # type: ignore
    dumps=serialize,  # type: ignore
)


class AppSettings(pydantic.BaseSettings):
    certinize_image_processor = pydantic.AnyHttpUrl = pydantic.AnyHttpUrl(
        url="https://", scheme="https"
    )
    certinize_api_key: uuid.UUID = uuid.UUID("00000000-0000-0000-0000-000000000000")

    class Config(pydantic.BaseSettings.Config):
        env_file = ".env"


app_settings = AppSettings()
