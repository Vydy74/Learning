from fastapi import FastAPI, Path, HTTPException
from typing_extensions import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_users():

    return users


@app.post("/user/{username}/{age}")
async def post_user(
        username: Annotated[
            str,
            Path(
                min_length=5,
                max_length=20,
                description="Enter username",
                example="UrbanUser"
            )
        ],
        age: Annotated[
            int,
            Path(
                ge=18,
                le=120,
                description="Enter age",
                example=24
            )
        ]
):
    """
    Создаем нового пользователя.
    """
    if not users:
        user_id = 1
    else:
        user_id = max(map(int, users.keys())) + 1
    users[str(user_id)] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
        user_id: Annotated[
            int,
            Path(
                ge=1,
                description="Enter User ID",
                example=1
            )
        ],
        username: Annotated[
            str,
            Path(
                min_length=5,
                max_length=20,
                description="Enter username",
                example="UrbanProfi"
            )
        ],
        age: Annotated[
            int,
            Path(
                ge=18,
                le=120,
                description="Enter age",
                example=28
            )
        ]
):
    """
    Обновляем данные пользователя.
    """
    if str(user_id) not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[str(user_id)] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} has been updated"


@app.delete("/user/{user_id}")
async def delete_user(
        user_id: Annotated[
            int,
            Path(
                ge=1,
                description="Enter User ID",
                example=2
            )
        ]
):
    """
    Удаляем пользователя.
    """
    if str(user_id) not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[str(user_id)]
    return f"User {user_id} has been deleted"


