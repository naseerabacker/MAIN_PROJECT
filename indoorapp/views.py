from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from indoorapp.models import *


def mainpage(request):
    return render(request,"indd.html")


def login_fun(request):
    return render(request,"login.html")

def login_post(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']
    print(username,password)
    try:
        if login.objects.filter(name=username,password=password).exists():
            ob=login.objects.get(name=username,password=password)
            print(ob)
            if ob.type=='admin':
                request.session['lid']=ob.id
                return HttpResponse('''<script> alert("ok");window.location='/myapp/admin_ind'</script>)''')
            elif ob.type == 'shop':
                request.session['lid']=ob.id

                return HttpResponse('''<script> alert("ok");window.location='/myapp/shop_ind'</script>)''')
            else:
                return HttpResponse('''<script> alert("Invalid username or password");window.location='/myapp/mainpage'</script>)''')
        else:
            return HttpResponse('''<script> alert("Invalid username or password");window.location='/myapp/mainpage'</script>)''')
    except Exception as e:
        print(e)
        return HttpResponse('''<script> alert("error");window.location='/myapp/mainpage'</script>)''')
     # return HttpResponse('HAI')

def admin_ind(request):
    return render(request,"ADMIND.html")
def shop_ind(request):
    return render(request,"shopindex.html")



def admin_add_shop(request):
    res=floor.objects.all()
    return render(request,"admin/addshop.html",{"data":res})

def admin_add_shop_post(request):

    Logo=request.FILES['fileField']
    shopname=request.POST['textfield']
    floor=request.POST['textfield6']
    Category=request.POST['textfield7']
    shopnumber=request.POST['textfield2']
    email=request.POST['textfield3']
    phonenumber=request.POST['textfield5']
    from datetime import datetime
    date=datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"
    fs=FileSystemStorage()
    fn=fs.save(date,Logo)
    path=fs.url(date)

    lobj = login()
    lobj.name=email
    lobj.password=phonenumber
    lobj.type='shop'
    lobj.save()
    sobj=shop()
    sobj.logo=path
    sobj.shopname=shopname
    sobj.Category=Category
    sobj.email = email
    sobj.phonenumber = phonenumber
    sobj.shopnumber = shopnumber
    sobj.FLOOR_id=floor
    sobj.LOGIN=lobj
    sobj.save()

    return redirect('/myapp/admin_view_shops')

    # return HttpResponse("ok")


def floor_shop(request,id):
    print(id)
    res=shop.objects.filter(FLOOR=id)
    return render(request,"shopfil.html",{'data':res})

def admin_add_floor(request):
    res=floor.objects.all()
    return render(request,"admin/add floor.html",{'data':res})



def admin_add_floor_post(request):
    Floornumber=request.POST['textfield']
    # Details=request.POST['textfield1']
    fobj=floor()
    fobj.floorno=Floornumber

    fobj.save()

    # return HttpResponse("ok")
    return redirect('/myapp/admin_view_floor/')


def admin_edit_floor(request,did):
    res=floor.objects.get(id=did)

    return render(request,"admin/editfloor.html",{'data':res})



def admin_edit_floor_post(request):
    did = request.POST["hh"]
    floorno=request.POST['textfield']
    res = floor.objects.filter(pk=did).update(floorno=floorno)
    return redirect('/myapp/admin_view_floor')

def admin_delete_floor(request,id):
    res=floor.objects.get(pk=id).delete()
    # return redirect('/myapp/admin_view_floor/')


    return HttpResponse('''<script> alert("DELETE?");window.location='/myapp/admin_view_floor'</script>)''')


def admin_view_floor(request):

    res=floor.objects.all()
    return render(request,"admin/viewfloor.html",{'data':res})

def view_floor(request):
    res=floor.objects.all()
    res2=shop.objects.all()

    return render(request,"viewfloor.html",{'data':res,'data2':res2})

def admin_view_feedback(request):
    return render(request,"admin/feedback.html")



def view_feedback(request):
    return render(request,"viewfeed.html")

def admin_add_hotspot(request):
    return render(request,"admin/addhotspot.html")

def admin_add_hotspot_post(request):
    Shop=request.POST['jumpMenu']
    HotspotAddress=request.POST['textfield']

    hobj =hotspot()
    hobj.hotspotaddress =HotspotAddress
    hobj.SHOP=Shop
    hobj.save()

    return HttpResponse("ok")

def admin_edit_hotspot(request):
    return render(request,"admin/edithotspot.html")
def admin_edit_hotspot_post(request):
    Shop=request.POST['textfield']
    hotspotaddress=request.POST['textfield2']
    return HttpResponse("ok")



def admin_view_hotspot(request):
    return render(request,"admin/viewhotspot.html")

def admin_view_complaint(request):
    return render(request,"admin/viewcmplnt.html")

def cus_post_complaint(request):
    return render(request,"cus/postcom.html")


def cus_post_complaint_post(request):
    complaint=request.POST['textfield ']
    cobj = complaint()
    cobj.complaint=complaint
    cobj.save()
    return HttpResponse("ok")

def cus_send_feedbk(request):
    return render(request,"cus/sendfeedbk.html")

def cus_send_feedbk_post(request):
    Feedback = request.POST['textfield ']
    fobj=feedback()
    fobj.feedback=Feedback
    fobj.save()
    return HttpResponse("ok")



def add_product(request):
    return render(request,"shop/addpro.html")



def add_product_post(request):
    productname = request.POST['textfield']
    price = request.POST['textfield2']
    Description = request.POST['textfield3']
    Stock= request.POST['textfield4']
    photo= request.FILES['img']
    from datetime import datetime
    date = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
    fs = FileSystemStorage()
    fn = fs.save(date, photo)
    path = fs.url(date)
    pobj=product()
    pobj.SHOP=shop.objects.get(LOGIN=request.session['lid'])
    pobj.productname=productname
    pobj.price=price
    pobj.description=Description
    pobj.stock=Stock
    pobj.photo=path
    pobj.save()


    return HttpResponse("ok")


def change_pass(request):
    return render(request, "changepass.html")
def change_pass_post(request):

     Currentpassword=   request.POST['textfield ']

     newpassword = request.POST['textfield2 ']
     confirmpassword = request.POST['textfield3 ']

     return HttpResponse("ok")



#
# def admin_add_floor_post(request):
#     Floornumber=request.POST['textfield']
#
#     fobj=floor()
#     fobj.floorno=Floornumber
#     fobj.save()
#
#
#     return HttpResponse("ok")



def signup(request):
    return render(request,"signup.html")

def signup_post(request):
    firstname = request.POST['textfield1 ']
    lastname = request.POST['textfield2']
    email = request.POST['textfield3 ']
    Phonenumber = request.POST['textfield4 ']
    password = request.POST['textfield6 ']
    lobj=login()
    lobj.name=email
    lobj.password=password
    lobj.type='user'
    lobj.save()
    uobj=user()
    uobj.firstname=firstname
    uobj.lastname=lastname
    uobj.email=email
    uobj.Phonenumber=Phonenumber
    uobj.LOGIN=lobj
    uobj.save()
    return HttpResponse("ok")


def view_offer(request):
    return render(request,"viewoffr.html")

def view_product(request):
    res=product.objects.all()

    return render(request,"viewproduct.html", {'data': res})

def shop_view_product(request):
    res=product.objects.all()
    return render(request,"shop/viewpro.html", {'data': res})


def shop_profile(request):
    lid=request.session['lid']
    res=shop.objects.get(LOGIN_id=lid)

    return render(request,"shop/profile.html",{'data':res})



def floor_shop(request,id):
    print(id)
    res=shop.objects.filter(FLOOR=id)
    return render(request,"shopfil.html",{'data':res})


#
# def view_category(request):
#     res=shop.objects.all()

    # res=category.objects.all()
    # return render(request,"viewshops.html")

#     return render(request,"category.html",{'data':res})

def admin_view_shops(request):
    res=shop.objects.all()
    return render(request,"admin/viewshop.html",{'data':res})


def admin_delete_shop(request,id):
    res=shop.objects.get(pk=id).delete()
    # return redirect('/myapp/admin_view_shops/')
    # return HttpResponse("ok")
    # return redirect('/myapp/admin_view_shops')
    return HttpResponse('''<script> alert("DELETE");window.location='/myapp/admin_view_shops'</script>)''')


def admin_edit_shops(request,did):
    res=shop.objects.get(id=did)
    res2=floor.objects.all()
    print(res)
    request.session['sid']=did

    return render(request,"editshop.html",{'data':res,'data2':res2})

def admin_edit_shops_post(request):
    print('hi')
    did=request.POST['h1']
    Logo = request.FILES['fileField']
    shopname = request.POST['textfield']
    floor = request.POST['textfield6']
    Category = request.POST['textfield7']
    shopnumber = request.POST['textfield2']
    email = request.POST['textfield3']
    phonenumber = request.POST['textfield5']
    sobj = shop.objects.get(id=request.session['sid'])

    if 'fileField' in request.FILES:
        Logo = request.FILES['fileField']
        if Logo.name != "":
            from datetime import datetime
            date = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
            fs = FileSystemStorage()
            fn = fs.save(date, Logo)
            path = fs.url(date)
            # print(path,'==============================')
    sobj.shopname = shopname
    sobj.floor = floor
    sobj.shopnumber = shopnumber
    sobj.Category = Category
    sobj.email = email
    sobj.phonenumber = phonenumber

    sobj.logo = path
    sobj.save()


    return redirect('/myapp/admin_view_shops')


def view_shop_detail(request,id):

    return render(request,"shopdetail.html")


def send_notifi(request,did):
    res=notification.objects.all()

    return render(request,"admin/sendnotifi.html")


def send_notifi_post(request):
    did = request.POST['h1']

    noti = request.POST['textfield']

    # time = request.POST['textfield1']
    # status = request.POST['textfield3']
    # date = request.POST['textfield2']
    nobj =notification()
    nobj.notification =noti
    # nobj.date = date
    # nobj.time = time
    # nobj.status = status

    nobj.save()
    # return HttpResponse("ok")
    return redirect('/myapp/admin_view_shops')

def view_notifi(request):
    res=notification.objects.all()
    return render(request, "viewnotifi.html", {'data':res})

#
def edit_profile(request,did):
    lid=request.session['lid']
    request.session['shopid']=did
    res=shop.objects.get(LOGIN_id=lid)
    request.session['sid']=did

    res2=floor.objects.all()
    print(res)
    return render(request,"shop/editprofile.html",{'data':res,'data2':res2})

def edit_profile_post(request):
    print('hi')
    did = request.POST['h1']
    Logo = request.FILES['fileField']
    shopname = request.POST['textfield']
    floor = request.POST['textfield6']
    Category = request.POST['textfield7']
    # shopnumber = request.POST['textfield2']
    email = request.POST['textfield3']
    phonenumber = request.POST['textfield5']

    sobj = shop.objects.get(id=request.session['sid'])

    if 'fileField' in request.FILES:
        Logo = request.FILES['fileField']
        if Logo.name != "":
            from datetime import datetime
            date = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
            fs = FileSystemStorage()
            fn = fs.save(date, Logo)
            path = fs.url(date)


    sobj.shopname = shopname
    sobj.floor = floor
    # sobj.shopnumber = shopnumber
    sobj.Category = Category
    sobj.email = email
    sobj.phonenumber = phonenumber
    sobj.logo = path
    sobj.save()
    return redirect('/myapp/shop_profile')






# shop view shops\\\\\
def view_shop(request):
        res = shop.objects.all()
        if request.method == "POST":
            name = request.POST['shopname']
            res = shop.objects.filter(shopname__icontains=name)
        # else:
        #          return HttpResponse('''<script> alert("no shops");window.location='/myapp/view_shops'</script>)''')
        return render(request, "shop/viewshop.html", {'data': res})













def view_shops(request):
        res = shop.objects.all()
        if request.method == "POST":
            name = request.POST['shopname']
            res = shop.objects.filter(shopname__icontains=name)
        # else:
        #          return HttpResponse('''<script> alert("no shops");window.location='/myapp/view_shops'</script>)''')
        return render(request, "viewshops.html", {'data': res})



        # return HttpResponse("ok")
#-------------------------------------------------------------------

#    android


def android_login_post(request):
    # res=login.objects.all()
    username = request.POST['username']
    password = request.POST['password']
    lid=request.POST['lid']

    if login.objects.filter(name=username, password=password).exists():
        ob = login.objects.get(name=username, password=password)
        print(ob)
        if ob.type == 'customer':
            return JsonResponse({'status':'ok', 'lid':lid, 'type':type})
        else:
            return JsonResponse({'status': 'no'})
    else:
        return JsonResponse({'status': 'no'})


def android_signup_post(request):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    phonenumber = request.POST['phonenumber']

    email = request.POST['email']
    password = request.POST['password']
    confirmpassword = request.POST['confirmpassword']

    lobj = login()
    lobj.name = email
    lobj.password = password

    lobj.type = 'user'
    lobj.save()
    uobj = user()
    uobj.firstname = firstname
    uobj.lastname = lastname
    uobj.email = email
    uobj.phonenumber = lastname
    uobj.LOGIN = lobj
    uobj.save()
    return JsonResponse({'status': 'ok'})



def cus_view_shop(request):
    sh=shop.objects.get()
    print(sh)
    data=list(sh.values())
    return JsonResponse({'status': 'ok','shopname':sh.shopname,})
#
# def cus_view_shop(request):
#     shops = shop.objects.all().values('shopname', 'type', 'Category', 'email', 'logo', 'phonenumber', 'FLOOR')
#     return JsonResponse({'status': 'ok', 'data': list(shops)})

#
# def  andview_shop(request):
#     # lid = request.POST['lid']
#     coj=shop.objects.all
#     return JsonResponse({'status':'ok','shopname':coj.shopname,'Category':coj.Category,'email':coj.email,'phonenumber':coj.phonenumber,'FLOOR':coj.FLOOR                         })