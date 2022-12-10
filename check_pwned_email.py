import requests

# Import the email header as a string
with open("email_headers.txt", "r") as f:
    email_header = f.read()

# Use a regular expression to find all email addresses in the header
import re
email_addresses = re.findall(r'[\w\.-]+@[\w\.-]+', email_header)

# Convert the email addresses list to a set to remove duplicates
email_addresses = set(email_addresses)

# Check each email address against the Have I Been Pwned API
html_output = "<h1>Email Header Analysis</h1>"
html_output += "<p>The following email addresses were found in the header:</p>"
html_output += "<ul>"
for email in email_addresses:
    html_output += f"<li>{email}</li>"
html_output += "</ul>"

# Add a table with the results of the breach search
html_output += "<h2>Breach Search Results</h2>"
html_output += "<p>The following table shows the results of searching for each email address on the Have I Been Pwned website:</p>"
html_output += "<table>"

# Add a table row for each email address
for email in email_addresses:
    response = requests.get(f'https://haveibeenpwned.com/api/v2/breachedaccount/{email}')
    if response.status_code == 200:
        # The email was found in a breach
        html_output += f'<tr><td>{email}</td><td><a href="https://haveibeenpwned.com/{email}">Breach details</a></td></tr>'
    else:
        # The email was not found in a breach
        html_output += f'<tr><td>{email}</td><td>No breaches found</td></tr>'

html_output += "</table>"

# Save the HTML output to a file
with open("email_analysis.html", "w") as f:
    f.write(html_output)