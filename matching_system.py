import maps
import database

def find_distributors_radius(location, radius):
    valid_distributors = []
    users = database.get_users()
    for user in users:
        if user['account_type'] == 'recipient':
            continue
        if maps.find_distance(location, user['location']) < radius:
            valid_distributors.append(user)
    
    return valid_distributors

def find_nearest_distributor(location):
    nearest_distributor = None
    min_distance = None
    users = database.get_users()
    for user in users:
        if user['account_type'] == 'recipient':
            continue

        distance = maps.find_distance(location, user['location'])
        if nearest_distributor is None:
            nearest_distributor = user
            min_distance = distance
        elif distance < min_distance:
            nearest_distributor = user
            min_distance = distance
    
    return nearest_distributor

# Test matching system
if __name__ == '__main__':
    print(find_distributors_radius("812 W State St, West Lafayette, IN 47907", 10))
    print(find_nearest_distributor("812 W State St, West Lafayette, IN 47907"))
