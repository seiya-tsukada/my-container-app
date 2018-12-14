# my_container_app

## Build Platform

・AWS CodeBuild

## use docker run

```
docker run -d -e FLASK_APP=/var/app/main.py [image_name]
```

## start command

```
export FLASK_APP=/[path]/[to]/main.py
flask run --host=0.0.0.0 --port=80
```
