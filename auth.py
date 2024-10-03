import json

def user_validate(username, password):

    with open('users.json', 'r') as arquivo:
        dados = json.load(arquivo)
        
    for user in dados:
        if user['username'] == username and user['password'] == password:
            return True
    return False