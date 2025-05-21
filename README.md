import requests
def check(domain):
    try: return requests.get(f'http://{domain}').status_code == 200
    except: return False
# Commit 33 at 2025-05-21T05:12:00