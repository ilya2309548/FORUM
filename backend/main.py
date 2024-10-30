
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session, declarative_base, Mapped, mapped_column
from sqlalchemy.exc import OperationalError
from sqlalchemy import text, MetaData, Column, Table, Integer, String, ForeignKey, select, inspect
from sql_app.database import engine
from sql_app.schemas import UserCreate, User
from sql_app.crud import  get_user, get_user_by_email, create_user
from sql_app.database import Base

# Base.metadata.create_all(bind=engine)

# Подключаем уже созданный SessionLocal
from sql_app.database import SessionLocal
app = FastAPI()


@app.get("/")
def root():
    return "hello"


app = FastAPI()

# Функция для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Эндпоинт для проверки подключения к базе данных


@app.get("/check_db_connection")
def check_db_connection(db: Session = Depends(get_db)):
    try:
        # Простой SQL-запрос для проверки подключения
        db.execute(text("SELECT 1"))
        return {"status": "Database connection is successful"}
    except OperationalError:
        return {"status": "Database connection failed"}


# with engine.connect() as connection:
#     result = connection.execute(text("select now()"))
#     print(result.all())
#
# metadata = MetaData()
#
# user_table = Table(
#     "Users",
#     metadata,
#     Column("id",Integer,primary_key=True),
#     Column("name", String),
# )
#
# address_table = Table(
#     "Address",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("name", String),
#     Column("user_id", ForeignKey('Users.id'))
# )
#
# metadata.drop_all(engine)

# Base = declarative_base()
# class AbstractModel(Base):
#     __abstract__ = True
#     id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
#
#
# class UserModel(AbstractModel):
#     __tablename__ = 'users'
#     name: Mapped[str] = mapped_column()

#
# class ProductModel(AbstractModel):
#     __tablename__ = 'products'
#     name: Mapped[str] = mapped_column()
#     user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
#
#
# with Session(engine) as session:
#     with session.begin():
#         # Base.metadata.create_all(engine)
#         user = UserModel(name="Ilya")
#         session.add(user)
#         session.flush()  # Этот вызов обеспечит, что пользователь уже имеет присвоенный ID
#
#         # Теперь создаём продукт и указываем id только что созданного пользователя
#         product = ProductModel(name="milk", user_id=user.id)
#         session.add(product)


@app.post("/users/")
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)

# @app.delete("/users/{user_id}")
# def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
#     return delete_user(db=db, user_id=user_id)


@app.get("/users/{user_id}", response_model = User)
def get_user_endpoint(user_id: int, db:Session=Depends(get_db)):
    user = get_user(db=db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail = "user is not found")
    return user