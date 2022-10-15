# import smtplib
# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()
# server.login('cryptobot0011@gmail.com', 'CryptoCrypto')
# server.sendemail('cryptobot0011@gmail.com', 'hj.desirena@gmail.com', 'Mail test')
# print('Mail sent')

import email
import os
from email.message import EmailMessage
import ssl
import smtplib


def contex(email_sender, email_password, email_receiver, subjet, body):
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['subject'] = subjet
    em.set_content(body)
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())


def send_email(position):
    email_sender = 'cryptobot0011@gmail.com'
    email_password = 'xlimpsptmqzanqmj'
    email_receiver1 = 'hj.desirena@gmail.com'
    # subjet ='Email test'cryptobot0011@gmail.com
    '''body = """
            Sending email test
            """
    '''
    if position == 'BUY':
        subjet = 'Bot - Buy'
        body = """
                        BUYING...
                        """
    elif position == 'SELL':
        subjet = 'BOT - SELL'
        body = """
                        BOT IS SELLING...
                        """
    elif position == 'NEUTRAL':
        subjet = 'BOT - NEUTRAL'
        body = """
                        NEUTRAL...
                        """

    contex(email_sender, email_password, email_receiver1, subjet, body)
    #contex(email_sender, email_password, email_receiver2, subjet, body)


send_email('SELL')