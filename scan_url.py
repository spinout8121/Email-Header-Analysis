import requests

# Import the email header as a string
with open("email_headers.txt", "r") as f:
    email_header = f.read()

# Use a regular expression to find all URLs in the header
import re
urls = re.findall(r'https?://[^\s]+', email_header)

# Set the API key for the urlscan API
api_key = "your-api-key-here"

# Check each URL against the urlscan API
html_output = "<h1>Email Header Analysis</h1>"
html_output += "<p>The following URLs were found in the header:</p>"
html_output += "<ul>"
for url in urls:
    html_output += f"<li>{url}</li>"
html_output += "</ul>"

# Add a table with the results of the urlscan and Symantec SiteReview searches
html_output += "<h2>URL Analysis Results</h2>"
html_output += "<p>The following table shows the results of analyzing each URL with the urlscan and Symantec SiteReview APIs:</p>"
html_output += "<table>"
html_output += "<tr><th>URL</th><th>urlscan results</th><th>Symantec SiteReview results</th></tr>"

# Add a table row for each URL
for url in urls:
    # Check the URL with the urlscan API
    urlscan_response = requests.get(f'https://urlscan.io/api/v1/scan/', params={'url': url})
    if urlscan_response.status_code == 200:
        # The URL was scanned successfully by urlscan
        urlscan_results = urlscan_response.json()
        print(urlscan_results)
        urlscan_link = f"https://urlscan.io/result/{urlscan_results['uuid']}"
    else:
        # There was an error with the urlscan API
        urlscan_link = "Error"

    # Check the URL with the Symantec SiteReview API
    sitereview_response = requests.get(f'https://sitereview.bluecoat.com/rest/categorization', params={'url': url})
    if sitereview_response.status_code == 200:
        # The URL was analyzed successfully by Symantec SiteReview
        sitereview_results = sitereview_response.json()
        sitereview_category = sitereview_results['categorization']
    else:
        # There was an error with the Symantec SiteReview API
        sitereview_category = "Error"

    html_output += f'<tr><td style="white-space: pre-wrap">{url}</td><td><a href="{urlscan_link}">urlscan results</a></td><td>{sitereview_category}</td></tr>'

html_output += "</table>"

# Save the HTML output to a file
with open("url_analysis.html", "w") as f:
    f.write(html_output)