from django.shortcuts import render, redirect, get_object_or_404
from .models import Publicacion, Imagen, Video
from datetime import datetime


def noticias(request):
    # Si el usuario no es superusuario y está intentando acceder al formulario de subida (método POST), redirige
    if not request.user.is_superuser and request.method == 'POST':
        return redirect('noticias')

    if request.method == 'POST' and request.user.is_superuser:
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        fecha = request.POST.get('fecha')
        localizacion = request.POST.get('localizacion')
        
        imagenes = request.FILES.getlist('imagenes')
        videos = request.FILES.getlist('videos')
        
        # Crear la publicación
        publicacion = Publicacion.objects.create(
            titulo=titulo,
            descripcion=descripcion,
            fecha=fecha,
            localizacion=localizacion,
        )
        
        # Guardar las imágenes si existen
        if imagenes:
            for imagen in imagenes:
                Imagen.objects.create(publicacion=publicacion, imagen=imagen)
        
        # Guardar los videos si existen
        if videos:
            for video in videos:
                Video.objects.create(publicacion=publicacion, video=video)
        
        return redirect('noticias')
    
    # Obtener todas las publicaciones para mostrarlas en la plantilla
    publicaciones = Publicacion.objects.all().order_by('-fecha')
    
    # Pasar el valor de si el usuario es superusuario al contexto
    return render(request, 'noticias.html', {
        'publicaciones': publicaciones,
        'is_superuser': request.user.is_superuser
    })

def editar_publicacion(request, id):
    publicacion = get_object_or_404(Publicacion, id=id)
    
    if not request.user.is_superuser:
        return redirect('noticias')  # Solo superusuarios pueden acceder
    
    if request.method == 'POST':
        # Actualizar los campos de la publicación
        publicacion.titulo = request.POST.get('titulo')
        publicacion.descripcion = request.POST.get('descripcion')
        
        # Obtener la fecha sin necesidad de formateo
        fecha_str = request.POST.get('fecha')
        if fecha_str:
            publicacion.fecha = fecha_str  # Ya está en el formato correcto "yyyy-MM-dd"
        
        publicacion.localizacion = request.POST.get('localizacion')
        publicacion.save()
        
        # Manejar eliminación de imágenes y videos
        imagenes_eliminar = request.POST.getlist('imagenes_eliminar')
        videos_eliminar = request.POST.getlist('videos_eliminar')
        
        # Eliminar las imágenes seleccionadas
        if imagenes_eliminar:
            Imagen.objects.filter(id__in=imagenes_eliminar).delete()
        
        # Eliminar los videos seleccionados
        if videos_eliminar:
            Video.objects.filter(id__in=videos_eliminar).delete()
        
        # Agregar nuevas imágenes
        nuevas_imagenes = request.FILES.getlist('nuevas_imagenes')
        if nuevas_imagenes:
            for imagen in nuevas_imagenes:
                Imagen.objects.create(publicacion=publicacion, imagen=imagen)
        
        # Agregar nuevos videos
        nuevos_videos = request.FILES.getlist('nuevos_videos')
        if nuevos_videos:
            for video in nuevos_videos:
                Video.objects.create(publicacion=publicacion, video=video)
        
        return redirect('noticias')
    
    return render(request, 'editarPublicacion.html', {
        'publicacion': publicacion,
        'imagenes': publicacion.imagenes.all(),
        'videos': publicacion.videos.all(),
    })

def eliminar_publicacion(request, id):
    publicacion = get_object_or_404(Publicacion, id=id)
    
    if not request.user.is_superuser:
        return redirect('noticias')  # Solo superusuarios pueden eliminar

    if request.method == 'POST':
        # Eliminar la publicación
        publicacion.delete()
        return redirect('noticias')  # Redirige a la página de noticias después de eliminar

    # Si no es POST, redirige a la edición de la publicación
    return redirect('editar_publicacion', id=id)
