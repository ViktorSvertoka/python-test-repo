from contextlib import contextmanager


@contextmanager
def file_manager(filename, mode="w", encoding="utf-8"):
    print("Відкриваємо файл", filename)
    file = open(filename, mode, encoding=encoding)
    try:
        yield file
    finally:
        print("Закриваємо файл", filename)
        file.close()
        print("Завершення блоку with")


if __name__ == "__main__":
    with file_manager("new_file.txt") as f:
        f.write("Hello world!\n")
        f.write("The end\n")


from contextlib import contextmanager
from datetime import datetime


@contextmanager
def managed_resource(*args, **kwargs):
    log = ""
    timestamp = datetime.now().timestamp()
    msg = f"{timestamp:<20}|{args[0]:^15}| open \n"
    log += msg
    file_handler = open(*args, **kwargs)
    try:
        yield file_handler
    finally:
        diff = datetime.now().timestamp() - timestamp
        msg = f"{timestamp:<20}|{args[0]:^15}| closed {round(diff, 6):>15}s \n"
        log += msg
        file_handler.close()
        print(log)


with managed_resource("new_file.txt", "r") as f:
    print(f.read())
