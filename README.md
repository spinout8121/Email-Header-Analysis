## Email Header Analysis

This project contains a set of Python scripts for analyzing the IP addresses, URLs, and email addresses found in an email header. The scripts use the VirusTotal, urlscan, and haveibeenpwned APIs to search for information about each IP address, URL, and email address, and generate an HTML report with the results of the searches.

## Requirements

To run the scripts in this project, you will need to have the following Python modules installed:

```
- requests
- re
- subprocess.run

```

You can install these modules by running the following command:

```
pip install -r requirements.txt

```

## Usage

To run the scripts, you can use the following command:

```
python main.py

```

This will run the three separate analysis scripts and generate an HTML report for each analysis. The reports will be saved to files called `ip_analysis.html`, `url_analysis.html`, and `email_analysis.html`.

## Limitations

This script only analyzes email headers, and does not provide any other information about the email itself.
The script is designed to work with a specific input format for the email header, and may not work properly if the header is incomplete or in a different format than expected.
The script relies on the availability and accuracy of the APIs used for each analysis. If any of the APIs are unavailable or return incorrect results, the analysis may be incomplete or incorrect.

## License

This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/licenses/MIT) file for details.
