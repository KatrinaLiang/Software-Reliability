import subprocess

try:
    r = subprocess.run(["python", "run_tests.py"], timeout=20)
except subprocess.TimeoutExpired as e:
    print(e)
