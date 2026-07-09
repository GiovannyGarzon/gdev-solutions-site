from django.shortcuts import render, redirect
from django.contrib import messages
import resend

resend.api_key = "re_NGWqaVyu_C3TvWq3fSkoL2BHPALy5vCN4"


def home(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        correo = request.POST.get("correo")
        telefono = request.POST.get("telefono")
        servicio = request.POST.get("servicio")
        mensaje = request.POST.get("mensaje")

        asunto = f"Nueva solicitud - {servicio}"

        contenido = f"""
        Nueva solicitud desde la web:

        Nombre: {nombre}
        Correo: {correo}
        Teléfono: {telefono}
        Servicio: {servicio}

        Mensaje:
        {mensaje}
        """

        resend.Emails.send({
            "from": "onboarding@resend.dev",
            "to": "gdevsolutions10@gmail.com",
            "subject": asunto,
            "text": contenido,
        })

        messages.success(
            request,
            "Tu solicitud fue enviada correctamente."
        )

        return redirect("/#contacto")

    return render(request, "website/home.html")

def apps(request):
    return render(request, 'website/apps.html')
