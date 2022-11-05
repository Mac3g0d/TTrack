FROM python:3.10

ENV PYTHONFAULTHANDLER=1 \
  PYTHONDONTWRITEBYTECODE=1\
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.2.2
RUN pip install "poetry==$POETRY_VERSION"
WORKDIR /ttrack
COPY poetry.lock pyproject.toml /ttrack/

RUN poetry install -n
COPY ../api /ttrack/
# Expose port 8000

EXPOSE 8000
# Use gunicorn as the entrypoint
CMD poetry run gunicorn -k uvicorn.workers.UvicornWorker -w 4 -b 0.0.0.0:8000 api.app:app
