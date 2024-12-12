from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def welcome() -> str:
    return {"Главная страница"}

@app.get("/user")
async def user_predator(username: str, age: int) -> str:
    return {"User": username, "Age": age}

@app.get("/user/admin")
async def welcome_admin() -> str:
    return {"Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def welcome_user(user_id: int) -> str:
    return {f"Вы вошли как пользователь № {user_id}"}
