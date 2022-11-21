from flask import Flask,render_template


app = Flask(__name__)

@app.route('/play')
@app.route('/play/<int:num>')
@app.route('/play/<int:num>/<color>')
def play(num=3,color='#9fc5f8'):
    #num = int(num)
    return render_template("index.html", num = num,color=color)  # Devuelve la cadena '¡Hola Mundo!' como respuesta



if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente  
    app.run(debug=True)