import pickle

def load_object(filename = 'usernames.pkl'):
    with open(filename, 'rb') as input_file:
        user = pickle.load(input_file)
    return user

def save_object(obj, filename = 'usernames.pkl'):
    with open(filename, 'wb') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

