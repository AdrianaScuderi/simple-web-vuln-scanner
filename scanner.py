import requests

target_url = "..."  # put here a common test site to run the script
                                  
# Pretend to be a real browser to avoid being blocked by some websites that filter out non-browser requests (Google Chrome)
headers_pretend = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

print(f"[*] Analyzing the site: {target_url}...\n")

try:
    # Send the HTTP GET request passing the disguised headers
    response = requests.get(target_url, headers=headers_pretend, timeout=5)
    
    # Check if the response was successful (status code 200)
    if response.status_code == 200:
        print("[+] The site is up and running!")
        headers = response.headers
    else:
        print(f"[-] The site returned an error: {response.status_code}")
        if response.status_code == 403:
            print("[-] Access denied (403). The site may have security measures in place, excellent!")
        exit() 

except requests.exceptions.RequestException as e:
    print(f"[-] Connection error: {e}")
    exit()

print("\n=== SECURITY HEADER CHECK ===")

# 1. Check for HSTS
if "Strict-Transport-Security" in headers:
    print("[+] GOOD: Strict-Transport-Security is present.")
else:
    print("[-] VULNERABILITY: Missing Strict-Transport-Security! This site could be vulnerable to MITM attacks.")

# 2. Check for X-Frame-Options
if "X-Frame-Options" in headers:
    print("[+] GOOD: X-Frame-Options is present.")
else:
    print("[-] VULNERABILITY: Missing X-Frame-Options! This site is vulnerable to Clickjacking.")

print("\n=== RICERCA FILE SENSIBILI EXPOSED ===")

file_sus = [".env", ".git/", "config.php", "backup.zip"] # List of common files that should never be publicly accessible

for file in file_sus:
    # Create the complete URL (e.g., https://site.com/.env)
    url_extended = f"{target_url}/{file}"
    
    # Applichiamo gli headers camuffati anche qui, per mantenere l'Opsec coerente durante la ricerca file
    test_file = requests.get(url_extended, headers=headers_pretend, timeout=3)
    
    # If the server responds with status 200 (OK), it means the file exists and is accessible!
    if test_file.status_code == 200:
        print(f"[!] ALERT: Found exposed file! -> {url_extended}")
    else:
        print(f"[+] SAFE: {file} is not accessible (Status: {test_file.status_code})")

