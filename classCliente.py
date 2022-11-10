
# Clase cliente

class cliente:

    # Atributos de clase
    identi_id = 0;#PK TABLA IDENTIFICADOR
    persona_id = 0;#PK TABLA PERSONA
    cliente_id = 0;#PK TABLA CLIENTE_BOOL
    infoPago_id = 0;#PK TABLA METODOS PAGO
    tipoPersona = True;#BOOLEANO IDENTIFICADOR SI CLIENTE ES PERSONA U ORGANIZACION
    municipio_id = 0;#FK TABLA MUNICIPIOS
    nombre = "";#NOMBRE DE CLIENTE
    NIT = "";#CI DEL CLIENTE
    genero = True;#GENERO DEL CLIENTE
    direccion = "";#DIRECCION DEL CLIENTE
    telefono = "";#TELEFONO DEL CLIENTE
    email = "";#EMAIL DEL CLIENTE
    #Blob foto = null;#FOTO DEL CLIENTE
    #Date fechaNacimiento = null;#FECHA NACIMIENTO CLIENTE
    flag = True;#FLAG CONTROLADOR DE ESTADO DATOS ACTUALES CLIENTE
    nombreEmpresa = "";#NOMBRE DE EMPRESA DE MÉTODO DE PAGO UTILIZADO POR EL CLIENTE
    codigo = "";#CODIGO DE SEGURIDAD DEL METODO DE PAGO
    #date fechaVencimiento = null;#FECHA DE VENCIMIENTO DE METODO DE PAGO
    flagMetodoPago = True;#ESTADO ACTUAL DEL METODO DE PAGO DENTRO DE LA BASE DE DATOS
    
    
    # Constructor 

    def __init__(self,identi_id,persona_id,cliente_id,infoPago_id,tipoPersona,municipio_id,nombre,nit, genero,direccion,telefono,email,flag,
        nombreEmpresa,codigo,flagMetodoPago):

        self.identi_id = identi_id
        self.persona_id = persona_id
        self.cliente_id = cliente_id
        self.infoPago_id = infoPago_id
        self.tipoPersona = tipoPersona
        self.municipio_id = municipio_id
        self.nombre = nombre
        self.NIT = nit
        self.genero = genero
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.flag = flag
        self.nombreEmpresa = nombreEmpresa
        self.codigo = codigo
        self.flagMetodoPago = flagMetodoPago

    # Metodos de clase

    def registrarMetodoPago (self):
        print("HOLA AMIGO")
        pass

    def modificarDatosCliente(self):
        pass

    def cambiarMetodoDePago (self):
        pass

    def eliminarMetodoDePago (self):
        pass
