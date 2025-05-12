from fastapi import FastAPI
import random

app = FastAPI()

phrases = [
    "Keep pushing forward!",
    "You're doing great!",
    "Small steps lead to big results.",
    "Believe in yourself!",
    "Never give up!",
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Motivator app!"}


@app.get("/health")
def healthcheck():
    return {"status: ok"}


@app.get("/motivate")
def get_phrase():
    return {"message": random.choice(phrases)}
