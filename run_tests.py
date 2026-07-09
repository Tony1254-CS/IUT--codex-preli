import os
import sys
import threading
import time
import requests
from concurrent.futures import ThreadPoolExecutor

BASE_URL = "http://localhost:8000"

def wait_for_server():
    for _ in range(30):
        try:
            r = requests.get(f"{BASE_URL}/health")
            if r.status_code == 200:
                return True
        except:
            pass
        time.sleep(0.5)
    return False

def reset_db():
    if os.path.exists("cowork.db"):
        os.remove("cowork.db")

def run_tests():
    # We will write the tests here.
    pass

if __name__ == "__main__":
    reset_db()
    # start server
    import subprocess
    proc = subprocess.Popen([sys.executable, "-m", "uvicorn", "app.main:app", "--port", "8000"])
    if not wait_for_server():
        print("Server failed to start")
        proc.kill()
        sys.exit(1)
        
    try:
        run_tests()
    finally:
        proc.kill()
