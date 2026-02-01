# Subdomain Enumerator

A Python script to discover subdomains for a given domain using a wordlist.

## Features
*   Uses a wordlist to test common subdomain prefixes.
*   Checks HTTP status codes to identify active subdomains.
*   Handles connection errors and timeouts gracefully.

## Usage
```bash
python3 subdomain_enum.py <domain> <wordlist_path>
```

### Example
```bash
python3 subdomain_enum.py example.com subdomains.txt
```

## Requirements
*   Python 3.x
*   `requests` library (`pip install requests`)

## How it Works
The script reads a list of potential subdomain prefixes from a wordlist. For each prefix, it constructs a full subdomain (e.g., `www.example.com`) and attempts to make an HTTP request. If the request is successful and returns a status code less than 400, the subdomain is considered active and reported.
