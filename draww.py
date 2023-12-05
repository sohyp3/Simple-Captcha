import string
import random
import time
from PIL import Image, ImageDraw, ImageFont

class DrawCode():
    def __init__(self,code):
        self.font_size = 30
        self.font_path ='./foley.otf'
        
        self.image = Image.new('RGB', (200, 70), 'white')

        self.y =(self.image.height - self.font_size) / 2

        self.draw = ImageDraw.Draw(self.image)
        self.font = ImageFont.truetype(self.font_path,self.font_size)

        self.write_chars(code)
        self.random_noise()
        self.random_lines()

    def output(self):
        self.time_id = time.time()
        self.image.save(f'./static/media/{self.time_id}.png')
        print("New Image Drawn")
        return self.time_id



    def write_chars(self,word):
        x_pos = 0
        for lett in word:
            x =( (self.image.width + self.font_size) / (len(word)+1) * x_pos)

            rotation_angle = random.randint(-35, 35)
            opeacity_level = random.randint(100, 200)
            
            letter_img = Image.new('RGBA',(self.font_size,self.font_size),(255,255,255,0))
            letter_draw = ImageDraw.Draw(letter_img)
            letter_draw.text((0,0),lett,fill=(0,0,0,opeacity_level),font=self.font)
            rotated_img = letter_img.rotate(rotation_angle,resample=Image.BICUBIC,expand=True)
                
            self.image.paste(rotated_img,(int(x),int(self.y)),rotated_img)

            x_pos +=1 
        
    def random_noise(self):
        for _ in range(300):  
            noise_x = random.randint(0, self.image.width - 1)
            noise_y = random.randint(0, self.image.height - 1)
            self.draw.point((noise_x, noise_y), fill='black')


        distorted_image = self.image.transform(self.image.size, Image.AFFINE, (1, 0.2, 0, 0, 1, 0), Image.BICUBIC)


    def random_lines(self):
       for _ in range(3):
            start_x = random.randint(0, self.image.width)
            start_y = random.randint(0, self.image.height)
            end_x = random.randint(0, self.image.width)
            end_y = random.randint(0, self.image.height)

            control_x1 = random.randint(0, self.image.width)
            control_y1 = random.randint(0, self.image.height)
            control_x2 = random.randint(0, self.image.width)
            control_y2 = random.randint(0, self.image.height)

            self.draw.line([(start_x, start_y), (control_x1, control_y1), (control_x2, control_y2), (end_x, end_y)], fill='black', width=2)



def get_random():
    #charz = string.ascii_uppercase + string.digits   
    charz = string.ascii_uppercase # removed the digits cuz its too difficult
    return "".join(random.choice(charz) for _ in range(5))

