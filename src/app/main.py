'''
'''

from fastapi import FastAPI, HTTPException
from app.db import init_db, get_connection

app = FastAPI()

# @app.lifespan("startup")
# def startup_event():
#     init_db()

@app.get("/")
def read_root():
	return {"Hello": "World"}

