from flask import Flask, render_template, request
from random import randint 
from Actions import Action
from utilisateur import Utilisateur
from commande import Commande
from main import requeter

app = Flask(__name__)



@app.route("/")
def index():
    return render_template("accueil.html")

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/connecter')
def connecter():
    return render_template('connecter.html')

@app.route('/apropos')
def apropos():
    return render_template('apropos.html')


@app.route('/recherche', methods=['GET', 'POST']) 
def recherche():
    resultats = []
    requete  = ''
    
    if request.method == 'POST':
        requete = request.form.get('recherche', '')
        resultats = [
            {"titre": f"L'utilisateur a demandé : {requete} ==>  {requeter(requete)}"}
        ]
    
    return render_template("recherche.html", resultats=resultats, requete=requete)


  
if __name__ == '__main__':
    app.run(debug=True)
