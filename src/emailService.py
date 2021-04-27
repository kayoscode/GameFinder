import smtplib, ssl

def sendEmail(senderUser, senderPass, receiverEmail, emailContent):
    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls(context = context)
        server.ehlo()
        server.login(senderUser, senderPass)
        server.sendmail(senderUser, receiverEmail, emailContent)
    except Exception as e:
        print("Error creating email session", e)
    finally:
        server.quit()