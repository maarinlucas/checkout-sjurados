import mercadopago

def gerar_link_pagamento():
    sdk = mercadopago.SDK("APP_USR-959358377413846-091918-f382a54b75e515fe89c7aea46d38c6c0-1956623115")

    payment_data = {
        "items": [
            {"id": "1", "title": "App Sjurados Vitalício", "quantity": 1, "currency_id": "BRL", "unit_price": 1.00}
        ],
        "back_urls": {
            "success": "http://127.0.0.1:5000/cadastro",
            "failure": "http://127.0.0.1:5000/compraerrada",
            "pending": "http://127.0.0.1:5000/compraerrada",
        },
        "auto_return": "all"
    }
    result = sdk.preference().create(payment_data)
    payment = result["response"]
    link_iniciar_pagamento = payment["init_point"]
    return link_iniciar_pagamento