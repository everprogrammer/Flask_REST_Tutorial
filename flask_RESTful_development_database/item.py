from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
            'price', type=float, required=True, help='This must be filled!'
            )
    
    @jwt_required()
    def get(self, name):

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()

        connection.close()

        if row:
            return {'item': {'name': row[0], 'price': row[1]}}
        return {'message': 'Item not found!'}, 404
    
    @classmethod
    def search_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item': {'name': row[0], 'price': row[1]}}

    def post(self, name):
        item = self.search_by_name(name)
        if item:
            return {'message': f'Item with name {name} already exists'}, 400
        
        data = Item.parser.parse_args()

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES (?, ?)"
        cursor.execute(query, (name, data['price']))

        connection.commit()
        connection.close()

        return {'item': {'name': name, 'price': data['price']}}, 201
    

    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM items WHERE name=?"
        cursor.execute(query, (name,))

        connection.commit()
        connection.close()  

        return {'message': 'Item deleted!'}
    def put(self, name):
        pass

class ItemList(Resource):
    def get(self):
        pass
    