import numpy as np
import string
from PIL import Image,ImageFont,ImageDraw
import argparse
import random
import os

parser=argparse.ArgumentParser()
parser.add_argument('--n_samples',type=int)
args=parser.parse_args()

file_counter=0

smallletters=string.ascii_lowercase
capitalletters=string.ascii_uppercase




#Base backgound.
back=Image.open('background.jpg')

#Different fonts to be used.
fonts_list=os.listdir('./fonts/')
fonts_list=['./fonts/'+f for f in fonts_list]

#Lengths of the words.
word_lengths=[]
for l in range(2,21):
	word_lengths.append(l)

#Font size.
font_size=[]
for l in range(10,30):
	font_size.append(l)

file_counter=0


for _ in range(args.n_samples):
	back_c=back.copy()
	font=ImageFont.truetype(random.choice(fonts_list),size=random.choice(font_size))
	word=''.join([random.choice(smallletters) for b in range(random.choice(word_lengths))])
	w,h=font.getsize(word)[0],font.getsize(word)[1]
	back_c=back_c.resize((w+5,h+5))
	draw=ImageDraw.Draw(back_c)
	draw.text((0,0),text=word,font=font,fill='rgb(0,0,0)')
	back_c.save(f'./images/{file_counter}_{word}.jpg')
	file_counter+=1







