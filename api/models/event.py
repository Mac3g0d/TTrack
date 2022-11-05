from datetime import datetime

from .base import TimestampedModelWithID


class Event(TimestampedModelWithID):
    """Event model."""

    name: str
    started_at: datetime
    ended_at: datetime
