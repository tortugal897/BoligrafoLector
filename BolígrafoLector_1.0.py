from picamera import PiCamera # Librería que controla la cámara
from time import sleep # Librería que permite programar con los tiempos con facilidad
import pytesseract #Librería que inicia el OCR
import cv2 #Librería que permite la alteración de las imágenes
from PIL import Image # Librería que nos permite leer imágenes de forma fácil
# import vlc # Librería que permite la reproduccion de archivos de sonido desde Python
import RPi.GPIO as GPIO # Librería que sirve para controlar el botón
import os # Consola de la Raspberry (para usar comandos de la consola desde este código)

def variación_contraste_adaptativo(file_path): # Función que modifica la imagen variando el contraste
    img = cv2.imread(file_path, 0) # Carga la imagen en gris
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8)) # Crea el contraste adaptativo dividido en secciones
    cl1 = clahe.apply(img) # Aplica el contraste
    return cl1

os.system('sudo alsactl restore') # Restauro la configuración de ALSAMixer
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN) # Inicializo el botón (es 17 porque usa el puerto GPIO17)

while(1): # Inicio un bucle para evitar que importe las librerías de nuevo
    #inicia el programa
    os.system('cvlc --play-and-exit /home/pi/Desktop/TFG/beep-02.wav')
    camera = PiCamera() # Iniciamos el proceso de la cámara de la raspberry
#    camera.start_preview(alpha=200) # Mostramos la imagen que vamos a capturar (debug)
    camera.rotation=90 # Cambiamos la posición de la imagen 90º

    i=0 
    while(i == 0):    
        boton = GPIO.input(17) # Lee el botón y espera a la señal
        if boton:
            sleep(0.001)
            continue
        else:
#            print ('haciendo foto') # (debug)
            sleep(2) # Doy 2 segundos para que la cámara pueda ajustarse si es necesario
            camera.capture('/home/pi/Desktop/TFG/ImagenesProyecto/image1.jpg') # Hago captura
            i=1 # Salgo del bucle while
        
    camera.stop_preview() # Detengo la visión de la imagen de captura (debug)
    camera.close()

    Direccion_archivo = '/home/pi/Desktop/TFG/ImagenesProyecto/image1.jpg'

    img = variación_contraste_adaptativo(Direccion_archivo) # Llamo a la función de variación de contraste

    original=pytesseract.image_to_string(img,config='-l spa --oem 3 --psm 1') # Inicio el OCR
#    print (original) # Muestro el resultado del OCR por la consola (debug)

    os.system('pico2wave -l es-ES -w grabacion.wav "%s"' %original)

    os.system('cvlc --play-and-exit /home/pi/grabacion.wav')
#     audio = vlc.MediaPlayer('/home/pi/Desktop/TFG/grabacion.wav') # Creo un objeto para reproducir con el VLC media player
#     audio.audio_set_volume(80) #Reduce el volumen, pero no sé por qué no funciona
#     audio.play() # Reproduzco el resultado
#     sleep(1.5) # Espero un poco de tiempo para que inicie la grabación sin problemas
#     duration = audio.get_length() / 1000 # Establezco una duración del audio a reproducir
#     sleep(duration) # Hago que el código se detenga hasta que la reproducción se complete
#     # Se está produciendo clipping en el audio y no entiendo por qué
