from datetime import datetime

from aredis_om import HashModel


class Day(HashModel):
    """Day model."""

    created_at: datetime
