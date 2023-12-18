import smtplib
from os.path import basename # ф-я получения базового пути из имени файла
from email.mime.multipart import MIMEMultipart # Класс для созд-я почт сообщения с неск частями
from email.mime.text import MIMEText # Класс для сод-я текст части сообщения
from email.mime.application import MIMEApplication # Класс для вложения файла


def send_email():
    from_address = "zareff07@mail.ru"
    to_address = "zareff@yandex.ru"
    my_password = "wTHymWkk5S25ptLbrtt9"
    report_name = "log.txt"

    message = MIMEMultipart()
    message['From'] = from_address
    message['To'] = to_address
    message['Subject'] = "Test Report"

    with open(report_name, "rb") as f:
        part = MIMEApplication(f.read(), Name=basename(report_name))
        part['Content-Disposition'] = 'attachment; filename = "%s"' % basename(report_name)
        message.attach(part)

    body = "Пробный тест"
    message.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    server.login(from_address, my_password)
    text = message.as_string()
    server.sendmail(from_address, to_address, text)
    server.quit()


if __name__ == '__main__':
    send_email()