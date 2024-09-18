from flask import Flask, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Make sure this key is kept secure

# Sample products (this could be from a database)
products = [
    {'id': 1, 'name': 'Laptop', 'price': 1000},
    {'id': 2, 'name': 'Smartphone', 'price': 500},
    {'id': 3, 'name': 'Headphones', 'price': 100},
]

@app.route('/')
def product_list():
    return render_template('products.html', products=products)

@app.route('/add-to-cart/<int:product_id>')
def add_to_cart(product_id):
    product = next((item for item in products if item['id'] == product_id), None)
    if product:
        cart = session.get('cart', [])
        cart.append(product)
        session['cart'] = cart
    return redirect(url_for('product_list'))

@app.route('/cart')
def cart():
    cart = session.get('cart', [])
    total_price = sum(item['price'] for item in cart)
    return render_template('cart.html', cart=cart, total_price=total_price)

@app.route('/clear-cart')
def clear_cart():
    session.pop('cart', None)
    return redirect(url_for('cart'))

if __name__ == '__main__':
    app.run(debug=True)