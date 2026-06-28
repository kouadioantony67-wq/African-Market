from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(_name_)

# Le dictionnaire pour stocker les produits
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
        nom = request.form.get('nom')
        prix = request.form.get('prix')
        description = request.form.get('description')
        
        PRODUITS[prochain_id] = {
            'nom': nom,
            'prix': prix,
            'description': description
        }
        prochain_id += 1
        return redirect(url_for('boutique'))

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
                <…
