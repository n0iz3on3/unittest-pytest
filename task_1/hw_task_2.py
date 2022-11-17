ids = {
    'user1': [213, 213, 213, 15, 213],
    'user2': [54, 54, 119, 119, 119],
    'user3': [213, 98, 98, 35]
}

def get_unique_ids(ids_dict):
    id = []
    for users in ids.values():
        id += users
    result = list(set(id))
    return sorted(result)