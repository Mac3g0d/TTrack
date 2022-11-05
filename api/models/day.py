from datetime import datetime

from aredis_om import Field, JsonModel

from ..db import keydb


class Day(JsonModel):
    """Day model."""

    events: list[str] | None = Field(index=True)
    created_at: datetime = Field(index=True)

    class Meta:
        database = keydb
