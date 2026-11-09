import re

import qrcode
from PIL import Image
import qrcode.constants


user_input=input("Enter the url that you want to convert into QR Code:")
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4,)
qr.add_data(user_input)
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="blue")
safe_name = re.sub(r"[^A-Za-z0-9._-]", "_", user_input).strip("._") or "qrcode"
img.save(safe_name+".png")
print(f"Saved {safe_name}.png")
