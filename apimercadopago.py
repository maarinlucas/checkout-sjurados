# -*- coding: utf-8 -*-
import mercadopago

def gerar_link_pagamento():
    sdk = mercadopago.SDK("APP_USR-959358377413846-091918-f382a54b75e515fe89c7aea46d38c6c0-1956623115")
    #APP_USR-959358377413846-091918-f382a54b75e515fe89c7aea46d38c6c0-1956623115
    #Produção: APP_USR-1746040795185388-092019-6d447169a49a891e0dec99d562fb1104-310155133

    payment_data = {
        "items": [
            {"id": "1", "title": "App Sjurados Vitalício", "quantity": 1, "currency_id": "BRL", "unit_price": 50.00}
        ],
        "back_urls": {
            #"success": "https://nameless-dawn-62388-3d072fabd70a.herokuapp.com/checkout_success",
            # https://checkout-sjurados.onrender.com
            "success": "https://checkout-sjurados.onrender.com/cadastro",
            "failure": "https://checkout-sjurados.onrender.com/compraerrada",
            "pending": "https://checkout-sjurados.onrender.com/compraerrada",
        },
        "auto_return": "all"
    }
    result = sdk.preference().create(payment_data)
    payment = result["response"]
    link_iniciar_pagamento = payment["init_point"]
    return link_iniciar_pagamento