# working with images, basics
# from https://automatetheboringstuff.com/chapter17/        guide

from PIL import Image, ImageColor
crow = Image.open('crow.png')
crow.size
width, height = crow.size   #sets both variables with what just printed out the line above
crow.filename               #the filename above... 'crow.png'
crow.format                 # this prints 'PNG'
crow.format_description     #this prints 'Portable network graphics'
crow.save('newCrow.jpg')    #automatically saves new file as a JPEG image format

im = Image.new('RGBA', (100, 200), 'purple')   # makes a new image, set size 100 by 200 with tuple, filled with purple
im.save('purpleImage.png')                     # save with name
im2 = Image.new('RGBA', (20, 20))              # make a transparent image, 20 by 20
im2.save('transparentImage.png')

crop = crow.crop((600, 0, 2000, 700))     # crops image
crow.paste(crop, (0, 0))                  # pastes crop on crow image at (0, 0)
crow.save('pasted.png')                   # saves pasted image

#tiles the cropped photo in the size of the original photo
cropWidth, cropHeight = crop.size
crowWidth, crowHeight = crow.size
crowCopy2 = crow.copy()
for left in range (0, crowWidth, cropWidth):
  for top in range(0, crowHeight, cropHeight):
    print (left, top)
    crowCopy2.paste(crop, (left, top))
crowCopy2.save('tiled.png')

#resizing the photo
quartersized = crow.resize((int(crowWidth / 2), int (crowHeight / 2)))
quartersized.save('quarterCrow.png')
quartersized.size()                        # verify resizing
plussized = crow.resize((width, height + 300))
plussized.save('plus.png')
plussized.size                             # verify resizing

crow.rotate(90).save('rotated90.png')      # we can resize and save in the same line
crow.rotate(6).save('rotated6.png')
crow.rotate(6, expand=True).save('rotated6_expanded.png') # resizes the photo, so it is not cropped
crow.rotate(6, expand=True).size                          # verify size increase

crow.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png') #pretty readable code, flips photo
crow.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')

newImage = Image.new('RGBA', (100, 100))
newImage.getpixel((0,0))
for x in range(100):
  for y in range(50):
    newImage.putpixel((x, y), (210, 210, 210))
newImage.save('put.png')                          # should be a rectangle with top half lightgrey
for x in range (100):
  for y in range (50, 100):
    newImage.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))
newImage.save('put2.png')                         # should be a rect with top half lt grey and bottom dark lightgrey
