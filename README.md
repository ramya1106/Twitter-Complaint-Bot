# TwitterComplaintBot

TwitterComplaintBot is a Python-based automation script that checks internet speed using Speedtest.net and posts a complaint to Twitter if the actual speed is below the promised speed.

---

## Features

1. **Internet Speed Check**:
   - Automates Speedtest.net to measure download and upload speeds.
   - Compares the measured speeds against predefined promised speeds.

2. **Automated Twitter Complaint**:
   - Logs into Twitter.
   - Tweets a pre-formatted complaint if the internet speed is below expectations.

---

## Requirements

- **Python 3.7 or higher**
- **Google Chrome**
- **ChromeDriver** (matching your Chrome version)
- **Selenium library**

Install Selenium using:

    Pip install selenium

## Setup Instructions

### 1. Download ChromeDriver
    - Ensure you have Google Chrome installed.
    - Download ChromeDriver that matches your browser version from:
      https://chromedriver.chromium.org/downloads

### 2. Update Paths

    - Place ChromeDriver in a directory included in your system PATH.
    - Alternatively, provide the explicit path in the script if ChromeDriver is located elsewhere.

### 3. Edit Script

    # Replace placeholders with your Twitter credentials:

# Replace the email placeholder

    email.send_keys("your_email_here@gmail.com")  
    
    # Replace the username and password placeholders
    username.send_keys("your_twitter_username")  
    password.send_keys("your_password")
    
    # Adjust the PROMISED_DOWN and PROMISED_UP variables as per your internet plan
    PROMISED_DOWN = 200  # Replace with your promised download speed
    PROMISED_UP = 10     # Replace with your promised upload speed

## Disclaimer

### 1. Use Responsibly

    - Ensure you comply with the terms and conditions of Twitter while using this script.

### 2. Credentials Safety

    - Avoid sharing your credentials with others.
    - Consider implementing a secure method to handle credentials, such as environment variables or a configuration file.

