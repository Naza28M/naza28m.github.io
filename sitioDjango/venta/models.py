from django.db import models

# Create your models here.

class Producto (models.Model):
	name = models. CharField(max_length=200,verbose_name="Nombre")
	price=models.DecimalField(max_digits=9, decimal_places=2,verbose_name="Precio")
	description = models.TextField(verbose_name="Descripcion")
	image = models.ImageField(verbose_name="Imagen", upload_to = "productos")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name= "producto"
		verbose_name_plural= "productos"
		ordering =["-created"]

	def _str_ (self):
		return self.nombre