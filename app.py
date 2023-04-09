from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    products = get_products()  
    return render_template('homepage.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = get_product_by_id(product_id) 
    return render_template('product_detail.html', product=product)

\
@app.route('/cart')
def cart():
    cart_items = get_cart_items()  
    return render_template('cart.html', cart_items=cart_items)


@app.route('/checkout', methods=['POST'])
def checkout():
    
    return render_template('checkout.html')

if __name__ == '__main__':
    app.run(debug=True)
