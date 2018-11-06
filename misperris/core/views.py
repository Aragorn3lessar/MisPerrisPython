from django.shortcuts import render
from .models import Estado,Mascota,Raza,Region,Ciudad,Socio,Vivienda,TipoUser
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
# Create your views here.

def logoutM(request):
    auth.logout(request)
    return render(request,'core/loginM.htm')

def loginM(request):
    if request.POST:
        usu=request.POST["txtRun"]
        pas=request.POST["txtPass"]
        user=auth.authenticate(username=usu,password=pas)
        if user is not None and user.is_active:
            auth.login(request,user)
            return render(request,'core/formularioM.htm',{'usuario':user.username})
        else:
            return render(request,'core/error.htm')

    return render(request,'core/loginM.htm')

def logoutS(request):
    auth.logout(request)
    return render(request,'core/loginS.htm')

def loginS(request):
    if request.POST:
        us=request.POST["txtRun"]
        pa=request.POST["txtPass"]
        use=auth.authenticate(username=us,password=pa)
        if use is not None and use.is_active:
            auth.login(request,use)
            return render(request,'core/formularioS.htm',{'usuario':use.username})
        else:
            return render(request,'core/error.htm')

    return render(request,'core/loginS.htm')


def index(request):
    return render(request,'core/home.htm')

def intermedio(request):
    return render(request,'core/intermedio.htm')


#recordar shois file
#file para imagenes

@login_required
def listarS(request):
    sos=Socio.objects.all()
    return render(request,'core/listarS.htm',{'socios':sos})
@login_required
def eliminarS(request):
    sos=Socio.objects.all()
    resp=False
    if request.POST:
        cod=request.POST.get("code","")
        so=Socio.objects.get(name=cod)
        so.delete()
        resp=True
    return render(request,'core/eliminarS.htm',{'socios':sos,'respuesta':resp})
@login_required
def formularioS(request):
    reg=Region.objects.all()
    ciu=Ciudad.objects.all()
    tivi=Vivienda.objects.all()
    tius=TipoUser.objects.all()
    resp=False
    if request.POST:
        rut=request.POST.get("txtRun","")
        correo=request.POST.get("txtCorreo","")
        nombre=request.POST.get("txtNombre","")
        fecha_n=request.POST.get("txtFecha","")
        telefono=request.POST.get("txtTelefono","")
        region=request.POST.get("cboRegion","")
        obj_reg=Region.objects.get(name=region) 
        ciudad=request.POST.get("cboCiudad","")
        obj_ciu=Ciudad.objects.get(name=ciudad)
        tipo_viv=request.POST.get("cboTipo","")
        obj_tip_viv=Vivienda.objects.get(name=tipo_viv)
        contrasena=request.POST.get("txtPass","")
        codeadmim=request.POST.get("txtCodeadmin","")
        if codeadmim=="0192837465":
            tipo_user=TipoUser.objects.get(name="admin")
        else:
            tipo_user=TipoUser.objects.get(name="socio")

        sos=Socio(
            name=rut,
            correo=correo,
            nombre=nombre,
            fecha_n=fecha_n,
            telefono=telefono,
            region=obj_reg,
            ciudad=obj_ciu,
            tipo_viv=obj_tip_viv,
            contrasena=contrasena,
            tipo_user=tipo_user,
        )
        us=User(
            username=rut,
            password=contrasena
        )
        us.save()
        sos.save()
        resp=True

    return render(request,'core/formularioS.htm',{'regiones':reg,'ciudades':ciu,'tipo_viviendas':tivi,'tipo_usuarios':tius ,'respuesta':resp})

@login_required
def modificar(request):
    mas=Mascota.objects.all()
    raz=Raza.objects.all()
    esta=Estado.objects.all()
    if request.POST:
        accion=request.POST.get("btnAccion","")
        mensaje=""
        if accion == "Buscar":
            code=request.POST.get("code","")
            ma=Mascota.objects.get(name=code)
            return render(request,'core/modificarM.htm',{'mascotas':mas,'razas':raz,'estados':esta,'ma':ma, 'mensaje':mensaje})
        if accion == "Modificar":
            code=request.POST.get("code","")
            ma=Mascota.objects.get(name=code)
            foto=request.POST.get("foto","")
            nombre=request.POST.get("nombre","")
            raza=request.POST.get("raza","")
            obj_raza=Raza.objects.get(name=raza) 
            desc=request.POST.get("desc","")
            est=request.POST.get("estado","")
            obj_estado=Estado.objects.get(name=est)
            ma.foto=foto
            ma.nombre=nombre
            ma.raza=obj_raza
            ma.descripcion=desc
            ma.estado=obj_estado
            ma.save()
            mensaje="actualizo"
            return render(request,'core/modificarM.htm',{'mascotas':mas,'razas':raz, 'estados':esta, 'mensaje':mensaje})
    return render(request,'core/modificarM.htm',{'mascotas':mas,'razas':raz,'estados':esta})

@login_required
def eliminar(request):
    mas=Mascota.objects.all()
    resp=False
    if request.POST:
        cod=request.POST.get("code","")
        ma=Mascota.objects.get(name=cod)
        ma.delete()
        resp=True
    return render(request,'core/eliminarM.htm',{'mascotas':mas,'respuesta':resp})

@login_required
def listar(request):
    mas=Mascota.objects.all()
    return render(request,'core/listar.htm',{'mascotas':mas})


def formulario(request):
    esta=Estado.objects.all()
    raz=Raza.objects.all()
    resp=False
    if request.POST:
        code=request.POST.get("code","")
        foto=request.POST.get("foto","")
        nombre=request.POST.get("nombre","")
        raza=request.POST.get("raza","")
        obj_raza=Raza.objects.get(name=raza) 
        desc=request.POST.get("desc","")
        est=request.POST.get("estado","")
        obj_estado=Estado.objects.get(name=est)
        mas=Mascota(
            name=code,
            foto=foto,
            nombre=nombre,
            raza=obj_raza,
            estado=obj_estado,
            descripcion=desc,

        )
        mas.save()
        resp=True

    return render(request,'core/formularioM.htm',{'estado':esta,'raza':raz,'respuesta':resp})

def error_accesoM(request):
    return render(request,'core/error_accesoM.htm')