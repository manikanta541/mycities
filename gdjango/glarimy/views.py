from django.shortcuts import render,redirect
import requests
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

url = 'https://4r5qkqzk35.execute-api.us-east-1.amazonaws.com/v1/activecities/'
r = requests.get(url).json()
csub = []
ncsub = []
ozip = [] 
ids = []
l = list()
d = {}
d1= {}
names = []
address = []
msg = ""
for i in range(1,len(r)):
    for j in r[i]['sections']:
        ncsub.append(j['display'])
    csub.append(r[i]['categorydisplay'])
c = 0
c1 = 3
for i in csub:     
    d[i] = ncsub[c:c1]
    c = c+3
    c1 = c1+c
cc = 0
cc1 = 3
for i in csub:     
    d1[i] = ncsub[cc:cc1]
    cc = cc+3
    cc1 = cc1+cc
data = {
        'cname' : r[0]['citydisplay'],
        # 'citysub' : csub
}
def index(request):
    return render(request,'index.html',{'name':'tadepalligudem','data' : data,'citysub':d})
def ok(request):
    global data1
    a = request.POST['csubt']
    for key,value in d1.items():
        if a+" " == key or a+"  " == key:
            data1 = value
    return render(request,'index.html',{'name':'tadepalligudem','data' : data,'citysub':d,'data1':data1})
def ok1(request):
    names = []
    address = []
    url1 = 'https://4r5qkqzk35.execute-api.us-east-1.amazonaws.com/v1/activecities/Tadepalligudem/Health/Hospitals/entry/'
    url2 = 'https://4r5qkqzk35.execute-api.us-east-1.amazonaws.com/v1/activecities/Tadepalligudem/Health/Labs/entry/'
    url3 = 'https://4r5qkqzk35.execute-api.us-east-1.amazonaws.com/v1/activecities/Tadepalligudem/Health/Pharmacies/entry/'
    # url2 = 
    r1 = requests.get(url1).json()
    r2 = requests.get(url2).json()
    r3 = requests.get(url3).json()
    m = request.POST['xyz']
    if m == 'ఆస్పత్రులు':
        for i in range(len(r1)):
            names.append(r1[i]['name'])
            address.append(r1[i]['address'])
            ids.append(r1[i]['url'])
        ozip = zip(names,address,ids)
    elif m == 'పరీక్ష':
        for i in range(len(r2)):
            names.append(r2[i]['name'])
            address.append(r2[i]['address'])
            ids.append(r2[i]['url'])
        ozip = zip(names,address,ids)
    else:
        for i in range(len(r3)):
            names.append(r3[i]['name'])
            address.append(r3[i]['address'])
            ids.append(r2[i]['url'])
        ozip = zip(names,address,ids)
    return render(request,'modals.html',{'ozip':ozip})
def ok2(request):
    n = []
    v = []
    m1 = request.POST['mod']
    url4 = 'https://4r5qkqzk35.execute-api.us-east-1.amazonaws.com/v1/activecities'+m1
    r4 = requests.get(url4).json()
    for i in range(len(r4['data'])):
        n.append(r4['data'][i]['name'])
        v.append(r4['data'][i]['value'])
    ozip2 = zip(n,v)
    # for i in range(len(r4[0]['data'])):
    #     n.append(r4[0]['data'][i]['name'])
    # print(n)
    return render(request,'modals1.html',{'citysub':d,'names':names,'ids':ozip2})
def register(request):
    if request.method == 'POST':
        fname = request.POST['fn']
        lname = request.POST['ln']
        uname = request.POST['un']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if(pass1 == pass2):
            user = User.objects.create_user(username=uname,password=pass1,email=email,first_name=fname,last_name=lname)
            user.save()
            return redirect('login')
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')
def login(request):
    if request.method == 'POST':
        uname = request.POST['un']
        password = request.POST['pass']
        user = auth.authenticate(username=uname,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')