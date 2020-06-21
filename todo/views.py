from django.contrib.auth.hashers import check_password , make_password
from django.shortcuts import render
from .models import todoItem , todouser
from django.http import HttpResponseRedirect , HttpResponse
from django.urls import reverse
from django.utils import timezone

# Create your views here.
def index(request):
    try:
        error = request.POST['error']
    except:
        dict_index = {'error_message':''}
    else:
        dict_index = {'error_message':request.POST['error']}

    try:
        username = (request.session["todousername"])
    except:
        return render(request , 'todo/loginpage.html' , dict_index)
    else:
        dict = {'todoItems':todouser.objects.get(username=username).todoitem_set.all() ,
                'todoItem':todoItem ,
                'todoItem_prior':todoItem.Priority ,
               }
        return render(request , 'todo/index.html' , dict)

def delete(request , q_id):
    rm_item = todoItem.objects.get(pk=q_id)
    if (rm_item.owner.username == request.session['todousername']):
        rm_item.delete()
    return HttpResponseRedirect(reverse('todo:index'))

def add(request , name , text , color_code , prior_code):
    todoItem.objects.create(Name=name , Text=text ,create_date=timezone.now() , Colour=color_code , Priority=prior_code ,owner=todouser.objects.get(username=request.session["todousername"]))
    return HttpResponseRedirect(reverse('todo:index'))

def login(request):
    try:
        user = todouser.objects.get(username=request.POST["username"])
    except:
        return render(request , 'todo/redirector.html' , {"error":"User doesn't exist"})
    else:
        pass_valid = check_password(request.POST['password'] , user.password)
        if pass_valid:
            request.session['todousername'] = user.username
            return HttpResponseRedirect(reverse('todo:index'))
        else :
            return render(request , 'todo/redirector.html' , {'error':'Password incorrect'})

def logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('todo:index'))

def signup(request):
    try:
        username = request.POST['username']
    except:
        return render(request , 'todo/signuppage.html' ,{})
    else:
        try:
            todouser.objects.get(username=username)
        except:
            password = request.POST['password']
            todouser.objects.create(username=username,password=make_password(password))
            request.session['todousername'] = username
            todoItem.objects.create(Name="Welcome!" ,
                                    Text="Start by adding a few items in your list and delete this note" ,
                                    create_date=timezone.now(),
                                    owner=todouser.objects.get(username=username) ,
                                    Colour="BLE" ,
                                    Priority="HI")
            return HttpResponseRedirect(reverse('todo:index'))
        else:
            return render(request , 'todo/signuppage.html' ,{'error':"Username already taken"})


def edit(request,q_id,name,text,color_code,prior_code):
    edit_item = todoItem.objects.get(pk=q_id)
    if (edit_item.owner.username == request.session['todousername']):
        edit_item.Name = name
        edit_item.Text = text
        edit_item.Colour = color_code
        edit_item.Priority = prior_code
        edit_item.save()
    return HttpResponseRedirect(reverse('todo:index'))