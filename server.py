from flask import Flask, render_template , request


App = Flask(__name__, template_folder="./src/views")

@App.route("/", methods=['GET']) # por padrão methods já é get methods=['GET'], aceita também mais de um verbo ex, methods=['GET', 'POST'] 
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        return "<h1>Pagina não econtrada</h1>"

@App.route("/", methods=['GET','POST']) # "/<multiplicar>" entre chaves recebe query params, /<int:multiplicar>" já retorna o numero como inteiro tudo via GET
def calcular():
    dados = request.form
    primeiro = int(dados['primeiro'])
    segundo = int(dados['segundo'])
    calc = primeiro * segundo    
    return f"<h1>A Multiplicação de {primeiro} x {segundo} é  {calc}</h1> "  ## pode retornar um soma str(int(<query>) + 1) dessa maneira

@App.errorhandler(404)
def not_found(erro):
    return render_template("erro.html")
  
    


    






App.run(port=5050, debug=True)