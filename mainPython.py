from flask import Flask, render_template, request
import pyodbc

#Base de datos
server = "DESKTOP-NHE6VVQ\SQLEXPRESS"
bd = "Prueba"
usuarioBD = "MaxSQLserver"
password = "1590SQLs"


# Conexion e insertar a la base de datos sqlserver
def insertar(user,passw):
    cursorIns = conexion.cursor()
    consulta = "use Login insert into usuario (usuario,password) values('"+user+"','"+passw+"')"
    cursorIns.execute(consulta)
    cursorIns.commit()
    cursorIns.close()
    print("Insercion exitosa")
    
try:
    conexion = pyodbc.connect("DRIVER={SQL Server}; SERVER=" + server + "; DATABASE = "
    + bd + "; UID="+usuarioBD+"; PWD="+password)
    print("Conexion exitosa")

except Exception as ex:
    print(ex)


# Flask

app = Flask(__name__)

# Cargamos el template html
@app.route("/")
def template():
    
    return render_template("index.html")


# Cargamos la funcionalidad para la base de datos
@app.route("/",methods=["GET","POST"])
def usuario():
    nombreUser = request.form["usuario"]
    passwUser = request.form["passwordV"]

    print (nombreUser)
    print (passwUser)
    insertar(nombreUser,passwUser)
    return render_template("index.html")
    #return  nombreUser, apellidoUser



if __name__ == "__main__":
    app.run(debug=True)
