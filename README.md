# Mouse
# Mouse Move 
>># Movimiento Automático del Mouse
Este es un programa simple en Python que mueve el mouse automáticamente cada cierto intervalo de tiempo para evitar que la computadora entre en modo de suspensión o para mantenerla activa. Es útil en situaciones donde necesitas que tu computadora permanezca despierta, como durante presentaciones, descargas largas, mantener activo un estado en Microsoft Teams o cualquier tarea que requiera que la pantalla no se bloquee.

> ## Requisitos
#### Instalaciones:
* Python 3.x instalado.

* Librerías 
* pyautogui
* time instaladas.
----


> ## Instalación
> 
#### Pasos a seguir:
1. Clona este repositorio o descarga el archivo `.py`.
2. Asegúrate de tener Python instalado en tu sistema.
3. Instala las dependencias necesarias ejecutando el siguiente comando en tu terminal:
```bash
  pip install pyautogui
```
----


> ## Uso:
#### Pasos a seguir:
1. Ejecuta el script en tu terminal, ejecuta en python
```sh bash
  mouse_yalizy.py
```

2. El programa comenzará a mover el mouse cada 120 segundos (2 minutos) por defecto. Puedes ajustar el `intervalo` cambiando el valor de la variable intervalo en el código.

3. El programa imprimirá en la consola la fecha y hora cada vez que haga un movimiento del mouse.

4. Para detener el programa, presiona `Ctrl + C` en la terminal.
----


> ##  Configuración

* **Intervalo de movimiento:** Puedes cambiar el intervalo de tiempo entre movimientos modificando la variable intervalo en el código. El valor está en segundos.
```bash
  intervalo = 120  # Cambia este valor para ajustar el intervalo
```
* **Duración del movimiento:** La duración del movimiento del mouse se puede ajustar cambiando el parámetro duration en las funciones pyautogui.moveTo().

  ```bash
    pyautogui.moveTo(x + 5, y + 5, duration=0.1)  # Ajusta la duración del movimiento
  ```
----



> ##  Manejo de Errores


El programa incluye un manejo básico de errores. Si ocurre algún error durante la ejecución, el programa imprimirá un mensaje de error y volverá a intentar el movimiento después de 5 segundos.

```bash
  except Exception as e:
    print(f"Ocurrió un error: {e}. Intentando nuevamente...")
    time.sleep(5)  # Espera 5 segundos antes de intentar nuevamente
```
----


> ##  Contribuciones
Si deseas contribuir a este proyecto, siéntete libre de hacer un fork y enviar un pull request con tus mejoras.

