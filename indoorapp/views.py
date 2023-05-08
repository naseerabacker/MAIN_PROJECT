from datetime import datetime
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, redirect
import numpy as np
from indoorapp.dijkstra import shortest_path


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
    x_axis=request.POST['textfield9']
    y_axis=request.POST['textfield10']

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
    sobj.x_axis = x_axis
    sobj.y_axis = y_axis

    sobj.phonenumber = phonenumber
    sobj.shopnumber = shopnumber
    sobj.FLOOR_id=floor
    sobj.LOGIN=lobj
    sobj.save()

    hobj=hotspot()
    hotspotaddress=request.POST['textfield8']
    hobj.hotspotaddress=hotspotaddress
    hobj.SHOP=sobj
    hobj.save()

    return redirect('/myapp/admin_view_shops')



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
    res2=shop.objects.all()
    res=floor.objects.all()
    return render(request,"admin/viewfloor.html",{'data':res,'data2':res2})



def view_floor(request):
    res=floor.objects.all()
    res2=shop.objects.all()

    return render(request,"viewfloor.html",{'data':res,'data2':res2})


# def floor_shop(request,id):
#     print(id)
#     res=shop.objects.filter(FLOOR=id)
#     return render(request,"shopfil.html",{'data':res})
#
#
#
# def view_floor(request,id):
#     res=shop.objects.filter(FLOOR=id)
#     return render(request,"viewfloor.html",{'data':res})

def admin_view_feedback(request):
    res = feedback.objects.all()
    return render(request,"admin/viewfeedback.html", {'data': res})



def view_feedback(request):
    return render(request,"viewfeed.html")


def view_query(request):
    res = emergencymessage.objects.all()
    return render(request,"admin/viewquery.html", {'data': res})


def reply_query(request,id):
    request.session['emid']=id
    return render(request,"admin/emreply.html")

def reply_query_post(request):
    reply=request.POST['comment']
    hobj =emergencymessage.objects.get(id=request.session['emid'])
    hobj.reply =reply
    hobj.status ='replied'
    hobj.save()
    # return HttpResponse("ok")
    return redirect('/myapp/view_query/')

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
    res3 = hotspot.objects.get(SHOP=lid)

    return render(request,"shop/profile.html",{'data':res,'data3':res3})



def floor_shop(request,id):
    print(id)
    res=shop.objects.filter(FLOOR=id)
    return render(request,"shopfil.html",{'data':res})


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

#
# def admin_edit_shops(request,did):
#     res=shop.objects.get(id=did)
#     res2=floor.objects.all()
#     res3=hotspot.objects.get(SHOP=shop.objects.get(LOGIN=did))
#     print(res3.id)
#     request.session['sid']=did
#
#     return render(request,"editshop.html",{'data':res,'data2':res2,'data3':res3})


def admin_edit_shops(request,did):
    res=shop.objects.get(id=did)
    res2=floor.objects.all()
    print(res)
    res3 = hotspot.objects.get(SHOP=did)
    print(res3.id)
    request.session['sid']=did

    return render(request,"editshop.html",{'data':res,'data2':res2,'data3':res3})

def admin_edit_shops_post(request):
    print('hi')
    did=request.POST['h1']
    shopname = request.POST['textfield']
    floor = request.POST['textfield6']
    Category = request.POST['textfield7']
    shopnumber = request.POST['textfield2']
    email = request.POST['textfield3']
    phonenumber = request.POST['textfield5']
    sobj = shop.objects.get(id=request.session['sid'])
    hotspotaddress = request.POST['textfield8']
    x_axis = request.POST['textfield9']
    y_axis = request.POST['textfield10']

    if 'fileField' in request.FILES:
        logo = request.FILES['fileField']
        if logo.name != "":
            from datetime import datetime
            date = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
            fs = FileSystemStorage()
            fn = fs.save(date, logo)
            path = fs.url(date)
            shop.objects.filter(id=did).update(shopname=shopname,shopnumber=shopnumber,Category=Category,email=email,phonenumber=phonenumber,logo=path)

            hotspot.objects.filter(SHOP=did).update(hotspotaddress=hotspotaddress)
        else:
            shop.objects.filter(id=did).update(shopname=shopname, shopnumber=shopnumber, Category=Category, email=email,phonenumber=phonenumber)

            hotspot.objects.filter(SHOP=did).update(hotspotaddress=hotspotaddress)


    else:

        shop.objects.filter(id=did).update(shopname=shopname, shopnumber=shopnumber, Category=Category, email=email, phonenumber=phonenumber)

        hotspot.objects.filter(SHOP=did).update(hotspotaddress=hotspotaddress)

    return redirect('/myapp/admin_view_shops')



def view_shop_detail(request,did):
    res=shop.objects.get(id=did)
    # res2=hotspot.objects.get(id=did)
    return render(request,"shopdetail.html",{'data':res})

    # return render(request,"shopdetail.html",{'data':res,'data2':res2})



