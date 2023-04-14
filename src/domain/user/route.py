from flask import request, jsonify
import domain.user.controller as Controller 

#la route llama al controller, donde está nuestra lógica

def user_route(app):

    @app.route('/user', methods=['POST'])
    def create_user():
        data = request.get_json()
        return Controller.create_user(data)
        
    @app.route('/user', methods=['GET'])
    def get_all_users():
        return Controller.get_all_users()
    
    @app.route('/user/<int:id>', methods=['GET'])
    def get_user_by_id(id):
        return Controller.get_user_by_id(id)
        
    @app.route('/user/<int:id>', methods=['DELETE'])
    def delete_user(id):
        return Controller.delete_user(id)

