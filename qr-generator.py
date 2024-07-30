import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1,error_correction=qrcode.ERROR_CORRECT_H,box_size=10,border=3)
qr.add_data("https://drive.google.com/file/d/1KxHnCFodB3O5uuZd7ak8uf0vqCHr4ni5/view?usp=drive_link")

qr.make(True)
img=qr.make_image()
img.save("gopi1.png")
