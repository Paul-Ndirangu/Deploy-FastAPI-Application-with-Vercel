# import uvicorn 
# from fastapi import FastAPI
from langcorn import create_service


app = create_service(
    "llm_chain:chain",
    "conversation_chian:conversation"
)


# @app.get("/")
# async def root():
#     return {"message": "Hello World!"}

# @app.post("/home")
# async def home():
#     return {"message": "Hello from FastAPI!"}


# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    