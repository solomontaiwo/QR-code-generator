import pyqrcode

from PIL import Image

# Ask user what the qr code will contain
link = input("Enter anything to generate QR: ")

# Create qr code based on user input
qr_code = pyqrcode.create(link)

# Create png file with appropriate filename and scale
qr_code.png("QRCode_" + link + ".png", scale = 5)

# Open created file in an image viewer
qr_code.show()