def view_shop_detail_admin(request,did):
    res=shop.objects.get(id=did)
    res2=hotspot.objects.get(SHOP=did)
    return render(request,"admin/adminshopdetail.html",{'data':res,'data2':res2})

def edit_profile(request,did):
    lid=request.session['lid']
    request.session['shopid']=did
    res=shop.objects.get(LOGIN_id=lid)
    request.session['sid']=did
    res3 = hotspot.objects.get(SHOP=did)

    res2=floor.objects.all()
    print(res)
    return render(request,"shop/editprofile.html",{'data':res,'data2':res2,'data3':res3})

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

def send_notifi(request):
            res = notification.objects.all()
            return render(request, "admin/sendnotifi.html")

def send_notifi_post(request):
            did = request.POST['h1']
            noti = request.POST['textfield']

            nobj = notification()
            nobj.notification = noti


            nobj.save()
            return redirect('/myapp/admin_view_shops')

def view_notifi(request):
    res = notification.objects.all()

    # res = notification.objects.filter(shop_id=id)
    return render(request, "viewnotifi.html", {'data': res})



def add_direction(request):
    res = shop.objects.all()
    return render(request, "admin/addirection.html",{"data":res})

def add_direction_post(request):
    shopname1=request.POST['textfield']
    shopname2=request.POST['textfield1']
    direct=request.POST['textfield3']

    fobj=direction()
    res=shop.objects.get(id=shopname1)
    fobj.shopida=res
    res2=shop.objects.get(id=shopname2)
    fobj.shopidb=res2
    fobj.direction=direct
    fobj.save()
    # return HttpResponse("ok")


    return redirect('/myapp/view_direction')


def view_direction(request):
        res = direction.objects.all()
        res2 = shop.objects.all()

        return render(request, "admin/viewdirection.html",{'data': res,'data2':res2})



# +++++++++++++++++++++
#-------------------------------------------------------------------

#    android


def android_login_post(request):
    # res=login.objects.all()
    username = request.POST['username']
    password = request.POST['password']
    # lid=request.POST['lid']

    if login.objects.filter(name=username, password=password).exists():
        ob = login.objects.get(name=username, password=password)
        print(ob)
        if ob.type == 'customer':
            return JsonResponse({'status':'ok', 'lid':ob.id, 'type':ob.type})
        else:
            return JsonResponse({'status': 'no'})
    else:
        return JsonResponse({'status': 'no'})


def android_signup_post(request):
    firstname = request.POST['firstname']
    # lastname = request.POST['lastname']
    phonenumber = request.POST['phone']
    email = request.POST['email']
    password = request.POST['password']
    confirmpassword = request.POST['confirmpassword']

    lobj = login()
    lobj.name = email
    lobj.password = password
    lobj.type = 'customer'
    lobj.save()
    uobj = user()
    uobj.firstname = firstname
    # uobj.lastname = lastname
    uobj.email = email
    uobj.phonenumber = phonenumber
    uobj.LOGIN = lobj
    uobj.save()
    return JsonResponse({'status': 'ok'})




def cus_view_shop(request):
    l=[]
    sh=shop.objects.filter(type="shop")
    for i in sh:
        l.append({'id':i.id,'shopname':i.shopname,'shopnumber':i.shopnumber,'Category':i.Category,'email':i.email,'phonenumber':i.phonenumber,'FLOOR':i.FLOOR.floorno,"logo":i.logo,'x_axis':i.x_axis,'y_axis':i.y_axis})
    print(l)
    return JsonResponse({'status': 'ok','data': l })


def cus_view_shop_post(request):
    shopnames=request.POST['shop']
    l=[]
    sh=shop.objects.filter(shopname=shopnames)
    for i in sh:
        l.append({'id':i.id,'shopname':i.shopname,'shopnumber':i.shopnumber,'Category':i.Category,'email':i.email,'phonenumber':i.phonenumber,'FLOOR':i.FLOOR.floorno,"logo":i.logo,'x_axis':i.x_axis,'y_axis':i.y_axis})
    print(l)
    return JsonResponse({'status': 'ok','data': l })


def cus_view_shop_floor(request):
    floorid=request.POST['floorid']
    l=[]
    sh=shop.objects.filter(FLOOR_id=floorid)
    for i in sh:
        l.append({'id':i.id,'shopname':i.shopname,'shopnumber':i.shopnumber,'Category':i.Category,'email':i.email,'phonenumber':i.phonenumber,'FLOOR':i.FLOOR.floorno,"logo":i.logo,'x_axis':i.x_axis,'y_axis':i.y_axis})
    print(l)
    return JsonResponse({'status': 'ok','data': l })







def cus_view_floor(request):
        l = []
        sh = floor.objects.all()
        for i in sh:
            l.append({'id': i.id, 'floorno': i.floorno})
        return JsonResponse({'status': 'ok', 'data': l})

