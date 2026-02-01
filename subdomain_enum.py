import requests
import sys

def enumerate_subdomains(domain, wordlist_path):
    print(f"[*] Enumerating subdomains for {domain} using wordlist: {wordlist_path}")
    found_subdomains = []
    try:
        with open(wordlist_path, "r") as f:
            subdomains = f.read().splitlines()
    except FileNotFoundError:
        print(f"[-] Error: Wordlist file not found at {wordlist_path}")
        sys.exit(1)

    for sub in subdomains:
        full_url = f"http://{sub}.{domain}"
        try:
            response = requests.get(full_url, timeout=1)
            if response.status_code < 400:
                print(f"[+] Found: {full_url} (Status: {response.status_code})")
                found_subdomains.append(full_url)
        except requests.exceptions.ConnectionError:
            pass # Host not found or connection refused
        except requests.exceptions.Timeout:
            pass # Request timed out
        except Exception as e:
            print(f"[-] An error occurred with {full_url}: {e}")
    return found_subdomains

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 subdomain_enum.py <domain> <wordlist_path>")
        sys.exit(1)

    target_domain = sys.argv[1]
    wordlist = sys.argv[2]

    # Create a dummy wordlist for demonstration if it doesn't exist
    if not os.path.exists(wordlist):
        print(f"[*] Creating a dummy wordlist at {wordlist}")
        with open(wordlist, "w") as f:
            f.write("www\nmail\ndev\nadmin\nblog\ntest\napi\ncdn\nshop\napp\n")

    found = enumerate_subdomains(target_domain, wordlist)
    if found:
        print(f"\n[*] Subdomain enumeration complete. Found {len(found)} subdomains.")
    else:
        print(f"\n[*] Subdomain enumeration complete. No subdomains found.")
