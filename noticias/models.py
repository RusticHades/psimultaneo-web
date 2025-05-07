from django.db import models

# Modelo de Publicación
class Publicacion(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha = models.DateField()
    localizacion = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo

# Modelo de Imagen
class Imagen(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"Imagen de {self.publicacion.titulo}"

# Modelo de Video
class Video(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name='videos')
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return f"Video de {self.publicacion.titulo}"
