import firebase_admin
from firebase_admin import credentials, firestore
import hashlib

# TODO: Revise documentation
# Initialize the Firebase Admin SDK
cred = credentials.Certificate('meals-matter-firebase-adminsdk-cgdbi.json')
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to add a user
def add_user(username, password, account_type, location):
    user_data = {
        'username': username,
        'password': hash_password(password), # Store hashed password
        'account_type': account_type,
        'location': location
    }
    # Add user data to the 'users' collection in Firestore
    db.collection('Users').add(user_data)
    print(f'User {username} added successfully!')

# Function to get all users
def get_users():
    users_ref = db.collection('Users')
    users = users_ref.stream()  # Retrieve all user documents
    user_list = []
    for user in users:
        user_dict = user.to_dict()  # Convert Firestore document to a dictionary
        user_list.append(user_dict)
    return user_list

def is_new_account(username):
    users = get_users()
    for user in users:
        if user['username'] == username:
            return False
    return True

def validate_account(username, password):
    users = get_users()
    for user in users:
        if user['username'] == username:
            return hash_password(password) == user['password']
    return False

# Test Firebase database
if __name__ == '__main__':
    add_user('JimmyJohns', 'password123', "distributor", "3311 W State St, West Lafayette, IN, 47906")
    add_user('PokeHibachi', 'mypassword', "distributor", "112 Andrew Pl, West Lafayette, IN, 47906")
    add_user('RaisingCanes', 'chicken', "distributor", "100 S Chauncey Ave Ste 100, West Lafayette, IN, 47906")
    add_user('RollingBowl', 'ricebowlwow', "distributor", "132 Northwestern Ave, West Lafayette, IN, 47906")
    add_user('EarhartDiningCourt', 'potstickeryay', "distributor", "1275 1st Street, West Lafayette, IN, 47906")
    add_user('Subway', 'eatfresh123', "distributor", "1400 Mitch Daniels Blvd Building F, West Lafayette, IN, 47906")
    add_user('MadMushroom', 'mypassword', "distributor", "320 W State St, West Lafayette, IN, 47906")
    add_user('OhanaEats', 'bobawoah', "distributor", "620 W Stadium Ave, West Lafayette, IN, 47906")
    add_user('EastEndGrill', 'grilly', "distributor", "1016 Main St, Lafayette, IN, 47901")
    add_user('ChickFilA', 'chickenfries', "distributor", "401 N Russell St, West Lafayette, IN, 47906")

    users = get_users()
    print("All users:")
    for user in users:
        print(user)
