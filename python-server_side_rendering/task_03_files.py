from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_products_from_json():
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except:
        return []

def read_products_from_csv():
    try:
        with open('products.csv', newline='') as file:
            reader = csv.DictReader(file)
            return [
                {"id": int(row["id"]), "name": row["name"], "category": row["category"], "price": float(row["price"])}
                for row in reader
            ]
    except:
        return []

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        products = read_products_from_json()
    elif source == 'csv':
        products = read_products_from_csv()
    else:
        return render_template("product_display.html", error="Wrong source", products=[])

    # Filter by ID if provided
    if product_id:
        try:
            product_id = int(product_id)
            products = [p for p in products if p.get("id") == product_id]
            if not products:
                return render_template("product_display.html", error="Product not found", products=[])
        except ValueError:
            return render_template("product_display.html", error="Invalid ID", products=[])

    return render_template("product_display.html", products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

