import qrcode

data = input("Enter Website URL or Text: ").strip()
filename = input("Enter filename:").strip()

#Strip is used to remove any extra spaces in input data so it will ignore space is url and filename

qr = qrcode.QRCode(box_size = 20, border = 5)
qr.add_data(data)
image = qr.make_image (fill_color = 'cyan', back_color = 'black')

#You can change fill_color and back_color as per your choice I Like neon so I kept it

image.save(filename)
print (f'QR Code generated and saved as {filename}')
# Always add .png or .jpg at the end of filename while saving !!