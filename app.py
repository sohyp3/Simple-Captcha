import random
import string
from PIL import Image, ImageDraw, ImageFont

image = Image.new('RGB', (200, 70), 'white')
draw = ImageDraw.Draw(image)

font_size = 30

font_path ='./foley.otf'

font = ImageFont.truetype(font_path,font_size)



letters = 'LIGMA2'
charz = string.ascii_uppercase + string.digits
letters = "".join(random.choice(charz) for _ in range(5))
y = (image.height - font_size) / 2

x_pos = 0

for lett in letters:
    x =( (image.width + font_size) / (len(letters)+1) * x_pos)

    rotation_angle = random.randint(-35, 35)
    opeacity_level = random.randint(100, 200)
    
    letter_img = Image.new('RGBA',(font_size,font_size),(255,255,255,0))
    letter_draw = ImageDraw.Draw(letter_img)
    letter_draw.text((0,0),lett,fill=(0,0,0,opeacity_level),font=font)
    rotated_img = letter_img.rotate(rotation_angle,resample=Image.BICUBIC,expand=True)
        
    image.paste(rotated_img,(int(x),int(y)),rotated_img)

    x_pos +=1 



# Add random noise

for _ in range(300):  
    noise_x = random.randint(0, image.width - 1)
    noise_y = random.randint(0, image.height - 1)
    draw.point((noise_x, noise_y), fill='black')


distorted_image = image.transform(image.size, Image.AFFINE, (1, 0.2, 0, 0, 1, 0), Image.BICUBIC)





# Add the Lines



for _ in range(3):
    start_x = random.randint(0, image.width)
    start_y = random.randint(0, image.height)
    end_x = random.randint(0, image.width)
    end_y = random.randint(0, image.height)

    control_x1 = random.randint(0, image.width)
    control_y1 = random.randint(0, image.height)
    control_x2 = random.randint(0, image.width)
    control_y2 = random.randint(0, image.height)

    draw.line([(start_x, start_y), (control_x1, control_y1), (control_x2, control_y2), (end_x, end_y)], fill='black', width=2)





image.save('out.png')



max_tries = 3
tries = 0 
print(letters)
while  tries <max_tries:
    answer = input('Enter the captcha: (from out.png)')
    if answer.upper() == letters:
        print('Correct Welcome abord')
        break
    else:
        tries +=1
        print('Wrong try again later')
