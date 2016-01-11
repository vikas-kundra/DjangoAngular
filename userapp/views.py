from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.
from django.http import HttpResponse
from .forms_old import PostForm, LoginForm
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, get_backends
# fro    m .backends import ClientAuthBackend
from .models import User, User_new, UserDetails
from io import StringIO
from .serializers import User_new_serializer, User_serializer, test_serializer, insert_serializer
from userapp.forms import AuthenticationForm, RegistrationForm
from django.shortcuts import render_to_response
from django.contrib.auth import login as django_login, authenticate, logout as django_logout
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_protect
from django.template.context_processors import csrf
from django.http import JsonResponse
import json
import logging
import pdb
import ipdb

"""
Dashboard page for app
"""


@login_required(redirect_field_name=None, login_url=None)
def index(request):
    #if request.session['login_status']=='YES':
    #    data_list = User.objects.all()
    #    output = ', '.join([q.user_name for q in data_list])
    #    return HttpResponse(output)

    if request.user.is_authenticated():
        data_list = User.objects.all
        #data_list = User_new.objects.all
        template = loader.get_template('userapp/index.html')
        context = RequestContext(request, {
            'data_list': data_list,
        })
        return HttpResponse(template.render(context))
    else:
        return HttpResponseRedirect('/userapp/login/')


class dashboard(generics.ListAPIView):
    lookup_url_kwarg = 'email'

    def get(self, request, format='None'):
        #if request.user.is_authenticated():
        #    data_list = User.objects.all
        #data_list = User_new.objects.all
        data_list = []
        s_data_list = []
        j_data_list = []
        ##data_list = self.kwargs.get(self.lookup_url_kwarg)
        email_obtained = self.request.query_params.get('email', None)
        if email_obtained is not None:
            data_list = User.objects.filter(email=email_obtained)
            s_data_list = User_serializer(data_list, many='true')
            #data_list = 'Entered email'
            #j_data_list = json.dumps(s_data_list.data)
            j_data_list = s_data_list.data[0]['email']

        template = loader.get_template('userapp/index.html')
        context = RequestContext(request, {
            'data_list': j_data_list,
        })
        return HttpResponse(template.render(context))

    def post(self, request, format='None'):
        data_list = request.data['email']

        template = loader.get_template('userapp/index.html')
        context = RequestContext(request, {
            'data_list': data_list,
        })
        return HttpResponse(template.render(context))


"""
Function to display all data present in User_new table
"""


def display(request):
    data_list = User_new.objects.all
    template = loader.get_template('userapp/display.html')
    context = RequestContext(request, {
        'data_list': data_list,
    })
    return HttpResponse(template.render(context))


def country(request):
    data_list = User.objects.all()
    output = ', '.join([q.country for q in data_list])
    return HttpResponse(output)


"""
Functional based view in order to display specific records
"""


def detail(request, user_id):
    data_list = User.objects.filter(id=user_id)
    context = {'data_list': data_list}
    #render(request,'userapp/index.html',context)
    template = loader.get_template('userapp/index.html')
    context = RequestContext(request, {
        'data_list': data_list,
    })
    return HttpResponse(template.render(context))


"""
Functional based view in order to perform register new user using django forms
"""


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            #User = form.save(commit=False)
            User_new = form.save(commit=False)
            User_new.password = request.POST['password']
            #User.id = '5'
            #User.user_name = request.user_name
            #User.country = request.country
            User_new.save()
            return HttpResponseRedirect('/userapp/')
    else:
        form = PostForm()
    return render(request, 'userapp/new_user.html', {'form': form})


"""
Functional based view in order to perform login operation using django forms
"""


