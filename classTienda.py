
# Clase Tienda

class tienda:

    # Atributos de clase:
    
    tienda_id = 0;#PK TABLA TIENDA
    nombre = "";#NOMBRE DE LA TIENDA
    nit = "";#NIT DE LA TIENDA
    direccion = "";#DIRECCION DE LA TIENDA
    email = "";#EMAIL DE LA TIENDA
    telefono = "";#TELEFONO DE LA TIENDA
    foto = "" #null;#FOTO DE LA TIENDA
    date = "" #null;#FECHA DE ULTIMA MODIFICACIÓN DE DATOS DE LA TIENDA
    flag = True;#ESTADO ACTUAL DE LOS DATOS DE LA TIENDA

    # Constructor 
    
    def __init__(self, tienda_id, nombre, nit, direccion, email, telefono, foto,date,flag):
        self.tienda_id = tienda_id;
        self.nombre = nombre
        self.nit = nit
        self.direccion = direccion
        self.email = email
        self.telefono = telefono
        self.foto = foto
        self.date = date
        self.flag = flag

        
