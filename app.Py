from flask import Flask,render_template_string

app=Flask(__name__)

#ledictionnaire est vide au départ! cest l'utilisateure qui vas le remplir.
PRODUITS={}
#un compteur pour donner un identifiant unique (1,2,3...)à chaque produit
prochain_id=1

#1.page d'acceuil:liste les produis(ou affiche un message si vide)
@app.route('/')
def boutique():
    html_page="""
   <!DOCTYPE htlm>
   <html>
   <head>
         <meta charset="UTF-8">
         <title>Nom De Ma Boutique</title>
         <style>
             body {front-family:Arial,sans-serf;margin:'40px;background-color:#f9f9f;}
             .header-bar {display: flex;justify-content:space-between;align-items:center;}
             .panier-btn {background-color:#333; color:white;padding: 12px 20px;text-decoration: none border-raduis: 5px; font-weight:bold;}
             .ajouter-btn {background-color:#28a745; color: withe; padding: 12px 20px; texte-decoration:none; border-radius:5px;display: inline-block;margin-top: 20px; font-weight: bold;}
             .produit-card{ background:white; padding:15px;margin:10px 0; border-raduis:8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);list-style:none; }
             .voir-lien{color:#007bff; text-decoration:none; font-weight:bold; margin-left:15px;}
             
        </style>
    </head>
    <body>

        <div class="header-bar">
             <h1>Ma Super Boutique</h1>
             <a href="#" class="panier-btn" onclick="alert('le panier est vide pour le moment!')">Mon Panier</a>
        </div>

        <a href="/ajouter" class="ajouter-btn"}+Mettre un produit en vente</a>

        <hr style="marging-top: 20px; border: 0; border-top:1px solid #ccc;">

        {%if not produits%}
            <p style="color:#666; font-style:italic; marging-top: 30px;">
                la boutique est vide. cliquer sur le bouton vert pour ajouter votre premier produit!

            </p>
        {% elese%}
            <h3>produits disponibles :</h3>
            ul style="padding: 0;">
               {% for id, prod in produits.items()%}
                   <li class="produit-card">
                       <strong>{{prod.nom}}</strong - <span style="color: #28a745; font-weight:bold;">{{prod.prix}}fcfa</span>
                       <a href="/produit/{{id}}" class="voir-lien">voirlafiche </a>
                   </li>
               {% endfor %}
            </ul>
         {%endif%}

       </body>
       </htlm>
       """
    return render_template_string(html_page, produits=PRODUITS)
#lancement du cerveur Flask
if __name__== '__main__':
    app.run(debug=True)
