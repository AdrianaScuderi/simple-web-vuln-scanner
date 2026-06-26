# Simple Web Vulnerability Auditor and Recon Tool

A lightweight, educational Python tool designed for passive web security auditing and basic misconfiguration reconnaissance. 

This project was developed as a personal training exercise to deepen my understanding of HTTP/HTTPS protocols, server response behaviors, and operational security (Opsec) principles applied to network monitoring.

## Features
* **Security Headers Auditing:** Verifies the presence of critical defensive HTTP headers (such as `Strict-Transport-Security` and `X-Frame-Options`) to assess resilience against MITM and Clickjacking attacks.
* **Information Disclosure Detection:** Performs targeted checks for exposed sensitive configuration files or directories (e.g., `.env`, `.git/`, `config.php`).
* **Opsec & Request Masking:** Implements User-Agent spoofing to simulate legitimate browser traffic, minimizing the script's fingerprint in target access logs.
* **Smart Error Handling:** Actively manages connection exceptions and analyzes HTTP status codes, properly documenting access restrictions like *403 Forbidden* responses.

## Installation and Usage

Requested Python installed on your pc.

1. Clone the repository:
   git clone https://github.com/YOUR_USERNAME/NAME_REPO.git
   cd NAME_REPO

2. Install the required dependencies:
   pip install requests

3. Run the script:
   python scanner.py


## Legal Disclaimer
This tool is developed strictly for educational purposes and authorized security auditing (Ethical Hacking / Penetration Testing). Using this software against targets without prior written consent is illegal. The author assumes no liability for any misuse or damage caused by this program.