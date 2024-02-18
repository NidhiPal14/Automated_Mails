import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders



smtp_port = 587
smtp_server = "smtp.gmail.com"

email_from = "palnidhi.projects@gmail.com"
email_list = ["nidhipal2121@gmail.com", "palnidhi.projects@gmail.com", "vickyaadhar12345@gmail.com"]

pswd = "kgqsswncpifjvqsk"

subject = "New Email with attachment!"


def send_emails(email_list):
    for person in email_list:

        body = f"""
        Cloud Computing
        Cryptography
        Blockchain
        Artificial Intelligence 
        Machine Learning
        etc
        """



        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['To'] = person
        msg['Subject'] = subject


        msg.attach(MIMEText(body, 'plain'))

        filename = "color_srgb.csv"


        attachment = open(filename, 'rb')


        attachment_package = MIMEBase('application', 'octet_stream')
        attachment_package.set_payload(attachment.read())
        encoders.encode_base64(attachment_package)
        attachment_package.add_header('Content-Disposition', "attachment; filename= " + filename)
        msg.attach(attachment_package)


        text = msg.as_string()


        print("Connecting to server...")
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls()
        TIE_server.login(email_from, pswd)
        print("Successfully connected to server")
        print()


        print(f"Sending email to: {person}...")
        TIE_server.sendmail(email_from, person, text)
        print(f"Email sent to: {person}")
        print()

    TIE_server.quit()


send_emails(email_list)