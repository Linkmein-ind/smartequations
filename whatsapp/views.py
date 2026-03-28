import json
import requests

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from .models import ChatUser, Message


# ======================================
# SEND WHATSAPP MESSAGE
# ======================================

def send_whatsapp(phone, text):

    phone = phone.replace("+", "").replace(" ", "")

    url = f"https://graph.facebook.com/v18.0/{settings.WHATSAPP_PHONE_ID}/messages"

    headers = {
        "Authorization": f"Bearer {settings.WHATSAPP_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": phone,
        "type": "text",
        "text": {"body": text}
    }

    res = requests.post(url, headers=headers, json=payload)

    print("WhatsApp response:", res.text)


# ======================================
# WEBHOOK (CRITICAL)
# ======================================

@csrf_exempt
def whatsapp_webhook(request):

    print("🔥 WEBHOOK HIT:", request.method)

    # ---------- VERIFY ----------
    if request.method == "GET":

        mode = request.GET.get("hub.mode")
        token = request.GET.get("hub.verify_token")
        challenge = request.GET.get("hub.challenge")

        if mode == "subscribe" and token == settings.VERIFY_TOKEN:
            return HttpResponse(challenge)

        return HttpResponse("error", status=403)


    # ---------- RECEIVE MESSAGE ----------
    if request.method == "POST":

        try:
            data = json.loads(request.body)
            print("DATA:", data)

            msg = data['entry'][0]['changes'][0]['value']['messages'][0]

            phone = msg['from']
            text = msg['text']['body']

            user, _ = ChatUser.objects.get_or_create(phone=phone)

            Message.objects.create(
                user=user,
                message=text,
                direction="incoming"
            )

            # optional auto reply
            send_whatsapp(phone, "Hi 👋 We received your message!")

        except Exception as e:
            print("Webhook error:", e)

        return HttpResponse("EVENT_RECEIVED")


# ======================================
# DASHBOARD
# ======================================

def chat_dashboard(request):

    users = ChatUser.objects.all().order_by('-id')

    selected = None
    chats = []

    uid = request.GET.get("user")

    if uid:
        selected = ChatUser.objects.get(id=uid)
        chats = Message.objects.filter(user=selected).order_by("created_at")

    return render(request, "whatsapp/chat.html", {
        "users": users,
        "selected": selected,
        "messages": chats
    })


# ======================================
# SEND FROM ADMIN
# ======================================

def send_message(request, user_id):

    if request.method == "POST":

        text = request.POST.get("message")
        user = ChatUser.objects.get(id=user_id)

        send_whatsapp(user.phone, text)

        Message.objects.create(
            user=user,
            message=text,
            direction="outgoing"
        )

    return redirect(f"/whatsapp/chat/?user={user_id}")