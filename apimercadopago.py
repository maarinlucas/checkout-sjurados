# -*- coding: utf-8 -*-
import mercadopago

def gerar_link_pagamento():
    sdk = mercadopago.SDK("APP_USR-1746040795185388-092019-6d447169a49a891e0dec99d562fb1104-310155133")

    payment_data = {
        "items": [
            {"id": "1", "title": "App Sjurados Vitalício", "quantity": 1, "currency_id": "BRL", "unit_price": 1.00}
        ],
        "back_urls": {
            "success": "https://nameless-dawn-62388-3d072fabd70a.herokuapp.com/cadastro",
            "failure": "https://nameless-dawn-62388-3d072fabd70a.herokuapp.com/compraerrada",
            "pending": "https://nameless-dawn-62388-3d072fabd70a.herokuapp.com/compraerrada",
        },
        "auto_return": "all"
    }
    result = sdk.preference().create(payment_data)
    payment = result["response"]
    link_iniciar_pagamento = payment["init_point"]
    return link_iniciar_pagamento