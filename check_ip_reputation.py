import requests

# Import the email header as a string
with open("email_headers.txt", "r") as f:
    email_header = f.read()

# Use a regular expression to find all IP addresses in the header
import re
ip_addresses = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', email_header)

# Convert the ip addresses list to a set to remove duplicates
ip_addresses = set(ip_addresses)

# Check each IP address against the VirusTotal API
html_output = "<h1>Email Header Analysis</h1>"
html_output += "<p>The following IP addresses were found in the header:</p>"
html_output += "<ul>"
for ip in ip_addresses:
    html_output += f"<li>{ip}</li>"
html_output += "</ul>"

# Add a table with the results of the VirusTotal search
html_output += "<h2>IP Analysis Results</h2>"
html_output += "<p>The following table shows the results of analyzing each IP address with the VirusTotal API:</p>"
html_output += "<table>"
html_output += "<tr><th>IP Address</th><th>VirusTotal results</th></tr>"

# Add a table row for each IP address
for ip in ip_addresses:
    # Check the IP address with the VirusTotal API
    virustotal_response = requests.get(f'https://www.virustotal.com/vtapi/v2/ip-address/report', params={'apikey': 'your-api-key-here', 'ip': ip})
    if virustotal_response.status_code == 200:
        # The IP address was analyzed successfully by VirusTotal
        virustotal_results = virustotal_response.json()
        virustotal_link = f"https://www.virustotal.com/gui/ip-address/{ip}/detection"
    else:
        # There was an error with the VirusTotal API
        virustotal_link = "Error"

    # Add the results of the VirusTotal search to the table
    html_output += f'<tr><td>{ip}</td><td><a href="{virustotal_link}">VirusTotal results</a></td></tr>'

html_output += "</table>"

# Save the HTML output to a file
with open("ip_analysis.html", "w") as f:
    f.write(html_output)