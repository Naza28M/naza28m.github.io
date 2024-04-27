from django.db import models

# Create your models here.

class Proyecto (models.Model):
	name = models. CharField(max_length=200, verbose_name="Nombre")
	description = models.TextField(verbose_name="Descripcion")
	webside = models.URLField (verbose_name="Url", null=True, blank=True)
	image = models.ImageField(verbose_name="Imagen", upload_to = "proyectos")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name= "proyecto"
		verbose_name_plural= "proyectos"
		ordering =["-created"]

	def _str_ (self):
		return self.name