def shop_view(request):
    shopid=request.POST['shopid']
    print(shopid)
    sh=shop.objects.get(id=shopid)
    return JsonResponse({'status':'ok','sid':sh.id,'logo':sh.logo,'shopname':sh.shopname,'shopnumber':sh.shopnumber,'email':sh.email,'phonenumber':sh.phonenumber,'floor':sh.FLOOR.floorno,'category':sh.Category,'x_axis':sh.x_axis,'y_axis':sh.y_axis})

def my_find(request):
    mac=request.POST["mac"]
    # print(mac)
    dd=mac.split("#")


    print(dd)
    shopid=request.POST["shop"]

    imagepath="C:\\Users\\USER\\PycharmProjects\\indoornav\\plan.png"
    import cv2

    img = cv2.imread(imagepath)

    # print(shopid)
    res = shop.objects.get(id=shopid)

    toshopid = 0
    dd.remove('')

    resnew = ''

    if len(dd) > 0:
        for i in dd:
            print(i," HSTSPOTS")
            if hotspot.objects.filter(hotspotaddress=i).exists():
                po=hotspot.objects.get(hotspotaddress=i)
                print(po, "PPPOOOO")
                toshopid = po.SHOP.id
                break
    shopids=[]
    ff=shop.objects.all()
    for i in ff:
        shopids.append(i.id)

    s = {}
    # print(toshopid, " toshpoid")
    for i in shopids:
        m = []

        your_set = set()

        for j in shopids:
            qty=direction.objects.filter(shopida=i,shopidb=j)
            if qty.exists():
                qty = direction.objects.get(shopida=i, shopidb=j)
                m.append(j)
        your_set.update(m)
        s[i] = your_set

    # print(s, "hurrrrrrraaaaaaaaaaaaaaaaaaaai", "====", shopid, "====", toshopid)

    s = shortest_path(s, toshopid, int(shopid))

    print(s," shortest")

    print(s)

    d = []

    finalplan = []

    for i in range(0,len(s)-1):
        frm=s[i]
        qry=shop.objects.get(id=frm)

        km=qry.shopname
        tos=s[i+1]
        qrye = shop.objects.get(id=tos)
        sm = qrye.shopname
        m=""
        x1=qry.x_axis
        y1=qry.y_axis
        x2=qrye.x_axis
        y2=qrye.y_axis

        cv2.line(img,(x1,y1),(x2,y2), (255,0,0), 5)

        if direction.objects.filter(shopida=frm,shopidb=tos).exists():
            ppt=direction.objects.get(shopida=frm,shopidb=tos)
            print(ppt, " if ppt")

            m=ppt.direction

        else:
            ppt=direction.objects.filter(shopida=tos, shopidb=frm)
            if ppt.exists():
                print(ppt, " ppt")
                ppt = direction.objects.get(shopida=tos, shopidb=frm)
                m=ppt.direction
                if m=="East":
                    m="West"
                elif m=="West":
                    m="East"
                elif m=="North":
                    m="South"
                elif m=="South":
                    m="North"
                elif m=="Forward":
                    m="Down"
                elif m=="Down":
                    m="Forward"
                elif m == "Up":
                    m = "Down"
                elif m == "Down":
                    m = "up"
        print(m,"directions")
        d={'km':km,'direction':m, 'sm':sm}
        finalplan.append(d)
        print(finalplan)

    from datetime import datetime
    dt = datetime.now().strftime("%Y%m%d%H%M%S%f")
    h=cv2.imwrite("C:\\Users\\USER\\PycharmProjects\\indoornav\\media\\routes\\"+dt+".jpg",img)
    route="/media/routes/"+dt+".jpg"
    print(h,"haiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")


    request.session["fplans"] = finalplan
    print(request.session["fplans"])

    return JsonResponse({"status":"ok","data":finalplan,"route":route})

def cus_view_direction(request):
    fplans = request.session["fplans"]
    return JsonResponse({'status': 'ok', 'data': fplans})



def send_feedback(request):
    feed =request.POST["feedback"]
    lid=request.POST["lid"]

    res=user.objects.get(LOGIN=lid)

    fobj=feedback()
    fobj.feedback=feed
    fobj.date=datetime.now()
    fobj.USER=res
    fobj.save()
    return JsonResponse({'status': 'ok'})


def send_query(request):
    qry =request.POST["emer"]
    lid=request.POST["lid"]

    res=user.objects.get(LOGIN=lid)

    fobj=emergencymessage()
    fobj.emergencymessage=qry
    fobj.date=datetime.now()
    fobj.time=datetime.now()

    fobj.USER=res
    fobj.save()
    return JsonResponse({'status': 'ok'})

def logout(request):

    return JsonResponse({'status': 'ok'})


def view_query_reply(request):
    l = []
    lid=request.POST['lid']
    sh = emergencymessage.objects.filter(USER_id=user.objects.get(LOGIN_id=lid).id)
    for i in sh:
        l.append( {'id': i.id, 'query': i.emergencymessage, 'reply': i.reply,  'time': i.time, 'date': i.date,  'status': i.status, 'USER_ID': i.USER_id })
    return JsonResponse({'status': 'ok', 'data': l})

