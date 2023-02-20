def get_path(file_path):
    """从相对地址返回正确的绝对地址"""
    while file_path.startswith('..\\'):
        file_path = file_path[3:]
    return file_path
