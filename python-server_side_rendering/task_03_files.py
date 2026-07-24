import json
import csv
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
       return render_template('index.html')

@app.route('/about')
def about():
       return render_template('about.html')

@app.route('/contact')
def contact():
       return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json') as f:
            data = json.load(f)
    items_list = data.get('items', []) if isinstance(data, dict) else data
    return render_template('items.html', items=items_list)

def read_json(filepath='products.json'):
    with open(filepath) as f:
        return json.load(f)


def read_csv(filepath='products.csv'):
    products = []
    with open(filepath, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template('product_display.html', error="Invalid product ID")

        filtered = [p for p in data if p['id'] == product_id]
        if not filtered:
            return render_template('product_display.html', error="Product not found")
        data = filtered

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True)