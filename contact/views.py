from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import JsonResponse
from django.contrib import messages
import sweetify

# Create your views here.
def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        
        # validar campos
        if not name or not email or not subject or not message:
            messages.error(request, "Todos los campos son obligatorios")
            return render(request, "contact.html")

        # Mensaje a enviar
        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        
        try:
            send_mail(
                subject,
                full_message,
                "pactumlawfirm@gmail.com",  # Reemplaza con tu correo Gmail
                ["pactumlawfirm@gmail.com"],  # Reemplaza con el correo receptor
                fail_silently=False,
            )
            # Mostrar mensaje Sweetify y redirigir
            sweetify.success(request, 'Mensaje enviado correctamente. Lo contactaremos pronto.', icon="success")
            return redirect("contact")
        
        except Exception as e:
            sweetify.error(request, f"Hubo un error: {str(e)}", icon="error")
            return redirect("contact")

    return render(request, "contact.html")