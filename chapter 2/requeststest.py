import requests
from io import BytesIO
from PIL import Image

r = requests.get("http://www.nmgncp.com/data/out/154/4914068-galaxy-wallpaper-png.png")

print("Status Code:" , r.status_code)

image = Image.open(BytesIO(r.content))

print(image.size, image.format, image.mode)
path = "./image2." + image.format

try:
    image.save(path, image.format)
except IOError:
    print("Cannot save image")