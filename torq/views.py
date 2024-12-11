from django.shortcuts import render,redirect
from .models import registration

# Create your views here.
def index(request):
    return render(request, 'index.html')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        role = request.POST.get('role')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        registration(email=email, password=password, name=name, role=role, phone=phone).save()

        return redirect('index')
    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = registration.objects.get(email = email,password = password)
            semail = user.email
            request.session['email'] = semail
            return render(request,'index.html')
        except:
            msg = "invalid password or email id"
            return render(request,'login.html',{"msg":msg})
    return render(request,'login.html')
        

def profile(request):
    if 'email' in request.session:
        mail = request.session['email']
        user = registration.objects.get(email = mail)
    return render(request, 'profile.html', {'user': user})

def view_pro(request):
    if 'email' in request.session:
        mail = request.session['email']
        user = registration.objects.get(email = mail)
    return render(request, 'view_pro.html', {'user': user})


def edit_pro(request, id):
    edit_pro = registration.objects.get(id = id)
    user = request.user
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        # email = request.POST.get('email')
        role = request.POST.get('role')
        address = request.POST.get('address')
        image =  request.FILES.get('image')
        edit_pro = registration.objects.get(id = id)

        edit_pro.name = name
        edit_pro.phone = phone
        # edit_pro.email = email
        edit_pro.role = role
        edit_pro.address = address

        if image:
            edit_pro.image = image

        # im = edit_pro.image
        # edit_pro.image = im

        edit_pro.save()

        # profile(email=email, password=password, name=name, phone=phone, gender=gender, address=address).save()

        return redirect('view_pro')
    return render(request,'edit_pro.html', {'user': user})

def service(request):
    return render(request, 'service.html')

def admin_login(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        psword=request.POST.get('Password')
        u='admin'
        p='ps'
        if uname==u:
            if psword==p:
                return redirect('admin_dashboard')
            return render(request,'register.html')
    return render(request,'admin_login.html')

def user_list(request):
    user=registration.objects.all()
    return render(request,'user_list.html',{'user':user})

def delete_user(request,id):
    user=registration.objects.get(id=id)
    user.delete()
    return redirect('user_list')