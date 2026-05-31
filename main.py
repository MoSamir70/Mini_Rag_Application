from fastapi import FastAPI

app = FastAPI()

# Call Function form from API
# Control Function Using Decorator with sepeate Logic

@app.get("/welcome")


def welcome():
    return {"message": "Welcome to Mini RAG Application!"}