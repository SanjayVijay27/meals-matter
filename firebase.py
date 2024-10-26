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
def add_user(username, password, account_type):
    user_data = {
        'username': username,
        'password': hash_password(password), # Store hashed password
        'account_type': account_type
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

# Test Firebase database
if __name__ == '__main__':
    add_user('user1', 'password123', "recipient")
    add_user('user2', 'mypassword', "distributor")

    users = get_users()
    print("All users:")
    for user in users:
        print(user)
