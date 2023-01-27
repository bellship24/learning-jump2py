import time


def elapsed(original_func):
    def wrapper():
        start = time.time()
        result = original_func()
        end = time.time()
        print("함수 수행시간: %f 초" % (end - start))
        return  result
    return wrapper

@elapsed
def myfunc(msg):
    print("'%s'를 출력합니다." % msg)


# decorated_myfunc = elapsed(myfunc)
# decorated_myfunc()

myfunc()