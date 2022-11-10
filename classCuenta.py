class cuenta:

    # Atributos de clase

    identi_id = 0;#PK TABLA IDENTIFICADOR
    cliente_id = 0;#PK TABLA CLIENTE
    usuario_id = 0;#PK TABLA CUENTA USUARIO
    cuentabool_id = 0;#PK TABLA CUENTADATOS BOOL
    cuenta = "";#NOMBRE DE CUENTA
    passw = "";#CONTRASEÑA DE CUENTA
    foto = "" #null;#FOTO DE CUENTA
    flag = True;#ESTADO ACTUAL DE LOS DATOS DE LA CUENTA

    def __init__(self,identi_id,cliente_id,usuario_id,cuentabool_id,cuenta,passw,foto,flag):
        self.identi_id = identi_id
        self.cliente_id = cliente_id
        self.usuario_id = usuario_id
        self.cuentabool_id = cuentabool_id
        self.cuenta = cuenta
        self.passw = passw
        self.foto = foto
        self.flag = flag


    def loginCuenta (self):
        print("HOLA AMIGO")
        pass

    def crearCuenta (self):
        pass

    def eliminarCuenta(self):
        pass

    def modificarCuenta(self):
        pass


    
