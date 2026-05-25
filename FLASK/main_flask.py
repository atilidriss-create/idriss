from flask import Flask, render_template, request
from random import randint 
from Actions import Action
from utilisateur import Utilisateur
from commande import Commande
from connect import connecter


app = Flask(__name__)




@app.route('/')
def index():
    
    return render_template("accueil.html")
    


@app.route("/recherche", methods=['GET', 'POST']) 
def recherche():
    resultats = []
    requete  = ''
    
    if request.method == 'POST':
        requete = request.form.get('recherche', "")
        resultats = [
            {"titre": f"L'utilisateur a demandé : {requete} ==>  {connecter(requete)}"}
        ]
    return render_template("recherche.html", resultats=resultats, requete=requete)



@app.route('/connexion', methods=['GET', 'POST'])
def connexion():
    if request.method == 'POST':
        nom_utilisateur = request.form.get('nom_utilisateur')
        mot_de_passe = request.form.get('mot_de_passe')
        
    
    return render_template('connexion.html')


@app.route('/inscription', methods=['GET', 'POST'])
def inscription():
    if request.method == 'POST':
        nom = request.form.get('nom')
        prenom = request.form.get('prenom')
        nom_utilisateur = request.form.get('nom_utilisateur')
        email = request.form.get('email')
        mot_de_passe = request.form.get('mot_de_passe')
        utilisateur = Utilisateur(nom, prenom, nom_utilisateur, email, mot_de_passe)
        utilisateur.inscription(nom, prenom, nom_utilisateur, email, mot_de_passe)
    return render_template("inscription.html")
    


@app.route("/informations")
def informations():
    return render_template("informations.html")




if __name__ == '__main__':
    app.run(debug=True)
    
    
