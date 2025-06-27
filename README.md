import requests
def check(domain):
    try: return requests.get(f'http://{domain}').status_code == 200
    except: return False
# Commit 27 at 2025-06-27T12:59:00