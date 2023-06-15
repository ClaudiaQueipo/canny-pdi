import cv2
import pydicom
import numpy as np

# Cargar la imagen DICOM
dicom_file = './0015.DCM'
dcm_data = pydicom.dcmread(dicom_file)
image = dcm_data.pixel_array

# Aplicar el algoritmo de Canny para detectar bordes
edges = cv2.Canny(image, 25, 50)

# Crear una imagen con los bordes resaltados
overlay = np.zeros_like(image)
overlay[edges > 0] = 255
result = cv2.addWeighted(image, 0.7, overlay, 0.3, 0)

# Mostrar las imágenes en una ventana de OpenCV
window_name = 'Imagen Original vs. Imagen Modificada'
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.imshow(window_name, np.hstack((image, result)))
cv2.waitKey(0)
cv2.destroyAllWindows()
