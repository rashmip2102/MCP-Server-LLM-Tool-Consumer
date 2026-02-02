import requests
import logging

logging.basicConfig(level=logging.INFO, format="[CLIENT] %(message)s")

BASE_URL = "http://127.0.0.1:8000"

# -------- Discovery --------
tools = requests.get(f"{BASE_URL}/tools").json()
logging.info(f"Discovered tools: {tools}")

resources = requests.get(f"{BASE_URL}/resources").json()
logging.info(f"Discovered resources: {resources}")

# -------- Fake LLM Decision --------
llm_decision = {
    "tool": "analyze_text",
    "args": {"text": "Hello World"}
}

# -------- Execution --------
response = requests.post(
    f"{BASE_URL}/call",
    json=llm_decision
).json()

print("Analysis Result:", response)
