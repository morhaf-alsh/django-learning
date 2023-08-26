FROM python:3.10.12

RUN mkdir /app

WORKDIR /app

COPY . .

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

RUN pip install psycopg2-binary

RUN export SECRET_KEY="mzDMzCCh-s5NOFmK1UM-o3r5GN9ho4k1BpFzinzxfwM"

RUN python manage.py makemigrations

RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000

