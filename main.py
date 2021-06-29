from flask import Flask
from flask_restful import Api, Resource, reqparse
import pandas as pd

app = Flask(__name__)
api = Api(app)


class Users(Resource):
    def get(self, userid=None):
        data = pd.read_csv('users.csv')
        data = data.to_dict('records')
        if userid:
            return {'data' : list(filter(lambda user: user['id'] == int(userid), data))}, 200
        return {'data' : data}, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('first_name', required=True)
        parser.add_argument('second_name', required=True)
        parser.add_argument('age', required=True)
        args = parser.parse_args()

        data = pd.read_csv('users.csv')

        new_data = pd.DataFrame({
            'id': data["id"].max()+1,
            'first_name': [args['first_name']],
            'second_name': [args['second_name']],
            'age': [args['age']]
        })

        data = data.append(new_data, ignore_index=True)
        data.to_csv('users.csv', index=False)
        return {'data' : new_data.to_dict('records')}, 201

    def delete(self, userid=None):
        parser = reqparse.RequestParser()
        if userid:
            data = pd.read_csv('users.csv')
            data = data[data['id'] != int(userid)]
            data.to_csv('users.csv', index=False)
            return {'message': 'Record deleted successfully.'}, 200

        parser.add_argument('id', required=True)
        args = parser.parse_args()
        data = pd.read_csv('users.csv')
        data = data[data['id'] != int(args['id'])]
        data.to_csv('users.csv', index=False)
        return {'message' : 'Record deleted successfully.'}, 200


api.add_resource(Users, '/users', "/users/<userid>")

if __name__ == '__main__':
    app.run()

