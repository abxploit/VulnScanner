COMPANY: CODTECH IT SOLUTIONS

NAME: Abinesh M

INTERN ID: CT04DH572

DOMAIN: Cybersecurity & Ethical Hacking

DURATION: 4 Weeks

MENTOR: NEELA SANTOSH

---

# 🔐 Web Application Vulnerability Scanner (SQLi + XSS)

A command-line tool built with Python to automatically scan web pages for **SQL Injection** and **Cross-Site Scripting (XSS)** vulnerabilities by analyzing HTML forms.

---

## ⚙️ Features

✅ Automatically detects and scans all `<form>` elements on a given page  
✅ Detects common **SQL Injection** vulnerabilities  
✅ Detects basic **Reflected XSS** vulnerabilities  
✅ Easy-to-use **CLI interface** with flags  
✅ Designed for Ethical Hacking practice and internships

---

## 📦 Requirements

- Python 3.x  
- `requests`  
- `beautifulsoup4`

Install dependencies:
```bash
pip install requests beautifulsoup4
```

🚀 Usage
Run the scanner with:

bash
```
python vuln_scanner.py <url> [--sqli] [--xss]
```
Examples
Scan for both SQLi and XSS (default):
```
python vuln_scanner.py http://testphp.vulnweb.com/login.php
```
SQLi only:
```
python vuln_scanner.py http://testphp.vulnweb.com/login.php --sqli
```
XSS only:

```
python vuln_scanner.py http://testphp.vulnweb.com/login.php --xss
```
## 🔍 How It Works

Fetches all HTML forms from the given URL

Injects common payloads into each input field:

SQL payloads (e.g. ' OR 1=1 --)

XSS payloads (e.g. <script>alert(1)</script>)

Submits the form and analyzes the response

Flags the form as vulnerable if:

SQL error message is found (SQLi)

Payload is reflected in response (XSS)

## 💡 Example Output

[+] Scanning http://testphp.vulnweb.com/login.php...
[+] Found 1 form(s).

[Form #1] Checking for vulnerabilities...
[!!] SQL Injection vulnerability in form #1 with payload: ' OR '1'='1
[!!] XSS vulnerability in form #1 with payload: <script>alert(1)</script>
--------------------------------------------------
## 📁 File Structure

Vuln_Scanner.py        # Main CLI scanner tool
README.md              # Project documentation

## ⚠️ Legal Disclaimer
This tool is for educational purposes only.
Do not scan websites without proper authorization.
Use only on targets you own or are permitted to test.

## 👨‍💻 Author
abxploit – CODTECH Internship
Built with 💻 using Python and 💡 powered by ethical hacking fundamentals.

## OUTPUT

<img width="739" height="212" alt="Image" src="https://github.com/user-attachments/assets/42844887-b538-403c-a1b0-a39de7a40eb7" />
