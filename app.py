from flask import Flask 

from flask import render_template, request, redirect, Response, url_for, session
from flask_mysqldb import MySQL
from flask_cors import CORS
import config as db

#from flask_bootstrap import Bootstrap
app = Flask(__name__)
app.secret_key = 'supersecretkey'

#aca cargamos datos del la db sql
#pp.config['MYSQL_HOST'] = config.MYSQL_HOST
#app.config['MYSQL_USER'] = config.MYSQL_USER
#app.config['MYSQL_PASSWORD'] = config.MYSQL_PASSWORD
#app.config['MYSQL_DB'] = config.MYSQL_DB
#app.config["MYSQL_CURSORCLASS"] = "DictCursor"



#mysql = MySQL(app)

#cur = mysql.connection.cursor()
#Bootstrap(app)



#app = Flask(__name__)
#app.json.ensure_ascii = False





@app.route('/',methods=['GET'])
def home():
    return render_template('iniciarSesion.html')


@app.route('/index',methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/iniciarSesion',methods=['GET'])
def iniciarSesion():
    if session['inisesion']== 'Cerrar Sesion':
        session['inisesion']= 'Iniciar Sesion' 
        session['registrarse']='Registrarse'
    return render_template('iniciarSesion.html')

@app.route('/contactanos',methods=['GET'])
def contactanos():
    return render_template('contactanos.html')


@app.route('/registrar',methods=['GET'])
def registrar():
    if session['registrarse']=='Perfil':
        return render_template('perfil.html')
    else:
        return render_template('registrar.html')


@app.route('/sucursales',methods=['GET'])
def sucursales():
    return render_template('sucursales.html')


@app.route('/productos',methods=['GET'])
def productos():
    return render_template('productos.html')


@app.route('/perfil',methods=['GET'])
def perfil():
    return render_template('perfil.html')


#@app.route('/acceso-login',methods=['GET','POST'])
#def login():
#    if request.method == 'POST' and 'txtCorreo' in request.fom and 'txtPassword' in request.form

#        _correo= request.form['txtCorreo']  
#        _password= request.form['txtPassword']  
#    return render_template('perfil.html')

@app.route('/acceso-login', methods= ["GET", "POST"])
def login():
   
    if request.method == 'POST' and 'txtCorreo' in request.form and 'txtPassword' in request.form:
       
        _correo = request.form['txtCorreo']
        _password = request.form['txtPassword']
        cur = db.database.cursor()

        
        
        cur.execute('SELECT * FROM cuenta WHERE correo = %s AND clave = %s', (_correo, _password,))
        account = cur.fetchone()
        

        cur.close()
        if account:
            session['usuario'] = _correo
            session['inisesion']= 'Cerrar Sesion'   
            session['registrarse']='Perfil'
            #session['logueado'] = True
            #session['id'] = account['id']
            
            return render_template("productos.html")
        else:
            session['inisesion']= 'Iniciar Sesion'
            session['registrarse'] 
            return render_template('iniciarSesion.html',mensaje="Usuario O Contraseña Incorrectas")
    return render_template('iniciarSesion.html',mensaje="Usuario o contraseña incorrectas")


@app.route('/nuevo-usuario', methods= ["GET", "POST"])
def nueuser():
    print(request.form['mail'])

    if request.method == 'POST' and 'mail' in request.form and 'txtClave' in request.form and 'txtClave2' in request.form:
       
        _correo = request.form['mail']
        _password = request.form['txtClave']
        _password2 = request.form['txtClave2']
        cur = db.database.cursor()

        
        if _password == _password2:
            cur.execute('INSERT INTO cuenta ( correo, clave) VALUES (%s, %s)', (_correo, _password))
            db.database.commit()
            cur.close()
            #account = cur.fetchone()
      
        #if account:
            #session['logueado'] = True
            #session['id'] = account['id']

            return render_template("productos.html")
        #else:
         #   return render_template('registrar.html',mensaje="Usuario O Contraseña Incorrectas")







if __name__ == "__main__":
    app.run(debug=True)