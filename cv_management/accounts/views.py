from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Verificar si el usuario es un docente (podemos usar un grupo o permisos)
            if user.groups.filter(name='Docente').exists():
                login(request, user)
                return redirect('docente_dashboard')  # Redirigir al dashboard de docentes
            else:
                messages.error(request, 'No tienes permiso para acceder como docente.')
        else:
            messages.error(request, 'Credenciales inválidas.')
            
    return render(request, 'accounts/login.html')
