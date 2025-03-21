# Simular una función que envía un correo y usa un callback al terminar
def enviar_correo(mensaje, callback):
    print(f"Enviando correo: {mensaje}")
    # Llamar al callback cuando termine el envío
    callback()

def notificar_envio_exitoso():
    print("El correo fue enviado correctamente.")

# Llamar a la función con el callback
enviar_correo("Este es un mensaje importante", notificar_envio_exitoso)
