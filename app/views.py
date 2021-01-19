import json
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import (response, HttpResponse, JsonResponse, request)
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.template.loader import render_to_string
from django.views.generic import (View, ListView, CreateView, UpdateView, DeleteView, DetailView)
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, auth
from django.contrib.auth.views import *
from .thread_mail import send_thread_mail


def send_mail(request):
    if request.method == "POST":
        subject = request.POST.get('subject')
        msg = request.POST.get('msg')
        recipient_list = list(request.POST.get('email').split(";"))
        print(recipient_list,'recipient_list')
        # recipient_list = ['ajit@yopmail.com']
        email_template = 'email.html'
        name = "Admin"
        # msg = 'विश्व बदले वेबजाल कम्प्युटर अर्थपुर्ण प्रति जिम्मे अनुकूल पत्रिका एवम् प्राण गुजरना वर्णित सोफ़्टवेर जाने बाधा मजबुत पुस्तक निर्माण गोपनीयता ध्येय रिती क्षमता ब्रौशर अत्यंत सारांश शारिरिक नीचे होसके समजते दिये लक्ष्य तकरीबन केन्द्रित भाषाओ लिए। हुआआदी आवश्यकत उनका अनुवाद व्याख्यान तरीके अधिक व्याख्यान अमितकुमार विकासक्षमता बनाने'
        html_content = render_to_string(email_template,
                                          {'name': name,
                                           'message': msg,
                                           })

        send_thread_mail(subject, html_content, recipient_list)
        return redirect('mail_send')
    else:
        pass

    return render(request, 'form.html', {})