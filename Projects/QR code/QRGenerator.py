import qrcode

url = input("Enter the website URL: ")
img = qrcode.make(url)
type(img)  # qrcode.image.pil.PilImage
fileName = input("Enter the file name: ")

img.save(fileName + ".png" or "qrcode.png")
