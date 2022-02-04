from flask import Flask
from flask import request
from flask.json import jsonify

app = Flask(__name__)

from products import products
@app.route('/ping')
def ping():
    return jsonify({'message': 'pong!!'})

@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify({'products': products, 'message': 'Products list'})

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    product_found = [product for product in products if product['name'] == product_name]
    if(len(product_found) > 0):
        return jsonify({'product':product_found[0]});
    return jsonify({'message': 'product not exist'})

@app.route('/products', methods=['POST'])
def addProduct():
    new_Product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity":request.json['quantity']
    }
    products.append(new_Product)
    return jsonify({'message':'Producto agregado satisfactoriamente', 'products': products})

@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    product_found = [product for product in products if product['name'] == product_name]
    if(len(product_found) > 0):
        product_found[0]['name'] = request.json['name'],
        product_found[0]['price'] = request.json['price'],
        product_found[0]['quantity'] = request.json['quantity']
        return jsonify({'message':'Producto odificiad', 'product': product_found[0]})
    return jsonify({'message': 'product not exist'})

@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    product_found = [product for product in products if product['name'] == product_name]
    if(len(product_found) > 0):
        products.remove(product_found[0])
        return jsonify({'message':'Product deleted', 'product': products})
    return jsonify({'message': 'Product not exist'})


if __name__ == '__main__':
    app.run(debug=True, port=4000)