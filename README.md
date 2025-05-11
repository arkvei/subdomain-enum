import requests
def check(domain):
    try: return requests.get(f'http://{domain}').status_code == 200
    except: return False
# Commit 20 at 2025-05-11T15:44:00