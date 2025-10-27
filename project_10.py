import qrcode as qr

img = qr.make("https://www.youtube.com/@ElvishYadavVlogs")
img.save("king of_youtube.png")