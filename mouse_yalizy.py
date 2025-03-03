import pyautogui
import time
from datetime import datetime

# Configuración del intervalo de movimiento
intervalo = 120  # Intervalo en segundos entre movimientos del mouse

while True:
    try:
        # Obtener la fecha y hora actual®
        ahora = datetime.now()

        # Obtiene la posición actual del mouse
        x, y = pyautogui.position()

        # Mueve el mouse un pequeño valor en la dirección x
        pyautogui.moveTo(x + 5, y + 5, duration=0.1)

        # Mueve el mouse de vuelta a la posición original
        pyautogui.moveTo(x, y, duration=0.1)

        print('Hice un movimiento de mouse ahora: ', ahora.strftime("%Y-%m-%d %H:%M:%S"))

        # Espera el intervalo antes de hacer el siguiente movimiento
        time.sleep(intervalo)

    except Exception as e:
        print(f"Ocurrió un error: {e}. Intentando nuevamente...")
        time.sleep(5)  # Espera 5 segundos antes de intentar nuevamente
