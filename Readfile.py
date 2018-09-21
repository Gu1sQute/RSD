from matplotlib import pyplot as plt
import numpy as np
from io import StringIO
from PIL import *
OCT_infile = open('Test1.raw','rb')
# Dimension: 648 x 488 x 578 (pixel) 
dimX = 648
dimY = 488
dimZ = 578
# i for dimZ
#i = 48
OCT_image_array = np.fromfile(OCT_infile,dtype=float,count=dimX * dimY * dimZ)
i = int(input("Please input the image dimension Z you want to check:(max:578)"))
OCT_image = OCT_image_array[(dimX * dimY * i):(dimX * dimY * (i+1))+1]
OCT_image = Image.frombuffer("F",(dimX,dimY),OCT_image,"raw","F",0,1)
#Show Pic
plt.imshow(OCT_image)
plt.show()
#for output this image
OCT_out = OCT_image.convert('L')
OCT_out.save('image.jpg')
