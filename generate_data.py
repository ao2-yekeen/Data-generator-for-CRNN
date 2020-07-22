import numpy as np
import string
from PIL import Image,ImageFont,ImageDraw
import argparse
import random

parser=argparse.ArgumentParser()
parser.add_argument('--n_samples',type=int)
args=parser.parse_args()

file_counter=0

charlist=string.ascii_lowercase


for _ in range(args.n_samples):
    back=Image.open('background.jpg')
    draw=ImageDraw.Draw(back)
    font=ImageFont.truetype('./fonts/arial_narrow_7.ttf',size=30)
    word=''.join([random.choice(charlist) for a in range(np.random.randint(2,8))])
    draw.text((0,0),text=word,font=font,fill='rgb(0,0,0)')
    back.save('./images/'+str(file_counter)+'_'+word+'.jpg')
    file_counter+=1


