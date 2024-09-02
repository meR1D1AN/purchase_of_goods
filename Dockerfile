# Указываем базовый образ Python
FROM python:3.12.5-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Устанавливаем Poetry
RUN pip install --no-cache-dir poetry

# Копируем файлы конфигурации Poetry (pyproject.toml и poetry.lock)
COPY pyproject.toml poetry.lock* /app/

# Устанавливаем зависимости проекта
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Копируем весь код приложения в рабочую директорию контейнера
COPY . /app

# Запускаем приложение с помощью Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]