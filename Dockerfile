ARG PYTHON_VERSION=3.12

FROM python:${PYTHON_VERSION}-bookworm
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_INDEX_URL=https://pypi.org/simple \
    WORKON_HOME=/venv \
    PYTHONPATH=/app

WORKDIR /app/api

RUN pip install --no-cache-dir pipenv
COPY Pipfile Pipfile.lock /app/

RUN pipenv sync

# Copy the source code into the container.
COPY api /app/api

# Create a non-privileged user that the capital_gains will run under.
# See https://docs.docker.com/go/dockerfile-user-best-practices/
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    ai_aura_test_user \
    && chown -R ai_aura_test_user:ai_aura_test_user /app

# Switch to the non-privileged user to run the application.
USER ai_aura_test_user

WORKDIR /app/api

# Expose the port that the application listens on.
EXPOSE 9000
ENTRYPOINT ["pipenv", "run"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:9000"]
