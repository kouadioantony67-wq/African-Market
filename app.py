from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(_name_)

# Le dictionnaire qui stocke temporairement les produits
PRODUITS = {}
prochain_id = 1

@app.route('/')
def boutique():
    html_page = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>African Market</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; background-color: #f4f4f4; }
            .header-bar { display: flex; justify-content: space-between; align-items: center; background-color: #333; color: white; padding: 10px 20px; }
            .panier-btn { background-color: #ff9900; color: white; padding: 10px; text-decoration: none; font-weight: bold; }
            .ajouter-btn { display: inline-block; background-color: #28a745; color: white; padding: 10px 20px; text-decoration: none; margin: 20px 0; font-weight: bold; }
            .produits-container { display: flex; flex-wrap: wrap; }
            .produit-card { background: white; padding: 15px; margin: 10px; border: 1px solid #ddd; width: 200px; }
            .voir-lien { color: #007bff; text-decoration: none; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="header-bar">
            <h1>African Market</h1>
            <a href="#" class="panier-btn" onclick="alert('Le panier est vide')">Mon Panier</a>
        </div>

        <a href="/ajouter" class="ajouter-btn">Mettre un produit en vente</a>
        <hr style="margin-top: 20px; border: 0; border-top: 1px solid #ccc;">

        {% if not produits %}
            <p style="color: #666; font-style: italic; margin-top: 30px;">Aucun produit n'est en vente pour le moment.</p>
        {% else %}
            <div class="produits-container">
            {% for id, prod in produits.items() %}
                <div class="produit-card">
                    <h3>{{ prod.nom }}</h3>
                    <p><strong>Prix :</strong> {{ prod.prix }} FCFA</p>
                    <a href="#" class="voir-lien">Voir le produit</a>
                </div>
            {% endfor %}
            </div>
        {% endif %}
    </body>
    </html>
    """
    return render_template_string(html_page, produits=PRODUITS)

@app.route('/ajouter', methods=['GET', 'POST'])
def ajouter_produit():
    global prochain_id
    if request.method == 'POST':
        # On recupere les infos tapees par l'utilisateur
        nom = request.form.get('nom')
        prix = request.form.get('prix')
        description = request.form.get('description')
        
        # On enregistre dans notre dictionnaire
        PRODUITS[prochain_id] = {
            'nom': nom,
            'prix': prix,
            'description': description
        }
        prochain_id += 1
        
        # Une fois ajoute, on redirige vers la page d'accueil
        return redirect(url_for('boutique'))

    # Si c'est une requete normale (GET), on affiche le formulaire HTML
    form_page = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Ajouter un produit - African Market</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f4f4; }
            .form-box { background: white; padding: 25px; border-radius: 5px; max-width: 400px; margin: auto; box-shadow: 0px 0px 10px rgba(0,0,0,0.1); }
            h2 { color: #333; margin-top: 0; }
            label { display: block; margin-top: 15px; font-weight: bold; }
            input, textarea { width: 100%; padding: 8px; margin-top: 5px; box-sizing: border-box; border: 1px solid #ccc; border-radius: 4px; }
            .btn-valider { background-color: #28a745; color: white; padding: 10px 15px; border: none; margin-top: 20px; width: 100%; cursor: pointer; font-size: 16px; font-weight: bold; }
            .btn-retour { display: block; text-align: center; margin-top: 15px; color: #555; text-decoration: none; }
        </style>
    </head>
    <body>
        <div class="form-box">
            <h2>Mettre un article en vente</h2>
            <form method="POST">
                <label>Nom du produit :</label>
                <input type="text" name="nom" required placeholder="Ex: Chaussures, Sac...">

                <label>Prix (FCFA) :</label>
                <input type="number" name="prix" required placeholder="Ex: 15000">

                <label>Description :</label>
                <textarea name="description" rows="4" placeholder="Decrivez votre produit..."></textarea>

                <button type="submit" class="btn-valider">Publier le produit</button>
            </form>
            <a href="/" class="btn-retour">Annuler et retourner a la boutique</a>
        </div>
    </body>
    </html>
    """
    return render_template_string(form_box=form_page) # Petite correction ici pour l'affichage simple

if _name_ == '_main_':
    app.run(debug=True)
