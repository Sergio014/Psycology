from django.shortcuts import render
from .conf import *
from .models import *
import telebot

bot = telebot.TeleBot(TOKEN, parse_mode='HTML')
# Create your views here.
def index_view(request):
    if request.POST:
        username = request.POST['username']
        phone = request.POST['phone']
        question = request.POST['question']
        bot.send_message(917369738, f"""
        Нове повідомлення!
        Ім'я: {username}
        Номер телефону: {phone}
        Питання: {question}""")
        Message.objects.create(username=username, phone=phone, question=question)
    return render(request, 'index.html')

def aboutme_view(request):
    if request.POST:
        username = request.POST['username']
        phone = request.POST['phone']
        question = request.POST['question']
        bot.send_message(917369738, f"""
        Нове повідомлення!
        Ім'я: {username}
        Номер телефону: {phone}
        Питання: {question}""")
        Message.objects.create(username=username, phone=phone, question=question)
    return render(request, 'aboutme.html')

def group_view(request):
    if request.POST:
        username = request.POST['username']
        phone = request.POST['phone']
        question = request.POST['question']
        bot.send_message(917369738, f"""
        Нове повідомлення!
        Ім'я: {username}
        Номер телефону: {phone}
        Питання: {question}""")
        Message.objects.create(username=username, phone=phone, question=question)
    return render(request, 'group.html')

def how_view(request):
    if request.POST:
        username = request.POST['username']
        phone = request.POST['phone']
        question = request.POST['question']
        bot.send_message(917369738, f"""
        Нове повідомлення!
        Ім'я: {username}
        Номер телефону: {phone}
        Питання: {question}""")
        Message.objects.create(username=username, phone=phone, question=question)
    return render(request, 'how.html')

def individual_view(request):
    if request.POST:
        username = request.POST['username']
        phone = request.POST['phone']
        question = request.POST['question']
        bot.send_message(917369738, f"""
        Нове повідомлення!
        Ім'я: {username}
        Номер телефону: {phone}
        Питання: {question}""")
        Message.objects.create(username=username, phone=phone, question=question)
    return render(request, 'individual.html')