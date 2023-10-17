from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
            'price', type=float, required=True, help='This must be filled!'
            )
    
    @jwt_required()
    def get(self, name):
        item = ItemModel.search_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found!'}, 404

    def post(self, name):
        item = ItemModel.search_by_name(name)
        if item:
            return {'message': f'Item with name {name} already exists'}, 400
        
        data = Item.parser.parse_args()

        item = ItemModel(name, data['price'])

        try:
            item.save_to_db()
        except:
            return {'message': 'An error occurred inserting the item!'}, 500 # INTERNAL ERROR
        
        return item.json(), 201

    def delete(self, name):
        item = ItemModel.search_by_name(name)

        if item:
            item.delete_from_db()

        return {'message': 'Item deleted!'}
    
    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.search_by_name(name)

        if item:
            item.price = data['price']
        else:
            item = ItemModel(name, data['price'])

        item.save_to_db()
            
        return item.json()


class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items"
        result = cursor.execute(query)
        items = []

        for row in result:
            items.append({'name': row[0], 'price': row[1]})

        connection.close() 

        return {'items': items}
    