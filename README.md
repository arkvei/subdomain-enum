import requests
def check(domain):
    try: return requests.get(f'http://{domain}').status_code == 200
    except: return False
# Commit 22 at 2025-12-21T19:14:00