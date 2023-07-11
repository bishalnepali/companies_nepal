import requests
import pandas as pd
import os

df = pd.read_csv('homes.csv')

i = 0
for id, row in df.iterrows():
    # breakpoint()
    if i > 12:
        property_number = row['propertyNo']
        images = row['images']
        try:
            all_images = images.split(',')
        except:
            all_images = []
        for i,image_url in enumerate(all_images):
            try:
                r = requests.get(image_url)
                if not os.path.exists(f'images/{property_number}'):
                    os.makedirs(f'images/{property_number}')
                with open(f'images/{property_number}/image_{i+1}.jpg', 'wb') as f:
                    f.write(r.content)
            except:
                print(f"Error downloading {image_url}")
        print(f"Downloaded {image_url} to images/{property_number}/image_{i+1}.jpg")
    i += 1
    print(i)
