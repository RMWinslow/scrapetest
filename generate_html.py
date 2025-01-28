import requests
from bs4 import BeautifulSoup
from datetime import datetime
import xml.etree.ElementTree as ET

# Fetch the RSS feed from YouTube
rss_url = 'https://www.youtube.com/feeds/videos.xml?channel_id=UCfMJ2MchTSW2kWaT0kK94Yw'
rss_response = requests.get(rss_url)
rss_content = rss_response.content

# Parse the RSS feed
root = ET.fromstring(rss_content)
latest_video = root.find('entry')

# Extract details of the latest video
video_title = latest_video.find('title').text
video_url = latest_video.find('link').attrib['href']
video_thumbnail_url = latest_video.find('{http://search.yahoo.com/mrss/}group').find('{http://search.yahoo.com/mrss/}thumbnail').attrib['url']
video_date = latest_video.find('published').text

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
    <blockquote>
        <h2>Latest Video</h2>
        <p><strong>Title:</strong> {video_title}</p>
        <p><strong>URL:</strong> <a href="{video_url}">{video_url}</a></p>
        <p><strong>Date:</strong> {video_date}</p>
        <img src="{video_thumbnail_url}" alt="Thumbnail">
    </blockquote>
    <p>Generated on: {timestamp}</p>
</body>
</html>
"""

# Write the HTML content to beans.html
with open('beans.html', 'w') as file:
    file.write(html_content)
