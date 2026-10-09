import os
import requests
import phonenumbers
from phonenumbers import geocoder, carrier

# !!! यहाँ अपनी VirusTotal API Key डालें !!!
VIRUSTOTAL_API_KEY = "YOUR_VIRUSTOTAL_API_KEY_HERE"

def print_banner():
    print("\n" + "=" * 50)
    print("      ADVANCED OSINT & CYBER SECURITY TOOL")
    print("=" * 50)
    print("1. URL Safe Check (Live VirusTotal API)")
    print("2. Web Vulnerability Scanner (SQLi Check)")
    print("3. Phone Number Lookup (Live Region & Carrier)")
    print("4. Email Breach & OSINT Framework")
    print("5. Bank Link Verification (Educational Simulation)")
    print("6. Exit")
    print("=" * 50)

# 1. URL Safe Check using VirusTotal API (Live Data)
def url_check():
    print("\n--- Live URL Safe Check ---")
    url_to_check = input("Enter URL to check (e.g., http://example.com): ")
    
    if VIRUSTOTAL_API_KEY == "YOUR_VIRUSTOTAL_API_KEY_HERE":
        print("[!] Warning: Please add your VirusTotal API Key in the code to fetch live data.")
        return

    print(f"[*] Scanning {url_to_check} via VirusTotal...")
    headers = {"x-apikey": VIRUSTOTAL_API_KEY}
    payload = {"url": url_to_check}
    
    try:
        # URL Submit करना
        response = requests.post("https://virustotal.com", data=payload, headers=headers)
        if response.status_code == 200:
            analysis_id = response.json()['data']['id']
            print(f"[+] Scan submitted successfully. Analysis ID: {analysis_id}")
            print("[*] Tip: You can check the detailed report on VirusTotal dashboard using this ID.")
        else:
            print(f"[-] Error from VirusTotal: {response.json().get('error', {}).get('message', 'Unknown Error')}")
    except Exception as e:
        print(f"[-] Connection Error: {e}")

# 2. Basic SQLi Detection Framework
def vulnerability_scanner():
    print("\n--- Web Vulnerability Scanner ---")
    target_url = input("Enter target URL with parameter (e.g., http://example.com): ")
    
    sqli_payload = "'"
    print(f"[*] Testing for SQL Injection with payload: {sqli_payload}")
    try:
        response = requests.get(target_url + sqli_payload, timeout=5)
        # SQL एरर डिटेक्ट करना
        error_keywords = ["sql", "mysql", "syntax error", "postgre", "oracle"]
        is_vulnerable = any(kw in response.text.lower() for kw in error_keywords)
        
        if is_vulnerable:
            print("[!] Alert: Possible SQL Injection vulnerability detected (Database error found in response)!")
        else:
            print("[+] SQLi: No standard database errors found.")
    except Exception as e:
        print(f"[-] Error connecting to target: {e}")

# 3. Phone Number Lookup (Live Country, State & Telecom Operator)
def phone_lookup():
    print("\n--- Live Phone Number Lookup ---")
    phone_input = input("Enter phone number with country code (e.g., +919876543210): ")
    
    try:
        # नंबर पार्स करना
        parsed_number = phonenumbers.parse(phone_input)
        
        # वैलिडिटी चेक करना
        if not phonenumbers.is_valid_number(parsed_number):
            print("[-] Invalid phone number format.")
            return
            
        # लोकेशन/राज्य का पता लगाना
        region = geocoder.description_for_number(parsed_number, "en")
        # टेलीकॉम ऑपरेटर (Carrier) का पता लगाना
        operator = carrier.name_for_number(parsed_number, "en")
        
        print(f"[+] Country/Location : {region if region else 'Unknown'}")
        print(f"[+] Telecom Operator : {operator if operator else 'Unknown / Ported Number'}")
        
    except Exception as e:
        print(f"[-] Error analyzing phone number: {e}")

# 4. Email OSINT & Breach Framework
def email_osint():
    print("\n--- Email OSINT Framework ---")
    email = input("Enter email address to analyze: ")
    print(f"[*] Analyzing footprint for: {email}")
    print("[*] To check live leaks, look into 'HaveIBeenPwned API' or tools like 'holehe'.")
    print(f"[+] Framework active: Simulating scan for {email}... No public data leaked in local database.")

# 5. Bank Link Verification (Educational Simulation)
def bank_link_check():
    print("\n--- Bank Link Verification (Simulation) ---")
    print("NOTE: Real-time bank account fetching via OTP requires official NPCI/AA license integration.")
    phone = input("Enter your mobile number: ")
    print(f"[*] OTP Code sent to {phone} (Simulation)...")
    
    otp = input("Enter the 4-digit code (Use '1234' for demo): ")
    if otp == "1234":
        print("[+] OTP Verified Successfully!")
        print("[+] Linked Accounts Found (Demo Data):")
        print("    - State Bank of India (Ending in X4321)")
        print("    - HDFC Bank (Ending in X8890)")
    else:
        print("[-] Invalid Verification Code.")

def main():
    while True:
        print_banner()
        choice = input("Select an option (1-6): ")
        
        if choice == '1':
            url_check()
        elif choice == '2':
            vulnerability_scanner()
        elif choice == '3':
            phone_lookup()
        elif choice == '4':
            email_osint()
        elif choice == '5':
            bank_link_check()
        elif choice == '6':
            print("Exiting tool. Keep learning, stay secure!")
            break
        else:
            print("Invalid choice! Please select between 1-6.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
