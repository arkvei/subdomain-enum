import requests
def check(domain):
    try: return requests.get(f'http://{domain}').status_code == 200
    except: return False
# Commit 35 at 2025-03-05T08:25:00