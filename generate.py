import qrcode
from PIL import Image

data = "kya kar rhi ha"

qr = qrcode.QRCode(version=1,box_size=10,border=3)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color = 'red',back_color = 'white')

img.save("/home/kautuk/Documents/Python/QR Code Reader and Generator/myQrCode1.png")
