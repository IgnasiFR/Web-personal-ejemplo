from django.db import models

# Create your models here.

#Esta clase va a representar una tabla dentro de la base de datos
class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name= 'Título')  
    description = models.TextField(verbose_name= 'Descripción')
    image =  models.ImageField(verbose_name= 'Imágen', upload_to='projects')
    informacion = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name= 'Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name= 'Fecha de modificación')

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['-created']

    def __str__(self):
        return self.title
