from user import User

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

users = [
    User(1, 'jack', 'jackpass'),
]

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}

def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password:
        return user
    
def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)