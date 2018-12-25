# Fargate Operation

## Deploy Platform

FARGATE

## command

> service up

```
ecs-cli compose --project-name sample-ap service up --create-log-groups
```

> service ps

```
ecs-cli compose --project-name sample-ap service ps
```

> confirm log

```
ecs-cli logs --task-id [task_id] --follow 
```

> service down

```
ecs-cli compose --project-name sample-ap service down
```
