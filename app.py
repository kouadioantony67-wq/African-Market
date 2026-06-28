from flask import Flask, render_template_string

app = Flask(_name_)

# Le dictionnaire est vide au depart! C'est l'utilisateur qui va le remplir.
PRODUITS = {}
# Un compteur pour donner un identifiant unique (1,2,3...) a chaque produit
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
                    <a href="/produit/{{ id }}" class="voir-lien">Voir le produit</a>
                </div>
            {% endfor %}
            </div>
        {% endif %}

    </body>
    </html>
    """
    return render_template_string(html_page, produits=PRODUITS)

if _name_ == '_main_':
    app.run(debug=True)
