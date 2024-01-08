import requests
from bs4 import BeautifulSoup
import os



url = " type your url"
folder = " type folder name"


def download_images(url, folder_name):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        images = soup.find_all('img')

        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        for idx, image in enumerate(images, start=1):
            image_url = image.get('src')

            if image_url and 'http' in image_url:
                image_data = requests.get(image_url).content

                with open(f'{folder_name}/image_{idx}.jpg', 'wb') as img_file:
                    img_file.write(image_data)
                print(f"Image #{idx} downloaded: {image_url}")
            else:
                print(f"Invalid or no URL found for image #{idx}")
    else:
        print("Error accessing the URL.")

download_images(url, folder)
