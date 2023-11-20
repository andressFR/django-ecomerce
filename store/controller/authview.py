from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from store.form import CustomUserForm


#pagina de formulario de registro
def register(request):
    #objeto de la clase CustomUserForm
    form = CustomUserForm()

    #validamos si se utiliza el metodo POST
    if request.method == 'POST':
        #objeto de la clase CustomUserForm
        form = CustomUserForm(data=request.POST)

        #valida el formulario
        if form.is_valid():
            #Guarda el formulario en la base de datos
            form.save()

            messages.success(request,'Registro Completado')

            #Redirecciona a la pagina de inicio de sesion
            return redirect('loginpage')

        """else:
            messages.error(request,"Error")"""

    context = {'form':form}
    return render(request, 'store/auth/register.html',context)

#pagina de inicio de sesion
def loginpage(request):
    #verifica si el usuario ya inicio sesion. En caso de ya estar registrado reddirecionara a la 
    #pagina de inicio
    if request.user.is_authenticated:
        messages.warning(request, 'Ya has iniciado sesion')
        return redirect('home')
    
    else:
        #Verifica que el metodo de envio sea POST
        if request.method == 'POST':
            #Obtiene los daros de los input (atributo name)
            name = request.POST.get('username')
            passwd = request.POST.get('password')

            #autentica el usuario
            user = authenticate(request, username=name, password=passwd)

            #Verifica si el usuario ya esta registrado
            if user is not None:
                login(request, user) 
                messages.success(request, 'Inicio de Sesion Exitoso')
                return redirect('/')

            else:
                messages.error(request,'Usuario o contraseña incorrecto')
                redirect('loginpage')
        return render(request, 'store/auth/login.html')
    
#funcion para cerrar sesion
def logoutpage(request):
    #verifica si el usuario ya inicio sesion.
    if request.user.is_authenticated:

        #cierra la sesion
        logout(request)
        messages.success(request, 'Has cerrado sesion exitantosamente')

        #redirecciona a la pagina de inicio
        return redirect('home')