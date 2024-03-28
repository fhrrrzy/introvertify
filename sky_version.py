import requests
from bs4 import BeautifulSoup
import re

def get_html_content(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Mobile Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve HTML content. Status code: {response.status_code}")
        return None

def extract_version_text(soup):
    notes_element = soup.find('div', class_='notes wrapText collapsed')

    if notes_element:
        anchor_tag = notes_element.find('a')

        if anchor_tag:
            anchor_text = anchor_tag.text
            version_text_match = re.search(r'Sky: Children of the Light (\d+\.\d+\.\d+ \(\d+\))', anchor_text)

            if version_text_match:
                extracted_text = version_text_match.group(1)
                modified_text = extracted_text.replace(' ', '.').replace('(', '').replace(')', '')
                return modified_text

    return None

def get_version():
    url = "https://www.apkmirror.com/apk/thatgamecompany-inc/sky-children-of-the-light/"
    html_content = get_html_content(url)

    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')
        modified_version_text = extract_version_text(soup)

        if modified_version_text:
            return modified_version_text
        else:
            return "Version text not found."

if __name__ == "__main__":
    result = get_version()
    print(result)
