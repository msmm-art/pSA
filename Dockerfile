FROM python:3.9-slim

# System deps
RUN apt-get update && apt-get install -y build-essential

# Poetry
RUN pip install poetry

WORKDIR /src
#COPY README.md .
COPY pyproject.toml poetry.lock* ./
RUN poetry install  --no-root

COPY src/ ./

# DEBUG: list all files
RUN echo "==== Listing /src ====" && ls -R /src
RUN echo "--- Listing /src:" && ls -R /src
CMD ["poetry", "run", "uvicorn", "psa.Services:app", "--host", "0.0.0.0", "--port", "80"]