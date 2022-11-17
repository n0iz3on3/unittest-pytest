list_ = ['2018-01-01', 'yandex', 'cpc', 100]

def get_convert_list_to_dicts(lst):
    dict_ = {lst[len(lst) - 2]: lst.pop()}
    del lst[-1]
    for elem in range(len(lst)):
        dict_ = {lst.pop(): dict_}
    return dict_