def login_django(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['login_status'] = 'YES'
            return HttpResponseRedirect('index')
    else:
        form = LoginForm()
    return render(request, 'userapp/Login.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['user_name']
            password = request.POST['password']
            user = authenticate(user_name=username, password=password)
            if user is not None:
                return HttpResponseRedirect('/userapp/index/')
    else:
        form = LoginForm()
    return render(request, 'userapp/Login.html', {'form': form})


"""
Functional based view in order to perform login operation
"""


def user_login(request):
    """
    Log in view
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(email=request.POST['email'], password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    django_login(request, user)
                    return redirect('/userapp/index')
    else:
        form = AuthenticationForm()
    return render_to_response('userapp/Login.html', {
        'form': form,
    }, context_instance=RequestContext(request))


"""
Functional based view in order to register new user
"""


def register(request):
    """
    User registration view.
    """
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/userapp/login')
    else:
        form = RegistrationForm()
    return render_to_response('userapp/register.html', {
        'form': form,
    }, context_instance=RequestContext(request))


class NewView(generics.ListAPIView):
    model = User_new
    queryset = User_new.objects.all()
    serializer_class = User_new_serializer


class LoginView(generics.RetrieveAPIView):
    template_name = 'Login.html'
    form_class = AuthenticationForm
    success_url = '/userapp/index/'


@api_view(['POST'])
@renderer_classes((JSONRenderer,))
def user_login_drf(request):
    """
    Log in view
    """
    if request.method == 'POST':
        #form = AuthenticationForm(data=request.POST)
        user = authenticate(email=request.data['email'], password=request.data['password'])
        if user is not None:
            if user.is_active:
                django_login(request, user)
                val = {'success': 'True'}
                return Response(val)
                #return redirect('/userapp/index')

    else:
        form = AuthenticationForm()
    return render_to_response('userapp/Login.html', {
        'form': form,
    }, context_instance=RequestContext(request))


"""
DRF Class containing code for serialization for Custom User Model
"""


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = User_serializer
    renderer_classes = (JSONRenderer, )

    def get(self, request, format='None'):
        #    query_set = User.objects.all()
        #    object_s = User_serializer(query_set,many='true')
        #    return Response(object_s.data)
        form = AuthenticationForm()
        return render_to_response('userapp/Login.html', {
            'form': form,
        }, context_instance=RequestContext(request))

    def post(self, request, format='None'):
        user = authenticate(email=request.data['email'], password=request.data['password'])
        if user is not None:
            if user.is_active:
                django_login(request, user)
                val = {'success': True}
                return Response(val)
                #return redirect('/userapp/index')

        else:
            val = {'success': False}
            return Response(val)


"""
DRF Class containing code for API call for  login mechanism
"""


class NewUserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = User_serializer
    renderer_classes = (JSONRenderer, )


    def get(self, request, format='None'):
        #    query_set = User.objects.all()
        #    object_s = User_serializer(query_set,many='true')
        #    return Response(object_s.data)
        csrf_token = {}
        csrf_token.update(csrf(request))
        return render_to_response("userapp/Latest_Login.html", csrf_token)


    def post(self, request, format='None'):
        data = {}
        user = authenticate(email=request.data['email'], password=request.data['password'])
        if user is not None:
            if user.is_active:
                django_login(request, user)
                val = {'success': True}
                data['success'] = 'true'
                return HttpResponse(json.dumps(data), content_type="application/json")

                #return HttpResponse(val)
                #return JsonResponse(val)
                #return  val
                #return redirect('/userapp/index')

        else:
            val = {'success': False}
            return Response(val)


class DisplayUserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = test_serializer
    renderer_classes = (JSONRenderer,)

    def get(self, request, format='None'):
        objects_recieved = User.objects.all()
        serialized_object = test_serializer(objects_recieved, many='true')
        json_return = JSONRenderer().render(serialized_object.data)
        return Response(json_return)


class NewUserListAng(generics.ListAPIView):
    def get(self, request, format='None'):
        return render_to_response("userapp/new_user_ang.html")


    def post(self, request, format='None'):
        New_User = User_new(user_name=request.data['username'], password=request.data['password'],
                            age=request.data['age'], country=request.data['country'])
        New_User.save()
        val = {}
        val['data'] = 'success'
        return Response(val)


class NewUserDetailsListAng(generics.ListAPIView):
    def get(self, request, format='None'):
        return render_to_response("userapp/new_user_ang.html")


    def post(self, request, format='None'):
        New_User = UserDetails(email=request.data['email'], name=request.data['username'], age=request.data['age'],
                               country=request.data['country'], password=request.data['password'])
        New_User.save()
        val = {}
        val['data'] = 'success'
        return Response(val)


"""
DRF class not making use of serializer in order to save object
"""


class NewUserClass(generics.ListAPIView):
    def get(self, request, format='None'):
        return render_to_response("userapp/new_user_ang.html")


    def post(self, request, format='None'):
        password_val = request.data['password']
        New_User = User(email=request.data['email'], name=request.data['username'], age=request.data['age'],
                        country=request.data['country'])
        New_User.set_password(password_val)
        New_User.save()
        val = {}
        val['data'] = 'success'
        return Response(val)


"""
DRF class for creating user
"""


class NewUserInsert(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = insert_serializer
    renderer_classes = (JSONRenderer,)


    def post(self, request):
        de_serialized_data = insert_serializer(data=request.data)
        if de_serialized_data.is_valid():
            print 'Data before save is'
            print de_serialized_data.validated_data
            de_serialized_data.save()
            print 'Data after save is'
            print de_serialized_data.data
        return Response(de_serialized_data.data)


def test_insertion(request):
    val = request.POST
    #pdb.set_trace()
    #return HttpResponse(json.loads(request.body))
    #data = JSONParser.parse(request.POST)
    #new_user = User(request.POST)
    logging.debug('Testing logging module')
    logging.debug(request.POST)

    de_serialized_data = insert_serializer(data=json.loads(request.body))
    #return HttpResponse(de_serialized_data)
    #pdb.set_trace()
    if de_serialized_data.is_valid():
        de_serialized_data.save()
        return HttpResponse("Success at last")
    return HttpResponse(de_serialized_data)
    print de_serialized_data.errors
    return HttpResponse(de_serialized_data.errors)
    return HttpResponse("Failure No success")
