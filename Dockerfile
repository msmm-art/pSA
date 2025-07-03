FROM python:3.9-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y build-essential


RUN pip install poetry

WORKDIR /src
#COPY README.md .
COPY pyproject.toml poetry.lock* ./
RUN poetry install  --no-root

COPY src/ ./


EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "psa.Services:app", "--host", "0.0.0.0", "--port", "80"]