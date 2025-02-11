from datetime import time


def log(filename=None):
    '''Декоратор автоматически логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки'''
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            ret = ""
            try:
                time1 = time()
                result = func(*args, **kwargs)
                time2 = time()
                ret += func.__name__ + " " + str(result) + "\n"
            except Exception as e:
                ret += (
                    func.__name__
                    + f" {type(e).__name__}: {e}. Inputs: {args}, {kwargs}\n"
                )
                raise
            finally:
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
