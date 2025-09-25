import os
import json
import logging
from time import sleep
from kivy.app import App
from android.permissions import request_permissions, Permission

# 1. Configuración del logger
logging.basicConfig(level=logging.INFO)
output_file = "/sdcard/Download/permisos_log.txt"

# 2. Lista de permisos que vamos a solicitar
permissions_to_request = [
    Permission.CAMERA,
    Permission.RECORD_AUDIO,
    Permission.READ_EXTERNAL_STORAGE,
    Permission.WRITE_EXTERNAL_STORAGE,
]

class PermissionApp(App):
    def build(self):
        # 3. Solicitar permisos al inicio
        def callback_permissions(permissions, results):
            log = f"Permisos solicitados: {permissions}\nResultados: {results}\n"

            # Intentamos escribir el log en el archivo
            try:
                with open(output_file, 'a') as f:
                    f.write(log)
                logging.info(f"Log escrito en: {output_file}")
            except Exception as e:
                logging.error(f"Error al escribir el log en {output_file}: {e}")

            # Cerramos la aplicación después de solicitar (o fallar) los permisos
            App.get_running_app().stop()

        # La función de Kivy para solicitar
        request_permissions(permissions_to_request, callback_permissions)

        # Kivy necesita un widget
        from kivy.uix.label import Label
        return Label(text='Solicitando permisos...')

if __name__ == '__main__':
    PermissionApp().run()
