from fastapi import FastAPI, Path, HTTPException, Request
from typing_extensions import Annotated
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/")
async def get_main_page(request: Request):

    return templates.TemplateResponse(
        "users.html", {"request": request, "users": users}
    )

@app.get("/user/{user_id}")
async def get_user(
    request: Request,
    user_id: Annotated[int, Path(ge=1, description="Enter User ID", example=1)],
):
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse(
                "users.html", {"request": request, "user": user}
            )
    raise HTTPException(status_code=404, detail="User was not found")

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
        user_id = users[-1].id + 1
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    return user


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
    for i, user in enumerate(users):
        if user.id == user_id:
            users[i].username = username
            users[i].age = age
            return users[i]
    raise HTTPException(status_code=404, detail="User was not found")


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
    for i, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(i)
            return deleted_user
    raise HTTPException(status_code=404, detail="User was not found")

users.append(User(id=1, username="UrbanUser", age=24))
users.append(User(id=2, username="UrbanTest", age=22))
users.append(User(id=3, username="Capybara", age=60))