def get_path(py_path, file_path):
    """从相对地址返回正确的绝对地址"""
    dpn = file_path.count('..')
    return '\\'.join(py_path.split('\\')[:-1 - dpn] + file_path.split('\\')[dpn:])
