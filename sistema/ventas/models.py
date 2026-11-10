from django.db import models
#Se van a colocar las clases tambien conocidass como modelos.
# Create your models here

#Se requiere crar la clase Producto
class Producto(models.Model):
    categorias = [(1, "Tecnologia"),(2, "Hogar"),(3, "Alimentos"),(4, "Vestimenta"),(5, "Otros")]
    #definir atributos
    nombre = models.CharField(max_length=10)
    #cuando se requiera añadir atributos a una clase ya existente debemos utuilizar
    #BLANK Y NULL
    #BLANK = true, cuando queremos colocar campos que no sean obligatorios de llenar para el usuario
    precio = models.DecimalField(max_digits=10, decimal_places= 2, blank=True, null=True)
    stock = models.IntegerField(default=0, blank=True, null=True)

    descripcion = models.TextField(null=True)
    estado = models.BooleanField(default=True, null=True)
    categoria = models.IntegerField(choices=categorias, default=5)
    
    # SE REQUIERE CREAR UN CAMPLO LLAMADO CATEGORIAS PARA SELECCIONA EL TIPO DE PRODUCTO
    # REGISTROS, UTILICE/CHOICES
    
    def __str__(self):
        return f"{self.nombre} - {self.stock}"




