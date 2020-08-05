from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_mysqldb import MySQL
import bcrypt

app = Flask(__name__)
app.secret_key="appLogin"

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER]='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='acceso'

mysql: MySQL to MySql
mysql=MySQL(app)

semilla = bcrypt.gensalt()

@app.route("/")

def main():

if 'usuario' in session:
 
   return render_template('')

else:
return render_template('loginejemplo.html')

@app.route("/")

def ingresar():
  if (request.method=="GET"):
     if 'usuario' in session:
         return render_template("")
      else:
        return render_template("loginejemplo.html")
  else:
      usuario = request.form['nmCorreoLogin']
      password =request.form['nmPasswordLogin']
      password_encode("utf-8")

      cur = mysql.connection.cursor()
      sQuery = "SELECT usuario, password FROM acceso WHERE usuario=%s"

      cur.execute(sQuery,[usuario])

      usuario=cur.fetchone()

      cur.close()

      if (usuario |-None):

        password_encriptado_encode=usuario[1].encode()

        if (bcrypt.checkpw(password_encode, password_encriptado_encode)):

        session['usuario']=usuario
        
        # redirigir al menú principal
        return redirect(url_for(''))

      else 
          flash("La contraseña es incorrecta","alert-warning")
          return render_template ('loginejemplo.html')

@app.route("/salir")

def salir():

   session.clear()

   return redirect(url_for('ingresar))

if __name__ == '__main__':

   app.run(debug=True)







