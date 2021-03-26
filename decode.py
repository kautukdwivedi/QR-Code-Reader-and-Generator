from pyzbar.pyzbar import decode
from PIL import Image

img=Image.open("/home/kautuk/Documents/Python/QR Code Reader and Generator/myQrCode1.png")
decoded = decode(img)
for attr in decoded:
    print(attr.data)