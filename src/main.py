from fastapi import FastAPI
from .database import test

app = FastAPI()

print(test)