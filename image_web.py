import requests
from bs4 import BeautifulSoup
import os
import csv

def scrape_images(url, save_folder):
    # Create a directory to save images if it doesn't exist
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # Fetch the HTML content of the webpage
    response = requests.get(url)
    if response.status_code == 200:
        # Parse HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all img tags
        img_tags = soup.find_all('img')

        # Extract image URLs and download images
        for img_tag in img_tags:
            img_url = img_tag.get('src')
            if img_url:
                # Download the image
                img_response = requests.get(img_url)
                if img_response.status_code == 200:
                    # Get the image filename
                    img_filename = os.path.join(save_folder, os.path.basename(img_url))
                    # Save the image
                    with open(img_filename, 'wb') as img_file:
                        img_file.write(img_response.content)
                    print(f"Downloaded: {img_filename}")
                else:
                    print(f"Failed to download image: {img_url}")
    else:
        print(f"Failed to fetch webpage: {url}")

# Example usage
url = 'https://www.geeksforgeeks.org/binary-search/'
save_folder = 'Binary Search'
scrape_images(url, save_folder)

# extracting data from any website
def Extract(url):
	response=requests.get(url=url).content
	soup=BeautifulSoup(response,'lxml')
	tag=soup.find('table',{'class':'sidebar sidebar-collapse nomobile nowraplinks hlist'})
	h=tag.find_all("ul")
	content=[li.text for li in h]

	with open("wiki.csv", "w") as f:
		w = csv.writer(f)
		w.writerow(content)
  

Extract('https://en.wikipedia.org/wiki/Artificial_intelligence#Intellectual_property')
