from datetime import datetime

from aredis_om import Field, JsonModel

from ..db import keydb


class Event(JsonModel):
    """Event model."""

    day: list[str] | None = Field(index=True)
    name: str = Field(index=True)
    started_at: datetime = Field(index=True)
    ended_at: datetime = Field(index=True)
    created_at: datetime = Field(index=True)

    class Meta:
        database = keydb
