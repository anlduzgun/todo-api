FROM python:3.12-alpine


ENV PYTHONBUFFERED=1

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python3", "todo/manage.py", "runserver", "0.0.0.0:8000"]