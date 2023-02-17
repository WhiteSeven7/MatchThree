def safe_remove(list_, value):
    new_list = list(list_)
    if value in new_list:
        new_list.remove(value)
    return new_list
