from django.shortcuts import render
from django.core.mail import EmailMessage
from django.templatetags.static import static
from django.template.loader import render_to_string
from django.http import HttpResponse

def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        asunto = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')

        if nombre and correo and asunto and mensaje:
            # Contenido del correo en HTML
            email_body = render_to_string('enviarEmail.html', {
                'nombre': nombre,
                'correo': correo,
                'asunto': asunto,
                'mensaje': mensaje,
            })

            email = EmailMessage(
                subject=asunto,
                body=email_body,
                from_email=correo,
                to=['psimultaneo@gmail.com'],
            )
            email.content_subtype = "html"
            email.send(fail_silently=False)

            return HttpResponse('¡Gracias por contactarnos!')
        else:
            return HttpResponse('Por favor, completa todos los campos.')

    return render(request, 'contacto.html')
