"""Django views."""
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.template import RequestContext
from .models import Student, Notebook, Professor
from django.db.models.signals import post_save
from django.dispatch import receiver
from pdfConverter.views import PdfConverter
# Create your views here.


class Index(View):
    """Home page for AtaOnline."""

    def get(self, request):
        """Index."""
        if request.user.is_authenticated():
            notebooks = Notebook.objects.all()
            respond_view = render_to_response(
                'index.html',
                {'notebooks': notebooks}, RequestContext(request))
        else:
            respond_view = render_to_response(
                'login.html', context_instance=RequestContext(request))
        return respond_view


class Login(View):
    """This class will define every method that has login in."""

    http_method_names = [u'get', u'post']

    @receiver(post_save, sender=Notebook)
    def update_stock_atas(sender, instance, **kwargs):
        print('Sinal foi Salvo!')

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


class SignUpStudent(View):
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
            'create_student.html', context_instance=RequestContext(request))


class SignUpTeacher(View):
    """Create user Professor or Student."""

    http_method_names = [u'get', u'post']

    def post(self, request):
        """Get all information and creat a user."""
        request_username = request.POST['username']
        request_password = request.POST['password']
        request_first_name = request.POST['first_name']
        request_number_id = request.POST['registration']
        request_formation = request.POST['formation']
        request_email = request.POST['email']

        new_teacher = Professor()
        new_teacher.username = request_username
        new_teacher.set_password(request_password)
        new_teacher.first_name = request_first_name
        new_teacher.professor_registration = request_number_id
        new_teacher.formation = request_formation
        new_teacher.email = request_email

        new_teacher.save()

        return redirect('login')
        # render(request, 'login.html', {})

    def get(self, request):
        """Get method for CreateUser."""
        return render_to_response(
            'create_professor.html', context_instance=RequestContext(request))


class Ata(View):
    """Class to use for ata manipulation."""

    def get(self, request):
        """Start template of create Ata."""
        if request.user.is_authenticated():
            respond_view = render_to_response(
                'create_ata.html', context_instance=RequestContext(request))
        else:
            respond_view = render_to_response(
                'login.html', context_instance=RequestContext(request))
        return respond_view

    def post(self, request):
        """Get ata informations to save."""
        user = request.user
        title = request.POST['title']
        date = request.POST['date']
        content = request.POST['content']

        new_notebook = Notebook()
        new_notebook.user = user
        new_notebook.title = title
        new_notebook.date = date
        new_notebook.content = content

        new_notebook.save()

        return redirect('index')


class Convertion(PdfConverter, View):
    """Clas that uses pdf convertion plugin."""

    def post(self, request):
        """Function that will convert"""
        user = request.user
        title = request.POST['title']
        date = request.POST['date']
        content = request.POST['content']

        new_notebook = Notebook()
        new_notebook.user = user
        new_notebook.title = title
        new_notebook.date = date
        new_notebook.content = content

        data_pass = {'ata': new_notebook}

        return self.convert(
            "ata_to_pdf.html", "ata " + title + ".pdf", data_pass)
