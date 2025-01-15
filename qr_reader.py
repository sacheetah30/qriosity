from pyzbar.pyzbar import decode
from PIL import Image

def decode_qr_code(image_path):
    code = Image.open(image_path)
    decoded_objects = decode(code)
    for obj in decoded_objects:
        return obj.data.decode("utf-8")
