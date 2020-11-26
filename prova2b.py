# bibliotecas para processamento de imagem
import PIL
from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Q01. Monte um Código em Python que sem o uso de OpenCV faça a abertura e informe dados do arquivo importado.

img = Image.open('carla.jpg')
# img.show()
width, height = img.size

# exibe tamanho/dimensoes da imagem
print("DADOS DO ARQUIVO IMPORTADO: ", img.size)

# exibe tamanho e altura da imagem
print('width: ', width)
print('height: ', height)

# Q02. Monte um código Python que imprima os valores dos pixels das diferentes camadas (RGB).
img = Image.open('carla.jpg')
# dividir a imagem em bandas individuais
# red, green, blue = img.split()
# exibe as bandas red, green, blue, separadas da imagem original
# red.show()
# green.show()
# blue.show()

'''
#outra formar de dividir
im1 = Image.Image.split(img)

#mostrando cada banda
im1[0].show()
im1[1].show()
im1[2].show()
'''

#Uma tupla de 12 valores que é uma matriz de transformação para descartar
#channels red, green e blue (neste caso)
matrix_red = ( 1, 1, 1, 1,
           0, 0, 0, 0,
           0, 0, 0, 0)

matrix_green = ( 0, 0, 0, 0,
           1, 1, 1, 1,
           0, 0, 0, 0)

matrix_blue = ( 0, 0, 0, 0,
           0, 0, 0, 0,
           1, 1, 1, 1)

#Transforma a imagem em RGB usando a matriz mencionada
rgb_img = PIL.Image.open('carla.jpg')

rgb = rgb_img.convert("RGB")
red = img.convert("RGB", matrix_red)
green = img.convert("RGB", matrix_green)
blue = img.convert("RGB", matrix_blue)
'''
# Exibe as imagens em vermelho, azul, verde
red.show()
green.show()
blue.show()
'''

# pega os valores e imprimi os valores de todos pixels em seus respectivos canais
pixels_red = list(red.getdata())
pixels_green = list(green.getdata())
pixels_blue = list(blue.getdata())
pixels_rgb = list(rgb.getdata())

print("\n----------------------------------------------------------------------------CAMADA RED----------------------------------------------------------------------------")
for r in pixels_red:
   print(r)
print("----------------------------------------------------------------------------CAMADA RED----------------------------------------------------------------------------")

print("\n----------------------------------------------------------------------------CAMADA GREEN----------------------------------------------------------------------------")
for g in pixels_green:
    print(g)
print("----------------------------------------------------------------------------CAMADA GREEN----------------------------------------------------------------------------")

print("\n----------------------------------------------------------------------------CAMADA BLUE----------------------------------------------------------------------------")
for b in pixels_blue:
    print(b)
print("----------------------------------------------------------------------------CAMADA BLUE----------------------------------------------------------------------------")

print("\n----------------------------------------------------------------------------RGB----------------------------------------------------------------------------")
for rgb in pixels_rgb:
   print(rgb)
print("----------------------------------------------------------------------------RGB----------------------------------------------------------------------------")

# Q03. Apresente essa imagem utilizando o Matplotlib

# Apresentando imagens com Matplotlib
imagem = mpimg.imread('carla.jpg')
plt.imshow(imagem)
plt.show()

plt.imshow(red)
plt.show()

plt.imshow(green)
plt.show()

plt.imshow(blue)
plt.show()

''' 
Q04.Escolha um arquivo de video e salve todos os seus frames como imagens em um diretório 
-Filtro de bordas (a sua escolha)
-Salvar em tons de cinza
-Salvar em cada uma das cores

Q05.Implemente a o job da Q04 aplicando (cada uma em um diretório diferente): 

R
G
B
'''

print("\n----------------------------------------------------------------------------INICIO FRAME ARQUIVO_VIDEO----------------------------------------------------------------------------")

# leitura do arquivo de vídeo, ele fica no mesmo local que código está salvo na máquina
arquivo_video = cv2.VideoCapture('libras.mp4')
count = 0

# loop para ler o arquivo de vídeo
while True:
    # faz a leitura do frame, ou seja, pega cada frame do vídeo
    ret, frame = arquivo_video.read()

    # Aplica os respectivos filtros
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_edges = cv2.Canny(frame, 20, 30)
    gaussianBlur = cv2.GaussianBlur(frame, (5, 5), 0)

    #exibe a forma do frame
    print(frame.shape)

    # extrai os canais red, green, blue
    red_channel = frame[:, :, 2]
    green_channel = frame[:, :, 1]
    blue_channel = frame[:, :, 0]

    # cria uma imagem vazia com a mesma forma do frame
    red_video = np.zeros(frame.shape)
    green_video = np.zeros(frame.shape)
    blue_video = np.zeros(frame.shape)

    # atribui os canais red, green, blue ao do frame da imagem vazia
    red_video[:, :, 2] = green_channel
    green_video[:, :, 1] = green_channel
    blue_video[:, :, 0] = blue_channel

    # salva varios frames de um video
    cv2.imwrite('C:/code/prova2b/rgb/rgb_{}.jpg'.format(count), frame)
    cv2.imwrite('C:/code/prova2b/gray/rgb_{}.jpg'.format(count), gray)
    cv2.imwrite('C:/code/prova2b/gray_edges/rgb_{}.jpg'.format(count), gray_edges)
    cv2.imwrite('C:/code/prova2b/gaussianBlur/rgb_{}.jpg'.format(count), gaussianBlur)

    cv2.imwrite('C:/code/prova2b/red/red_{}.jpg'.format(count), red_video)
    cv2.imwrite('C:/code/prova2b/green/green_{}.jpg'.format(count), green_video)
    cv2.imwrite('C:/code/prova2b/blue/blue_{}.jpg'.format(count), blue_video)

    count += 1

    # salva um unico frame de um video
    # cv2.imwrite('C:/code/rgb/rgb.jpg', frame)

    # aperta a tecla Q para sair
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

    # exibe o frame do vídeo pessoas
    cv2.imshow("Video", frame)

print("\n----------------------------------------------------------------------------FIM FRAME ARQUIVO_VIDEO----------------------------------------------------------------------------")

# libera os recursos, no caso o arquivo_video
arquivo_video.release()

# fecha todas as janelas
cv2.destroyAllWindows()

# exibe tamanho/dimensoes da imagem
print("\nDADOS DO ARQUIVO IMPORTADO: ", img.size)
print('width: ', width)
print('height: ', height)