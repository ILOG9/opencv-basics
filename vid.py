import cv2

# captura video de un fichero
captura = cv2.VideoCapture("1.mp4")

# captura video de la webcam
# captura = cv2.VideoCapture(0)
#sirve para manipular while
captura.open("1.mp4")

#ALto y ancho de la vista
captura.set(3,1000)
captura.set(4,600)

while captura.isOpened():
	#capturando video fotograma por fotograma
	ret,frame = captura.read()
	# gris = cv2.cvtColor(frame,cv2.COLORMAP_SUMMER) <- cambia el filtro de video por uno gris
	cv2.rectangle(frame, (100, 100), (10+100, 100+100), (255, 0, 200), 2)
	print (captura.read())
	cv2.imshow("! video ¡", frame)
	# cv2.imshow("! video ¡", gris) <- muestra una pantalla con la frame antes definida en gris
	#con waitkey podemos ajustar la cantidad de fotogramas por segundo
	if (cv2.waitKey(1) & 0xFF) == ord("q"):
		break
cap.release()

# cv2.imwrite("nuevaimagen.jpg",imagen)