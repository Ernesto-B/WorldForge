from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.models import User

DATABASE_URL = "mysql+pymysql://root:rootpassword@localhost:8080/worldforge_db"     # Change on prod

engine = create_engine(DATABASE_URL, echo=False)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)    # Sessions for ORM operations


def get_db():
    db = SessionLocal()

    try:
        yield db    # Returned to the route or service, then closed automatically
    finally:
        db.close()


# For testing db connectivity
if 0:
    connection = engine.connect()   # Connection for raw SQL operations
    print("\nDatabase connected successfully!")
    db = SessionLocal()
    user = db.query(User).first()
    print(user)
    db.close()
    connection.close()

