from fastapi import FastAPI, HTTPException
from httpx import AsyncClient

app = FastAPI()

# URL внешнего API
EXTERNAL_API_URL = "https://jsonplaceholder.typicode.com/users"


@app.get("/user/{user_id}")
async def get_user_info(user_id: int):
    async with AsyncClient() as client:
        response = await client.get(f"{EXTERNAL_API_URL}/{user_id}")
        if response.status_code == 200:
            user_data = response.json()
            return {
                "id": user_data["id"],
                "name": user_data["name"],
                "email": user_data["email"],
                "phone": user_data["phone"],
            }
        else:
            raise HTTPException(status_code=404, detail="User not found")
