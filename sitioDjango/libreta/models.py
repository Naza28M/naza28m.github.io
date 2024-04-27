from django.db import models

# Create your models here.

class Receta (models.Model):
	name = models.CharField(max_length=200, verbose_name="Nombre")
	description = models.TextField(verbose_name="Descripcion")
	information = models.TextField(verbose_name="Informacion")
	image = models.ImageField(verbose_name="Imagen", upload_to = "recetas")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name= "receta"
		verbose_name_plural= "recetas"
		ordering =["-created"]

	def _str_ (self):
		return self.name