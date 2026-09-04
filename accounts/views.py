from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib.auth.decorators import login_required
from .models import*
import math
User=get_user_model()

# Create your views here.
def home(request):
	return render(request, "accounts/home.html")
  
def dashboard(request):
	return render(request, "accounts/dashboard.html")

def signup_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")

        if not username or not email or not password or not confirm_password:
            messages.error(request, "All fields are required.")
            return redirect("signup")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("signup")

        if len(password) < 8:
            messages.error(request, "Password must be at least 8 characters.")
            return redirect("signup")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("signup")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect("signup")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, user)
        messages.success(request, "Account created successfully.")
        return redirect("home")

    return render(request, "accounts/signup.html")

def login_view(request):
    def login_view(request):
     if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        if not username or not password:
            messages.error(request, "Username and password are required.")
            return redirect("login")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully.")

            next_url = request.GET.get("next")
            return redirect(next_url or "home")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("login")

    return render(request, "accounts/login.html")

@login_required
def logout_view(request):
     logout(request)
     messages.success(request, "Logged out successfully.")
     return redirect("login") 

     return render(request,"accounts/logout.html")

def about_view(request):
    return render(request,"accounts/about.html")

def contact_view(request):
    return render(request,"accounts/contactus.html")

def privacy_view(request):
    return render(request,"accounts/privacy.html")

def terms_view(request):
    return render(request,"accounts/terms.html")

def cookie_view(request):
    return render(request,"accounts/cookie.html")

def copy_view(request):
    return render(request,"accounts/copy.html")

def help_view(request):
    return render(request,"accounts/help.html")

def report_view(request):
    return render(request,"accounts/report.html")

def features_view(request):
    return render(request,"accounts/features.html")

def error_view(request):
    return render(request,"accounts/404.html")

def pricing_view(request):
    return render(request,"accounts/pricing.html")

def reviews_view(request):
    return render(request,"accounts/reviews.html")
    
def accessibility_view(request):
    return render(request,"accounts/accessibility.html")

def gallery_view(request):
    return render(request,"accounts/gallery.html")

def careers_view(request):
    return render(request,"accounts/careers.html")

def creators_view(request):
    return render(request,"accounts/creators.html")

def ad_center_view(request):
    return render(request,"accounts/adcenter.html")

def support_view(request):
    return render(request,"accounts/support.html")  

def press_view(request):
    return render(request,"accounts/press.html")        

def developers_view(request):
    return render(request,"accounts/developers.html")

def documentation_view(request):
    return render(request,"accounts/documentation.html")   

def sitemap_view(request):
    return render(request,"accounts/sitemap.html") 

def feedback_view(request):
    return render(request,"accounts/feedback.html")

def event_view(request):
    return render(request,"accounts/events.html")

def community_view(request):
    return render(request, "accounts/community.html")

def disclaimer_view(request):
    return render(request, "accounts/disclaimer.html")

def downloads_view(request):
    return render(request, "accounts/downloads.html")

def partners_view(request):
    return render(request, "accounts/partners.html")

def services_view(request):
    return render(request, "accounts/services.html")

def status_view(request):
    return render(request, "accounts/status.html")

def news_view(request):
    return render(request, "accounts/news.html")

def addition(request):
    if request.method == "POST":
        a=int(request.POST.get("a",""))
        b=int(request.POST.get("b",""))
        c=int(a+b)
        print(c)
        return render(request,'accounts/add.html',{"a":a,"b":b,"c":c})
    return render(request,"accounts/add.html")

def substraction(request):
    if request.method=="POST":
        a=int(request.POST.get("a",""))
        b=int(request.POST.get("b",""))
        c=a-b
        print(c)
        return render(request,'accounts/add.html',{"a":a,"b":b,"c":c})
    return render(request,"accounts/substraction.html")


def multipicatiion(request):
    if request.method=="POST":
        a=int(request.POST.get("a",""))
        b=int(request.POST.get("b",""))
        c=a*b
        print(c)
        return render(request,'accounts/add.html',{"a":a,"b":b,"c":c})
    return render(request,"accounts/multiplication.html")

def division(request):
    if request.method=="POST":
        a=int(request.POST.get("a",""))
        b=int(request.POST.get("b",""))
        c=a/b
        print(c)
        return render(request,'accounts/add.html',{"a":a,"b":b,"c":c})
    return render(request,"accounts/division.html")

def square(request):
    if request.method=="POST":
        a=int(request.POST.get("a",""))
        b=int(request.POST.get("b",""))
        c=a*a
        d=math.sqrt(b)
        print(c)
        print(d)
        return render(request,'accounts/square.html',{"a":a,"b":b,"c":c,"d":d})
    return render(request,"accounts/square.html")

@login_required
def view_profile(request):
    profile = Profile.objects.get(user=request.user)

    return render(request, "accounts/profile.html", {
        "profile": profile
    })


@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == "POST":
        profile.bio = request.POST.get("bio")
        profile.location = request.POST.get("location")

        if request.FILES.get("profile_picture"):
            profile.profile_picture = request.FILES["profile_picture"]

        profile.save()

        return redirect("view_profile")

    return render(request, "accounts/edit_profile.html", {
        "profile": profile
    })