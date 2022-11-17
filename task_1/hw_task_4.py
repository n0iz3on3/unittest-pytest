stats = {
    'facebook': 55,
    'yandex': 120,
    'vk': 115,
    'google': 99,
    'email': 42,
    'ok': 98
}

def get_key_from_max_value(stats_dict):
    result = max(stats, key=stats.get)
    return result