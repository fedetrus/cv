from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os

# TECNOLOGIAS #####################################
class Technology(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/')
    nro_orden = models.PositiveSmallIntegerField(editable=True)  # Editable y no único
    status = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.nro_orden:  # Si el nro_orden no está asignado, le da el siguiente número
            last_order = Technology.objects.order_by('-nro_orden').first()
            self.nro_orden = (last_order.nro_orden + 1) if last_order else 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
@receiver(post_delete, sender=Technology)
def delete_technology_logo(sender, instance, **kwargs):
    """ Elimina el archivo de la carpeta media cuando se borra una tecnología """
    if instance.logo:
        if os.path.isfile(instance.logo.path):
            os.remove(instance.logo.path)

@receiver(post_delete, sender=Technology)
def reorder_nro_orden(sender, instance, **kwargs):
    """ Reordena los números de orden después de eliminar una tecnología """
    technologies = Technology.objects.order_by('nro_orden')
    for index, tech in enumerate(technologies, start=1):
        if tech.nro_orden != index:
            tech.nro_orden = index
            tech.save()
##############################################################

# PROYECTOS #####################################
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    nro_orden = models.PositiveSmallIntegerField(editable=True)  # Editable y no único
    status = models.BooleanField(default=True)
    inicio = models.DateField()
    technologies = models.ManyToManyField('Technology', related_name='projects')  # Relación muchos a muchos

    def save(self, *args, **kwargs):
        if not self.nro_orden:  # Si el nro_orden no está asignado, le da el siguiente número
            last_order = Project.objects.order_by('-nro_orden').first()
            self.nro_orden = (last_order.nro_orden + 1) if last_order else 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return f"Imagen de {self.project.title}"
    
@receiver(post_delete, sender=Project)
def delete_technology_logo(sender, instance, **kwargs):
    """ Elimina el archivo de la carpeta media cuando se borra una tecnología """
    if instance.logo:
        if os.path.isfile(instance.logo.path):
            os.remove(instance.logo.path)

@receiver(post_delete, sender=Project)
def reorder_nro_orden(sender, instance, **kwargs):
    """ Reordena los números de orden después de eliminar una tecnología """
    technologies = Project.objects.order_by('nro_orden')
    for index, tech in enumerate(technologies, start=1):
        if tech.nro_orden != index:
            tech.nro_orden = index
            tech.save()
##############################################################

# EXPERIENCIA LABORAL #####################################
class Trabajo(models.Model):
    empresa = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=255)
    inicio = models.DateField()
    fin = models.DateField(null=True, blank=True)

    def anio_inicio(self):
        return self.inicio.year

    def anio_fin(self):
        return self.fin.year if self.fin else "Actualidad"

    def __str__(self):
        return f"{self.empresa} ({self.ubicacion})"

class Puesto(models.Model):
    trabajo = models.ForeignKey(Trabajo, on_delete=models.CASCADE, related_name='puestos')
    nombre = models.CharField(max_length=255)
    inicio = models.DateField()
    fin = models.DateField(null=True, blank=True)
    descripcion = models.CharField(max_length=300, blank=True)

    class Meta:
        ordering = ['-inicio']

    def anio_inicio(self):
        return self.inicio.year

    def anio_fin(self):
        return self.fin.year if self.fin else "Actualidad"

    def __str__(self):
        return f"{self.nombre} en {self.trabajo.empresa}"
##############################################################

# Académico #####################################
class Academia(models.Model):
    nombre = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=255)
    inicio = models.DateField()
    fin = models.DateField(null=True, blank=True)

    def anio_inicio(self):
        return self.inicio.year

    def anio_fin(self):
        return self.fin.year if self.fin else "Actualidad"

    def __str__(self):
        return f"{self.nombre} ({self.ubicacion})"

class Carrera(models.Model):
    academia = models.ForeignKey(Academia, on_delete=models.CASCADE, related_name='carreras')
    nombre = models.CharField(max_length=255)
    inicio = models.DateField()
    fin = models.DateField(null=True, blank=True)
    descripcion = models.CharField(max_length=300, blank=True)

    class Meta:
        ordering = ['-inicio']

    def anio_inicio(self):
        return self.inicio.year

    def anio_fin(self):
        return self.fin.year if self.fin else "Actualidad"

    def __str__(self):
        return f"{self.nombre} en {self.academia.nombre}"
##############################################################