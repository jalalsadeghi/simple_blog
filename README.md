# TrackTrace

## project setup

1- compelete cookiecutter workflow (recommendation: leave project_slug empty) and go inside the project
```
cd TrackTrace
```

2- SetUp venv
```
python -m venv venv
source venv/bin/activate
```

3- install Dependencies
```
pip install -r requirements_dev.txt
```

4- create your env
```
cp .env.example .env
```

5- spin off docker compose
```
docker compose -f docker-compose.dev.yml up -d
```

6- Create tables
```
python manage.py migrate
```

7- run the project
```
python manage.py runserver
```

8- Celery and celery beat

```
  python manage.py setup_periodic_tasks
  celery -A tracktrace.tasks worker -l info --without-gossip --without-mingle --without-heartbeat
  celery -A tracktrace.tasks beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
```
