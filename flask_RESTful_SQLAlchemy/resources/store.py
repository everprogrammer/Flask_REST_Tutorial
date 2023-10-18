from flask_restful import Resource, reqparse
from models.store import StoreModel

class Store(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True,
                        help='This name must be specified!')

    def get(self, name):
        store = StoreModel.search_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not found!'}, 404

    def post(self, name):
        store = StoreModel.search_by_name(name)
        if store:
            return {'message': f'Store with name "{name}" already exists!'}, 400
        
        store = StoreModel(name)

        try:
            store.save_to_db()
        except:
            return {'message': 'An error occurred while creating the store!'}, 500

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.search_by_name(name)
        if store:
            store.delete_from_db()
        
        return {'message': 'Store deleted'}



class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}