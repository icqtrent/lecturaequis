import cv2

# Cargar la imagen
image = cv2.imread("imagen2.jpg")

# Convertir a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar umbralización adaptativa para obtener una imagen binaria
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

# Encontrar los contornos de la imagen binaria
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Contar el número de contornos que parecen una X
count = 0
coord_x = []
coord_y = []
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    if len(approx) == 1:
        x, y, w, h = cv2.boundingRect(contour)
        if w/h > 0.8 and w/h < 1.2:
            count += 1/50
            conteo=round(count,0)
            # Selecciona la coordenada central de la equis
            coord_x.append((x + w) / 2)
            coord_y.append((y + h) / 2)

# Imprimir el resultado
print("Cantidad de equis escritas con lápiz:", conteo)
print("Coordenadas de las equis:", coord_x, coord_y)


