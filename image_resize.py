from PIL import Image
from app import app
import os

for filename in os.listdir(app.config['UPLOADS_FOLDER']):
    if filename != '.gitkeep':
        img = app.config['UPLOADS_FOLDER'] + '/' + filename
        im1 = Image.open(img)
        width = 250
        height = 350
        im5 = im1.resize((width, height), Image.ANTIALIAS)
        im5.save(os.path.join(app.config['UPLOADS_FOLDER'], filename))
