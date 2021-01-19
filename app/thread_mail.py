import threading
from threading import Thread
from django.core.mail import EmailMessage
from django.http import HttpResponse
from mailsend.settings import EMAIL_HOST_USER


def thread_mail(request):
    subject = 'Test mail'
    html_content = '<p>this is test mail send using thread </p>'
    recipient_list = list()
    for i in range(50):
        vendor = 'vendor' + str(i) + '@yopmail.com'
        recipient_list.append(vendor)
    send_thread_mail(subject, html_content, recipient_list)
    return HttpResponse('mail send successfull')


class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        threading.Thread.__init__(self)

    def run(self):
        msg = EmailMessage(self.subject, self.html_content, EMAIL_HOST_USER, self.recipient_list)
        msg.content_subtype = "html"
        msg.send()


def send_thread_mail(subject, html_content, recipient_list):
    EmailThread(subject, html_content, recipient_list).start()