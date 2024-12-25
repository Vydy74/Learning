from fastapi import APIRouter, Depends, status, HTTPException
from slugify import slugify
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated, List
from sqlalchemy import select, insert, update, delete

from app.models.user import User
from app.schemas import CreateUser, UpdateUser

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/")
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    return users

@router.get("/user_id")
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")
    return user

@router.post("/create")
async def create_user(user_data: CreateUser, db: Annotated[Session, Depends(get_db)]):
    db.execute(insert(User).values(username=user_data.username,
                                   firstname=user_data.firstname,
                                   lastname=user_data.lastname,
                                   age=user_data.age,
                                   slug=slugify(user_data.username)))
    db.commit()
    return {
        "status_code": status.HTTP_201_CREATED,
        "transaction": "Successful"
    }


@router.put("/update_user")
async def update_user(db: Annotated[Session, Depends(get_db)], user_id: int, update_user: UpdateUser):
    updated_user = select(User).where(User.id == user_id)
    user = db.scalar(updated_user)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no category found"
        )
    # else:
    #     pass

    db.execute(update(User).where(User.id == user_id).values(
        username=update_user.username,
        firstname=update_user.firstname,
        lastname=update_user.lastname,
        age=update_user.age,
        slug=slugify(update_user.username)
    ))
    db.commit()
    return {
        "status_code": status.HTTP_200_OK,
        "transaction": "Category update successful"
    }

@router.delete("/delete")
async def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):

    # Проверка
    user_query = select(User).where(User.id == user_id)
    user = db.scalar(user_query)
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    # Удаляем пользователя
    db.execute(delete(User).where(User.id == user_id))
    db.commit()
    return {
        "status_code": status.HTTP_200_OK,
        "transaction": "User delete is successful!",
    }
