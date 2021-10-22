#!/usr/bin/python
from PIL import Image, ImageDraw, ImageFont, ImageChops, ImageEnhance, ImageOps
import random
import os


Opcion= ['rota','invert','scalgris','contraste','espejo']
def tratam(elecc, ii, jj):
        if elecc=='rota':
                directorio= direct+str(ii)+".bmp"
                imagen = Image.open(directorio)
                imagen = imagen.resize((alto,ancho))
                imagen = imagen.rotate(45)
                directorio =dirout+str(jj)+'rota'+".bmp"
                imagen.save(directorio)
        if elecc=='invert':
                directorio= direct+str(ii)+".bmp"
                imagen = Image.open(directorio)
                imagen = imagen.resize((alto,ancho))
                imagen = ImageChops.invert(imagen)
                directorio =dirout+str(jj)+'invert'+".bmp"
                imagen.save(directorio)
        if elecc=='scalgris':
                directorio= direct+str(ii)+".bmp"
                imagen = Image.open(directorio)
                imagen = imagen.resize((alto,ancho))
                imagen = ImageOps.grayscale(imagen)
                directorio =dirout+str(jj)+'scalgris'+".bmp"
                imagen.save(directorio)
        if elecc=='contraste':
                directorio= direct+str(ii)+".bmp"
                imagen = Image.open(directorio)
                imagen = imagen.resize((alto,ancho))
                imagen = ImageEnhance.Contrast(imagen).enhance(4)
                directorio =dirout+str(jj)+'contraste'+".bmp"
                imagen.save(directorio)
        if elecc=='espejo':
                directorio= direct+str(ii)+".bmp"
                imagen = Image.open(directorio)
                imagen = imagen.resize((alto,ancho))
                imagen = ImageOps.mirror(imagen)
                directorio =dirout+str(jj)+'espejo'+".bmp"
                imagen.save(directorio)
ruta='/home/programacion2/jguillermo/prueba'
cont=os.listdir(ruta)
sigcarpt= len(cont)
NombCarp= 'Carpeta_'+str(sigcarpt)
print("total carpeta es de ",sigcarpt)

path=os.path.join(ruta,NombCarp)
os.mkdir(path)
i=0
j=0
direct="/home/programacion2/jguillermo/cartas/Imagenes/"
dirout= path+'/'

while (i<52):
        i=i+1
        k=0
        alto=100
        ancho=100
        while (k<10):
                k=k+1
                j=j+1
                eleccion= Opcion[random.randint(0, 4)]
                tratam(eleccion,i,j)
