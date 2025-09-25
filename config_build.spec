[app]
# (str) Title of your application
title = Llave-Maestra

# (str) Package name (DEBE SER ÚNICO)
package.name = com.llave.maestra

# (str) Package domain
package.domain = org.llave

# (str) Version of your application
version = 1.0

# (list) Requirements: list of modules needed by your application
requirements = python3,kivy,android

# (str) Icon file to use as the application icon
icon.filename = %(source.dir)s/icon.png

# (str) Source code where the main application lives
source.dir = .

# (str) EL NOMBRE ÚNICO DEL ARCHIVO PRINCIPAL
main.py = %(source.dir)s/inicio_app.py

# (list) Android permissions (needed for Kivy)
android.permissions = CAMERA, RECORD_AUDIO, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# (int) Android SDK version to target
android.targetsdk = 33

# (int) Android NDK version
android.ndk = 25b

# (str) Full name for the APK
android.apk_name = Llave-Maestra-%(version)s-debug.apk

[buildozer]
# (list) Log levels
log_level = 2
