from email.mime.text import MIMEText
import smtplib


# Create your tests here.


def send_email():
    try:
        mailServer = smtplib.SMTP('smtp.gmail.com', 587)
        print(mailServer.ehlo())
        mailServer.starttls()
        print(mailServer.ehlo())
        mailServer.login("minuevomejoramigoguate@gmail.com", "Proyectos201801376")
        print('conectado....')

        #Construimos mensaje simple
        mensaje = MIMEText("""Quieres restablecer tu contraseña? Victor Gay""")
        mensaje['From'] = "minuevomejoramigoguate@gmail.com"
        mensaje['To'] = "javiabarrios@gmail.com"
        mensaje['Subject'] = "Restablecimiento de contraseña"
        
        mailServer.sendmail("minuevomejoramigoguate@gmail.com",
                            "javiabarrios@gmail.com", 
                            mensaje.as_string())

        print('Correo enviado con exito')
    except Exception as e:
        print(e)

send_email()