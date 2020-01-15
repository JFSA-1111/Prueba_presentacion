from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test

from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

# Vistas = Listar y crear
from django.views.generic import ListView, CreateView, UpdateView, FormView

# Exception
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User

# Forms

from usuario.forms import SignupForm, PerfilForm
from usuario.models import Perfil
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash


def login_view(request):
    """Login view."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)

            return redirect('usuario:perfil')

        else:
            return render(request, 'users/login.html', {'error': 'Usuario y/o contraseña invalido'})

    return render(request, 'users/login.html')


def perfil(request):
    return render(request, 'users/perfil.html')


class PerfilCreateView(FormView):
    template_name = 'users/perfil.html'
    form_class = PerfilForm
    success_url = reverse_lazy('usuario:listar_usuario')

class UserCreateView(FormView):

    template_name = 'users/usuario_nuevo.html'
    form_class = SignupForm
    success_url = reverse_lazy('usuario:listar_usuario')

    def form_valid(self, form):
        """Guardar datos."""
        form.save()
        return super().form_valid(form)

@login_required
def cambio_contrasena(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Tu contrasena ha sido cambiada!')
            return redirect('usuario:logout')
        else:
            messages.error(request, 'Por favor corrija el error a continuación.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/nuevaContrasena.html', {
        'form': form
    })




@login_required
def logout_view(request):
    """Logout a user."""
    logout(request)
    return redirect('usuario:login')


"""@login_required
def listar_usuario(request):
    array = Perfil.objects.all()
    if array:
        contexto = {'lista': array}
        return render(request, 'users/listar.html', contexto)
    return render(request, 'users/listar.html', {'error': 'No hay datos'})"""


class listar_usuario(ListView):

    model = Perfil
    template_name = 'users/listar.html'
    queryset = Perfil.objects.filter(usuario__is_superuser=False)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Perfil.objects.all()
        else:
            return Perfil.objects.filter(usuario__is_superuser=False)



# @user_passes_test(lambda u:u.is_staff, login_url=('perfil'))
@login_required
def deshabilitar(request):

    if request.method == 'POST':
        pk = request.POST.get('')
        django = User.objects.get(pk=request.user.pk)

        if django.is_active:
            django.is_active = False
            django.save()
        else:
            django.is_active = True
            django.save()

    url = reverse('usuario:listar_usuario')

    return redirect(url)

