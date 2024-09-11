from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def escala_grises(array):
    gray_values = 0.299 * array[:, :, 0] + 0.587 * array[:, :, 1] + 0.114 * array[:, :, 2]
    gray_img = gray_values.astype(np.uint8)
    return gray_img


#leer imagen
img=np.array(Image.open('leopardo.jpg'))

img_gris = escala_grises(img)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img_gris, cmap='gray')
plt.title('Imagen en escala de grises')
plt.axis('off')


plt.subplot(1, 2, 2)
plt.hist(img_gris.ravel(), 256, [0, 256])
plt.title('Histograma')
plt.xlabel('Intensidad de píxel')
plt.ylabel('Frecuencia')

plt.tight_layout()
plt.show()