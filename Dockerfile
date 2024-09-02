# Указываем базовый образ Python
FROM python:3.12.5-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app


# Копируем файлы конфигурации Poetry (pyproject.toml и poetry.lock)
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости проекта
RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-dev --no-root

# Копируем весь код приложения в рабочую директорию контейнера
COPY . .

# Запускаем приложение с помощью Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]