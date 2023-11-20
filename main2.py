import cv2

# Cargar la imagen
image = cv2.imread("imagen.jpg")

# Convertir a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar umbralización para obtener una imagen binaria
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Encontrar los contornos de la imagen binaria
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Contar el número de contornos que parecen una X
count = 0
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    if len(approx) == 4:
        x, y, w, h = cv2.boundingRect(contour)
        if w/h > 0.8 and w/h < 1.2:
            count += 1

# Imprimir el resultado
print("Cantidad de equis escritas con lápiz:", count)