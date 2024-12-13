from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def welcome():
    return "Главная страница"

@app.get("/user")
async def user_predator(username: str, age: int):
    return f"Информация о пользователе: Имя: {username}, Возраст: {age}"

@app.get("/user/admin")
async def welcome_admin():
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def welcome_user(user_id: int):
    return f"Вы вошли как пользователь № {user_id}"
