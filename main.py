import subprocess

# Run the IP address analysis script
subprocess.call(["python", "check_ip_reputation.py"])

# Run the URL analysis script
subprocess.call(["python", "scan_url.py"])

# Run the email address analysis script
subprocess.call(["python", "check_pwned_email.py"])