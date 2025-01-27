import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Fetch the content from example.com
url = 'http://example.com'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the main content (for simplicity, we'll grab the first paragraph)
main_content = soup.find('p').text if soup.find('p') else "No content found"

# Get the current timestamp
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Generate the HTML content
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Beans</title>
</head>
<body>
    <h1>Beans</h1>
    <blockquote>{main_content}</blockquote>
    <p>Generated on: {timestamp}</p>
</body>
</html>
"""

# Write the HTML content to beans.html
with open('beans.html', 'w') as file:
    file.write(html_content)
