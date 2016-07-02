"""Django views."""
from django.shortcuts import render_to_response, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.template import RequestContext
from .models import Student

# Create your views here.


class Index(View):
    """Home page for AtaOnline."""

    def get(self, request):
        """Index."""
        if request.user.is_authenticated():
            respond_view = render_to_response('index.html')
        else:
            respond_view = render_to_response(
                'login.html', context_instance=RequestContext(request))
        return respond_view


class Login(View):
    """This class will define every method that has login in."""

    http_method_names = [u'get', u'post']

    def post(self, request):
        """Loggin method."""
        request_username = request.POST['username']
        request_password = request.POST['password']

        user = authenticate(username=request_username,
                            password=request_password)
        if user:
            if user.is_active:
                login(request, user)
                respond_view = redirect('/')
            else:
                respond_view = render_to_response('UserOff.html')
        else:
            respond_view = render_to_response('create_user.html')

        return respond_view

    def get(self, request):
        """Get Method for Login."""
        return render_to_response(
            'login.html', context_instance=RequestContext(request))


class Logout(View):
    """Class to access method to log out a user."""

    http_method_names = [u'get', u'post']

    def get(self, request):
        """Logout post access method."""
        # user = authenticate(username=req_username, password=req_password)
        logout(request)
        return redirect('login')


class SignUp(View):
    """Create user Professor or Student."""

    http_method_names = [u'get', u'post']

    def post(self, request):
        """Get all information and creat a user."""
        request_username = request.POST['username']
        request_password = request.POST['password']
        request_first_name = request.POST['first_name']
        request_number_id = request.POST['registration']
        request_email = request.POST['email']

        new_student = Student()
        new_student.username = request_username
        new_student.set_password(request_password)
        new_student.first_name = request_first_name
        new_student.student_registration = request_number_id
        new_student.email = request_email

        new_student.save()

        return redirect('login')
        # render(request, 'login.html', {})

    def get(self, request):
        """Get method for CreateUser."""
        return render_to_response(
            'create_user.html', context_instance=RequestContext(request))
