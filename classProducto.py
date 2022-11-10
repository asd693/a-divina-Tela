
# Clase

class producto:

    # Atributos de clase 

    producto_id = 0;#PK TABLA PRODUCTO
    marca = "";#MARCA DEL PRODUCTO
    categoria = "";#CATEGORIA DEL PRODUCTO
    talla = "";#TALLA DEL PRODUCTO
    nombre = "";#NOMBRE DEL PRODUCTO
    unidades = "";#UNIDADES DEL PRODUCTO
    peso = "";#PESO DEL PRODUCTO
    precio = "";#PRECIO DEL PRODUCTO 
    foto = "";#FOTO DEL PRODUCTO 
    flag = True;#ESTADO ACTUAL DE LOS DATOS DEL PRODUCTO

    # Constructor
    def __init__(self,producto_id,marca,categoria, talla, nombre,unidades,peso,precio,foto,flag):
        self.producto_id = producto_id
        self.marca = marca
        self.categoria = categoria
        self.talla = talla
        self.nombre = nombre
        self.unidades = unidades
        self.peso = peso
        self.precio = precio
        self.foto = foto
        self.flag = flag

    def registrarProducto(self):
        pass

    def modificarProducto(self):
        pass

    def comprarProducto(self):
        pass

    def venderProducto(self):
        pass
