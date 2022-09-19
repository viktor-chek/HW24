from marshmallow import fields, Schema, validates_schema, ValidationError
from typing import Any

VALID_CMD_PARAMETERS: tuple = (
    "filter",
    "map",
    "unique",
    "sort",
    "limit",
    "regex"
)


class Request(Schema):
    filename = fields.Str(required=True)
    cmd1 = fields.Str(required=True)
    value1 = fields.Str(required=True)
    cmd2 = fields.Str(required=True)
    value2 = fields.Str(required=True)

    @validates_schema()
    def validate_cmd(self, values: dict, *args: Any, **kwargs: Any) -> dict:
        if values["cmd1"] not in VALID_CMD_PARAMETERS:
            raise ValidationError("cmd1: недопустимый параметр")
        if values["cmd2"] not in VALID_CMD_PARAMETERS:
            raise ValidationError("cmd2: недопустимый параметр")
        return values
