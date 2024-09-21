import os
from flask import Flask, render_template
from apimercadopago import gerar_link_pagamento

app = Flask(__name__)

@app.route("/")
def homepage():
    link_iniciar_pagamento = gerar_link_pagamento()
    return render_template("index.html", link_pagamento=link_iniciar_pagamento)

@app.route("/cadastro")
def compra_certa():
    return render_template("cadastro.html")

@app.route("/compraerrada")
def compra_errada():
    return render_template("compraerrada.html")

""" if __name__ == "__main__":
    # Obtém a porta fornecida pelo Heroku, ou usa 5000 para rodar localmente
    port = int(os.environ.get("PORT", 5000))
    # Faz a aplicação escutar em todas as interfaces de rede (necessário para Heroku)
    app.run(host="0.0.0.0", port=port) """
