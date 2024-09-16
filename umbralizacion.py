from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def escala_grises(array):
    gray_values = 0.299 * array[:, :, 0] + 0.587 * array[:, :, 1] + 0.114 * array[:, :, 2]
    gray_img = gray_values.astype(np.uint8)
    return gray_img

def umbralizacion_global(img_gris, valorT_list):
    resultados = {}
    
    # se calcula T0 con la media
    T0 = np.mean(img_gris)
    
    for valorT in valorT_list:
        T = T0
        dif = np.inf
        
        while dif > valorT:  # división de píxeles de acuerdo al umbral
            grupo1 = img_gris[img_gris <= T]
            grupo2 = img_gris[img_gris > T]
            
            mean1 = np.mean(grupo1) if len(grupo1) > 0 else 0
            mean2 = np.mean(grupo2) if len(grupo2) > 0 else 0
            
            T_new = (mean1 + mean2) / 2  # umbral nuevo con promedio de los dos grupos
            
            dif = abs(T_new - T)
            T = T_new
        
        umbralizada = np.where(img_gris > T, 255, 0).astype(np.uint8)
        resultados[valorT] = umbralizada
    
    return resultados

imagenes = [
    'C:/Users/Anna Beristain/Downloads/practicaV/Umbralizaci-n-global/leopardo.jpg', 
    'C:/Users/Anna Beristain/Downloads/practicaV/Umbralizaci-n-global/flor.jpg', 
    'C:/Users/Anna Beristain/Downloads/practicaV/Umbralizaci-n-global/perro.jpg'
]

imgs_grises = [escala_grises(np.array(Image.open(img))) for img in imagenes]

valorT_list = [0, 0.05, 0.1]

for idx, img_gris in enumerate(imgs_grises):
    umbralizadas = umbralizacion_global(img_gris, valorT_list)
    
    plt.figure(figsize=(15, 10))

    plt.subplot(2, 3, 1)  
    plt.imshow(img_gris, cmap='gray')
    plt.title(f'Imagen en escala de grises {idx+1}')
    plt.axis('off')

    plt.subplot(2, 3, 2)
    plt.hist(img_gris.ravel(), 256, [0, 256])
    plt.title(f'Histograma {idx+1}')
    plt.xlabel('Intensidad de píxel')
    plt.ylabel('Frecuencia')

    for i, valorT in enumerate(valorT_list, start=1):
        plt.subplot(2, 3, i + 3) 
        plt.imshow(umbralizadas[valorT], cmap='gray')
        plt.title(f'Umbralización {idx+1} (ΔT = {valorT})')
        plt.axis('off')

    plt.tight_layout()
    plt.show()

