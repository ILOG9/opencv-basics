import cv2

# imagen = cv2.imread("auto.jpg",cv2.IMREAD_COLOR)
imagen = cv2.imread("auto.jpg",cv2.IMREAD_GRAYSCALE)
# imagen = cv2.imread("auto.jpg",cv2.IMREAD_UNCHANGED)

# Cambia el tamaño de la ventana por otro
cv2.namedWindow("Windows Title",cv2.WINDOW_NORMAL)

#muestra una ventana con el titulo en primer parametro y la imagen indicada en segundo parametro
cv2.imshow("Windows Title",imagen)

#espera a que una tecla sea pulsada 
cv2.waitKey(0) & 0xFF

# crea una nueva imagen a partir de la variable en segundo parametro
cv2.imwrite("nuevaimagen.jpg",imagen)

#destruye las ventanas
cv2.destroyAllWindows()