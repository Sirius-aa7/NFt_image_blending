from PIL import Image, ImageDraw

img = Image.open('im1.jpg').convert("RGBA")
x,y = img.size
img2 = Image.open('paap.jpg').convert("RGBA").resize((x,y))
img4 = Image.open('noise.png').convert("RGBA").resize((x,y))
img5 = Image.open('sky2.jpg').convert("RGBA").resize((x,y))

img.putalpha(75)
img2.putalpha(75)
img4.putalpha(120)
img5.putalpha(75)

img3 = Image.alpha_composite(img, img2)
img3 = Image.alpha_composite(img3,img4)
img3 = Image.alpha_composite(img3,img5)
img3.show()

img3.save('luic.png')