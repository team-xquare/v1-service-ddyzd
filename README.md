```
📦 v1-service-ddyzd
├─ app
│  ├─ core
│  │  ├─ applicatoin
│  │  │  ├─ view
│  │  │  │  ├─ payload
│  │  │  │  │  ├─ request.py
│  │  │  │  │  └─ response.py
│  │  │  │  ├─ api.py
│  │  │  │  └─ __init__.p
│  │  │  └─ controller
│  │  │     ├─ dto
│  │  │     ├─ control.py
│  │  │     └─ __int__.py
│  │  └─ club
│  │     ├─ view
│  │     │  ├─ payload
│  │     │  │  ├─ request.py
│  │     │  │  └─ response.py
│  │     │  ├─ api.py
│  │     │  └─ __init__.py
│  │     └─ controller
│  │        ├─ dto
│  │        ├─ control.py
│  │        └─ __init__.py
│  ├─ data
│  │  ├─ mysql
│  │  │  ├─ model
│  │  │  │  ├─ club
│  │  │  │  │  └─ club_model.py
│  │  │  │  └─ application
│  │  │  │     └─ application_model.py
│  │  │  └─ cqrs
│  │  │     ├─ club
│  │  │     │  ├─ query.py
│  │  │     │  ├─ command.py
│  │  │     │  └─ __init__.py
│  │  │     └─ application
│  │  │        ├─ query.py
│  │  │        ├─ command.py
│  │  │        └─ __init__.py
│  │  └─ mongo
│  │     ├─ model
│  │     │  ├─ room
│  │     │  │  └─ room_model.py
│  │     │  └─ chat
│  │     │     └─ chat_model.py
│  │     └─ cqrs
│  │        ├─ room
│  │        │  ├─ query.py
│  │        │  ├─ command.py
│  │        │  └─ __init__.py
│  │        └─ chat
│  │           ├─ query.py
│  │           ├─ command.py
│  │           └─ __init__.py
│  ├─ config
│  └─ common
│     ├─ security
│     └─ exception
├─ test
│  ├─ club
│  │  ├─ view
│  │  │  └─ test_view_add_club.py
│  │  └─ controller
│  │     └─ test_control_add_club.py
│  └─ application
│     ├─ view
│     │  └─ test_view_applicate_club.py
│     └─ controller
│        └─ test_control_applicate_club.py
├─ .env
├─ .gitignore
├─ requirements.txt
├─ Dockerfile
└─ README.md
```
©generated by [Project Tree Generator](https://woochanleee.github.io/project-tree-generator)