import os
import smtplib


def send_mail(mail_sub='', mail_body='', sender='', receivers=[], mail_server='192.168.0.10'):
    # we need the receivers.
    if not receivers:
        return 'No receivers found, aborting mailing process.'
    # if no senders specified then take the local user as the sender.
    if not sender:
        user_name = os.environ['USERNAME']
        sender = '%s@pcgi.com' % user_name
    if not mail_sub or not mail_body:
        return 'No Subject or the mail body provided, aborting mailing process.'

    message = 'From: %s\nTo: %s\nSubject: %s\n%s.' % (sender, receivers[0], mail_sub, mail_body)

    try:
        smtp_obj = smtplib.SMTP(mail_server)
        smtp_obj.sendmail(sender, receivers, message)
        smtp_obj.quit()
        print "Successfully sent email"
    except smtplib.SMTPException:
        print "Error: unable to send email"


if __name__ == '__main__':
    body1 = 'Hi BalaSir,\n\t'
    body2 = 'We are working on a script which will send automated mail to the artists. Kindly please provide us with ' \
            'an e-mail for this purpose. The ID should be something like "noreply@pcgi.com" ' \
            'so we can use the same ID for various mails.'
    body3 = '\nThanks.\nDurgesh'
    body = body1 + body2 + body3
    subject = 'Mail ID for automated mailing system'
    # print send_mail(mail_sub=subject, mail_body=body, receivers=['support@pcgi.com', 'bala.k@pcgi.com', 'rnd@pcgi.com'], sender='durgesh.n@pcgi.com')
    # print send_mail(mail_sub=subject, mail_body=body, receivers=['durgesh.n@pcgi.com'], sender='durgesh.n@pcgi.com')
