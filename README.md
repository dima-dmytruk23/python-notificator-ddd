# SetUp

1. Python 3.9+
2. Requirements
```shell
pip install -r requirements.txt
```
3. Env variables

**Example**
```shell
SENDER_EMAIL='test@gmail.com'
SENDER_PASSWORD='Gas@35Ff'
SMTP_SERVER='smtp.gmail.com'
SMTP_PORT=465
```

# How it work?

The package is written according to `DDD` principles and `Strategy` pattern.

To add your own service for sending notifications, need:

1. create a new *domain* in `src`
2. implement *entity*, inheriting from `NotificationBase`
3. implement *dto* notification
4. implement the logic in the *use case*, inheriting from `BaseUseCase`

**Scheme**:

`Controller` -> `Entity`(`DTO`) -> `UseCase`

*The `controller` can be dynamic (if you define the desired entity from the slug)*
