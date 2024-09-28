from datetime import time


def log(filename=None):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            ret = ""
            try:
                time_1 = time()
                result = func(*args, **kwargs)
                time_2 = time()
                ret += func.__name__ + " " + str(result) + "\n"
            except Exception as e:
                ret += func.__name__ + f" error: {e}. Inputs: {args}, {kwargs}\n"

            if filename is None:
                print(ret)
            else:
                with open(filename, "w") as file:
                    file.write(ret)
                    file.close()

            return result

        return wrapper

    return my_decorator


@log()  # filename="mylog.txt"
def my_function(x, y):
    return x + y
