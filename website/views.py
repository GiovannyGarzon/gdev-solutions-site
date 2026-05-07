from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail


def home(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        correo = request.POST.get("correo")
        telefono = request.POST.get("telefono")
        servicio = request.POST.get("servicio")
        mensaje = request.POST.get("mensaje")

        asunto = f"Nueva solicitud desde G-DEV Solutions - {servicio}"

        cuerpo = f"""
Nueva solicitud desde la página web:

Nombre: {nombre}
Correo: {correo}
Teléfono: {telefono}
Servicio de interés: {servicio}

Mensaje:
{mensaje}
"""

        send_mail(
            asunto,
            cuerpo,
            "gdevsolutions10@gmail.com",
            ["gdevsolutions10@gmail.com"],
            fail_silently=False,
        )

        messages.success(request, "Tu solicitud fue enviada correctamente. Pronto te contactaremos.")
        return redirect("website:home")

    return render(request, "website/home.html")
