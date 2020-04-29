#importing barcode module (pip install barcode)
import barcode

# defining a variable with class having ean13 (13 numbers can be converted to barcode)
br = barcode.get_barcode_class("ean13")
# 13 digit number you want to convert to barcode
Br = br("0123456789123")
# saving the barcode with name barcode (it will save as barcode.svg in same directory)
qr = Br.save("barcode")
