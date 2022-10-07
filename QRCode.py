# Impoert pyqrcode library and QRCode module
import pyqrcode
from pyqrcode import QRCode

# Enter the URL/Path whose QR needs to be generated
url = str(input("Enter the URL/Path whose QR needs to be generated: "))
# Enter output filename as per user
file = str(input("Enter filename of your choice: "))

# Generating QR Code
qrc = pyqrcode.create(url)

# Save QR Code in png using the above input name
qrc.svg(file + ".svg", scale= 8)