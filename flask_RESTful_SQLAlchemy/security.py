from resources.user import User

# users = [
#     {
#         'id': 1, 
#         'username': 'jack',
#         'password': 'jackpass'
#     }
# ]

# username_mapping = { 'bob':
#     {
#         'id': 1, 
#         'username': 'jack',
#         'password': 'jackpass'
#     }
# }

# userid_mapping = {1: 
#     {
#         'id': 1, 
#         'username': 'jack',
#         'password': 'jackpass'            
#     }
# }


def authenticate(username, password):
    user = User.search_by_username(username)
    if user and user.password == password:
        return user
    
def identity(payload):
    user_id = payload['identity']
    return User.search_by_id(user_id)