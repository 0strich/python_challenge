from PIL import Image

im = Image.open('cave.jpg')
(x, y) = im.size

even = Image.new('RGB', ((x // 2, y // 2)))
odd= Image.new('RGB', ((x // 2, y // 2)))

for i in range(x):
    for j in range(y):
        p = im.getpixel((i,j))
        if((i+j)%2 == 1):
            odd.putpixel((i//2, j//2), p)
        else:
            even.putpixel((i//2, j//2), p)

even.save('even.jpg')
odd.save('odd.jpg')
