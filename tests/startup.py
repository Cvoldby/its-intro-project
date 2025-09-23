'''

'''

import os
from pathlib import Path
from dotenv import load_dotenv
import tempfile
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
import pytest

from src.app.db import init_db, get_connection
from src.app.main import app

# Load environment variables
load_dotenv()
DB_PATH = Path(os.getenv("DB_PATH", "data/my_project.db"))
TEST_DB_PATH = Path(tempfile.gettempdir()) / "test_my_project.db"
os.environ["DB_PATH"] = str(TEST_DB_PATH)
client = TestClient(app)

# Basic test to verify test setup
def test_setup():
	assert True

@pytest.fixture(scope="module", autouse=True)
def setup_and_teardown():
	# Setup: Initialize the test database
	if TEST_DB_PATH.exists():
		TEST_DB_PATH.unlink()
	init_db()
	yield
	# Teardown: Remove the test database
	if TEST_DB_PATH.exists():
		TEST_DB_PATH.unlink()

def test_startup_event():
	response = client.get("/")
	assert response.status_code == 200
	assert response.json() == {"Hello": "World"}
