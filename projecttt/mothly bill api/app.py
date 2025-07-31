from flask import Flask, jsonify

app = Flask(__name__)

# Sample product data
products = [
    {'id': 1, 'name': 'Laptop', 'price': 50000},
    {'id': 2, 'name': 'Smartphone', 'price': 20000},
    {'id': 3, 'name': 'Tablet', 'price': 15000}
]

# Home route
@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the Product API! Use /api/products or /api/products/<id>"
    })

# Route to get all products
@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)

# Route to get a product by ID
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({'error': 'Product not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
