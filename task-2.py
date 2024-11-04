from flask import Flask, request, jsonify

app = Flask(__name__)

stores = []

# Створення магазину
@app.route('/store', methods=['POST'])
def create_store():
    data = request.get_json()
    new_store = {
        'name': data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store), 201

# Отримання всіх магазинів
@app.route('/store', methods=['GET'])
def get_stores():
    return jsonify({'stores': stores}), 200

# Отримання конкретного магазину за назвою
@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store), 200
    return jsonify({'message': 'Магазин не знайдено'}), 404

# Додавання товару до магазину
@app.route('/store/<string:name>/item', methods=['POST'])
def add_item(name):
    data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': data['name'],
                'price': data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item), 201
    return jsonify({'message': 'Магазин не знайдено'}), 404

# Отримання всіх товарів магазину
@app.route('/store/<string:name>/item', methods=['GET'])
def get_items(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']}), 200
    return jsonify({'message': 'Магазин не знайдено'}), 404

#видалення магазину за назвою
@app.route('/store/<string:name>', methods=['DELETE'])
def delete_store(name):
    global stores
    # Перевіряємо чи існує магазин зі вказаною назвою
    for store in stores:
        if store['name'] == name:
            stores.remove(store)
            return jsonify({'message': f'Магазин "{name}" видалено успішно'}), 200
    return jsonify({'message': 'Магазин не знайдено'}), 404

if __name__ == '__main__':
    app.run(debug=True)
