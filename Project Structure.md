```txt
worldforge/backend
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── core/
│   │   └── security.py           # OAuth, JWT, RBAC logic
│   ├── routers/
│   │   ├── auth_router.py
│   │   ├── user_router.py
│   │   ├── world_router.py
│   │   ├── campaign_router.py
│   │   ├── region_router.py
│   │   ├── session_router.py
│   │   ├── marker_router.py
│   │   ├── event_router.py
│   │   └── lore_router.py
│   ├── controllers/
│   │   ├── auth_controller.py
│   │   ├── user_controller.py
│   │   ├── world_controller.py
│   │   ├── campaign_controller.py
│   │   ├── region_controller.py
│   │   ├── session_controller.py
│   │   ├── marker_controller.py
│   │   ├── event_controller.py
│   │   └── lore_controller.py
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── user_service.py
│   │   ├── world_service.py
│   │   ├── campaign_service.py
│   │   ├── region_service.py
│   │   ├── session_service.py
│   │   ├── marker_service.py
│   │   ├── event_service.py
│   │   └── lore_service.py
│   ├── repositories/
│   │   ├── auth_repository.py
│   │   ├── user_repository.py
│   │   ├── world_repository.py
│   │   ├── campaign_repository.py
│   │   ├── region_repository.py
│   │   ├── session_repository.py
│   │   ├── marker_repository.py
│   │   ├── event_repository.py
│   │   └── lore_repository.py
│   └── db/
│       ├── database.py            # Database connection setup
│       └── models.py              # SQLAlchemy models
│
└── README.md
```