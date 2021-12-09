from datetime import datetime


def log_dec_path(path):
    def log_dec(old_function):
        def new_function(*args, **kwargs):

            result = old_function(*args, **kwargs)
            log = open(f'{path}/log.txt', 'w')
            log.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}: Function called "{old_function.__name__}",'
                      f' with args {args}{kwargs}, returned {result}')
            return result

        return new_function

    return log_dec


# указать путь
@log_dec_path('')
def unpacker(packed_list):
    for unpacked_list in packed_list:
        for unpacked_item in unpacked_list:
            yield unpacked_item


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]
for item in unpacker(nested_list):
    print(item)
