import requests


database = {
    1: "Alice",
    2: "Bob",
    3: "Charlie",
}

def get_user_from_db(user_id):
    return database.get(user_id)


# https://www.jsonplaceholder.typeicode.com/users

def get_user_from_db(user_id):
    return database.get(user_id)


def get_users():
    response = requests.get("https://www.jsonplaceholder.typeicode.com/users")

    if response.status_code == 200:
        return response.json()
    
    # If there is an error it raises an http error
    raise requests.HTTPError