El algoritmo de Canny es un popular método de detección de bordes en imágenes, y se compone principalmente de tres pasos: obtención del gradiente, supresión no máxima y histéresis de umbral [Recurso 2](https://www.slideshare.net/c09271/deteccinde-bordes-canny).

1. **Obtención del gradiente**: En este paso, se calcula la magnitud y la orientación del vector gradiente en cada píxel de la imagen. Primero, se aplica un filtro gaussiano para suavizar la imagen y eliminar el ruido [Recurso 2](https://www.slideshare.net/c09271/deteccinde-bordes-canny). Luego, para cada píxel, se obtiene la magnitud y la orientación del gradiente utilizando las derivadas parciales en las direcciones x e y [Recurso 2](https://www.slideshare.net/c09271/deteccinde-bordes-canny). 

```python
Gx = np.gradient(image, axis=1)  # Gradiente en dirección x
Gy = np.gradient(image, axis=0)  # Gradiente en dirección y
magnitud_gradiente = np.sqrt(Gx**2 + Gy**2)
orientacion_gradiente = np.arctan2(Gy, Gx)
```

2. **Supresión no máxima**: Este paso tiene como objetivo adelgazar los bordes obtenidos en el paso anterior hasta lograr bordes de un píxel de ancho. Se consideran cuatro direcciones (0º, 45º, 90º y 135º) y se verifica si el valor de la magnitud del gradiente en un píxel es más grande que al menos uno de sus dos vecinos en la dirección del ángulo obtenido en el paso anterior [Recurso 2](https://www.slideshare.net/c09271/deteccinde-bordes-canny). Si es menor, se asigna el valor 0 a dicho píxel; en caso contrario, se asigna el valor que tenga la magnitud del gradiente.

3. **Histéresis de umbral**: La imagen obtenida en el paso anterior puede contener máximos locales creados por el ruido. Para eliminar dicho ruido, se aplica una función de histéresis basada en dos umbrales (alto y bajo) [Recurso 2](https://www.slideshare.net/c09271/deteccinde-bordes-canny). Para cada punto de la imagen, se localiza el siguiente punto de borde no explorado que sea mayor al umbral alto, y a partir de dicho punto, se siguen las cadenas de máximos locales. Un método robusto para determinar el valor de doble umbral es utilizar el método de Otsu en la imagen de magnitud de gradiente suprimido no máximo para generar el umbral alto, y establecer el umbral bajo como la mitad del umbral alto [Recurso 1](https://hmong.es/wiki/Canny_edge_detector).

Además, se han utilizado curvas (curvelets) en lugar del filtro gaussiano y la estimación del gradiente para calcular un campo vectorial cuyas direcciones y magnitudes se aproximan a la dirección y la fuerza de los bordes en la imagen, a los que luego se aplican los pasos 3 a 5 del algoritmo de Canny [Recurso 1](https://hmong.es/wiki/Canny_edge_detector). Los curvelets descomponen las señales en componentes separados de diferentes escalas, y la eliminación de los componentes de escalas más finas puede reducir el ruido.

## Artículo analizado
El artículo de Programar Facil llamado Detector de bordes Canny cómo contar objetos con OpenCV y Python se centra en el detector de bordes Canny utilizando OpenCV en el contexto de la visión artificial. El autor explica cómo implementar el algoritmo Canny en Python utilizando la biblioteca OpenCV. A lo largo del artículo, se describen los detalles técnicos del algoritmo, cómo se aplica en la visión artificial y cómo implementarlo en código. Además, se proporcionan ejemplos de código y resultados visuales para ilustrar el funcionamiento del algoritmo en diferentes situaciones.

## Referencia del articulo
[Programar Facil](https://programarfacil.com/blog/vision-artificial/detector-de-bordes-canny-opencv/)