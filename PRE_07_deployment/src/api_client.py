#
# Usage from command line:
# curl http://127.0.0.1:5000 -X POST -H "Content-Type: application/json" -d '{"bathrooms": "2", "bedrooms": "3", "sqft_living": "1800", "sqft_lot": "2200", "floors": "1", "waterfront": "1", "condition": "3"}'
#
import re
import requests


def make_request():
    url = "http://127.0.0.1:5000"

    data = {
        "bathrooms": "2",
        "bedrooms": "3",
        "sqft_living": "1800",
        "sqft_lot": "2200",
        "floors": "1",
        "waterfront": "1",
        "condition": "3",
    }

    response = requests.post(url, data=data, timeout=5)

    # Buscar el valor numérico después de 'Estimated Price:'
    match = re.search(r"Estimated Price:.*?\s+([\d.]+)", response.text, re.DOTALL)
    if match:
        price = float(match.group(1))
        print(f"Precio estimado obtenido: ${price:,.2f}")
    else:
        print("No se encontró el precio en la respuesta HTML.")


if __name__ == "__main__":
    make_request()