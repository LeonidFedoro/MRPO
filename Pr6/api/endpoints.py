from flask import Flask, request, jsonify
from use_case.dating_use_case import DatingUseCase
from repositories.user_repository import UserRepository
from repositories.pair_repository import PairRepository
from repositories.message_repository import MessageRepository
from repositories.chat_repository import ChatRepository
from repositories.gift_repository import GiftRepository

app = Flask(__name__)
use_case = DatingUseCase()

@app.route('/api/user', methods=['GET'])
def get_users():
    users = use_case.get_all_users()
    return jsonify([user.to_dict() for user in users])

@app.route('/api/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = use_case.get_user(user_id)
    if user:
        return jsonify(user.to_dict())
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
