import smtplib, ssl
from email.message import EmailMessage


def smtp_connection(user_email, swimmer_name, class_selected, experience_selected):
  global sender_email, password
  smtp_server = "smtp.gmail.com"
  port = 587
  sender_email = "swimclass05@gmail.com"
  email = str(user_email)
  receiver_email = email
  message = f"Subject: Registration Confirmation\n\nHello! This is confirmation that you have registered {swimmer_name} for {class_selected} {experience_selected} class."
  password = "odth ztaa dofw upmv"
  #password = input("Enter password: ")

  context = ssl.create_default_context()
  with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)



def send_sms(swimmer_name, class_selected, experience_selected, user_phone):
  try:
    msg = EmailMessage()
    msg.set_content("Hello! This is confirmation that you have registered " + swimmer_name +  " for " + class_selected + " " + experience_selected + " class.")
    print(user_phone)
    phone = str(user_phone)
    print(phone)
    gatewayAddress = phone + "@vtext.com"
    print(gatewayAddress)

    msg['From'] = sender_email 
    msg['To'] = gatewayAddress

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.send_message(msg)

    server.quit()
  except Exception as e:
    print("SMS not sent properly")