from aredis_om import NotFoundError as NotFound
from fastapi import APIRouter, Response

from ..exceptions import NotFoundError
from ..models import Day

day_router = APIRouter(prefix="/days")


@day_router.post("/create", response_model=Day)
async def create(day: Day) -> Day:
    return await day.save()


@day_router.get("/")
async def get_days() -> Response:
    days = await Day.find().all()
    return {"days": days}


@day_router.get("/{pk}", response_model=Day)
async def get_day(pk: str) -> Day:
    # To retrieve this customer with its primary key, we use `Customer.get()`:
    try:
        return await Day.find((Day.pk == pk)).all()

    except NotFound:
        raise NotFoundError("Day")
