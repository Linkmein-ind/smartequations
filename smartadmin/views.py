from django.shortcuts import render

# Create your views here.
from functools import wraps
from django.shortcuts import redirect

def admin_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.session.get("is_admin"):
            return redirect("admin_login")
        return view_func(request, *args, **kwargs)
    return wrapper


from django.conf import settings
from django.contrib import messages

def admin_login(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if (username == settings.DEFAULT_ADMIN_USERNAME and
            password == settings.DEFAULT_ADMIN_PASSWORD):

            request.session["is_admin"] = True
            return redirect("admin_dashboard")

        messages.error(request, "Invalid credentials")

    return render(request, "smartadmin/login.html")


def admin_logout(request):
    request.session.flush()
    return redirect("admin_login")

from smartequ.models import RequestCall

@admin_required
def admin_dashboard(request):

    total_calls = RequestCall.objects.count()
    pending_calls = RequestCall.objects.filter(contacted=False).count()

   

    return render(request, "smartadmin/dashboard.html", {
        "total_calls": total_calls,
        "pending_calls": pending_calls,
    })


@admin_required
def callback_list(request):

    calls = RequestCall.objects.all().order_by("-created_at")

    return render(request, "smartadmin/callback_list.html", {
        "calls": calls
    })


@admin_required
def mark_contacted(request, id):
    call = RequestCall.objects.get(id=id)
    call.contacted = True
    call.save()
    return redirect("callback_list")