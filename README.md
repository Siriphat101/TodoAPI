# TodoAPI
API for Create, Update and Delete data from todo app

## build setup:
```bash
# from folder ToDoList 
$ pip install -r requirement.txt

# make migrations file
$ python manage.py makemigrations
$ python manage.py migrate

# create super user
$ python manage.py createsuperuser

# run server
$ python manage.py runserver

```

## Urls:
  * http://localhost:8000/api/create
  * http://localhost:8000/api/update/id
  * http://localhost:8000/api/delete/id

