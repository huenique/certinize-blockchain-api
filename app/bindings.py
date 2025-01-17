"""
app.bindings
~~~~~~~~~~~~

This module contains custom bindings. See:
https://www.neoteroi.dev/blacksheep/binders/
"""
import typing

import blacksheep
import pydantic
from blacksheep.server import bindings

from app import errors, models


class FromIssuanceRequestModel(
    bindings.BoundValue[bindings.T]
):  # pylint: disable=R0903
    ...


class IssuanceRequestBinder(bindings.Binder):

    handle = FromIssuanceRequestModel

    async def get_value(self, request: blacksheep.Request) -> typing.Any:
        try:
            return models.IssuanceRequest(**await request.json())
        except pydantic.ValidationError as validation_error:
            raise errors.BadRequest(details=validation_error.errors())
