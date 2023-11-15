import cv2
import numpy as np

# Kamera girişi
cap = cv2.VideoCapture(0)

while True:
    # Görüntüyü oku
    ret, frame = cap.read()

    # Görüntüyü HSV formatına dönüştür
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Kırmızı renge karşılık gelen HSV aralığını belirle
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    # HSV aralığına göre bir maske oluştur
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Orijinal görüntü ve maske arasında bitwise AND uygula
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Sonucu göster
    cv2.imshow('Original', frame)
    cv2.imshow('Result', result)

    # Çıkış için 'q' tuşuna basın
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Pencereyi kapat
cap.release()
cv2.destroyAllWindows()