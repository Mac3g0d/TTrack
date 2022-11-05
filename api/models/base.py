import uuid
from datetime import datetime

from aredis_om import HashModel
from db import keydb
from pydantic import Field


class TimestampedModel(HashModel):
    """Event model."""

    created_at: datetime

    class Meta:
        database = keydb


class TimestampedModelWithID(TimestampedModel):
    """Event model."""

    id: uuid.UUID = Field(default=uuid.uuid4())  # noqa: VNE003
