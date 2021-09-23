import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

data = "Do not forget to subscribe"

### encoding
# making a qrcode with styling
# qr = qrcode.qrcode(version = 1, box_size=10,border=5)
# qr.add_data(data)
# qr.make(fit=True)
# img = qr.make_image(fill_color="red",back_color="white")
# img.save("C:/Users/larat/Documents/Token/new/myqrcode.png")

# making a qrcode with no styling
# img = qrcode.make(data)
# img.save("C:/Users/larat/Documents/Token/new/myqrcode.png")

### decoding
# img = Image.open("C:/Users/larat/Documents/Token/new/myqrcode.png")
# result = decode(img)
# print(result)
