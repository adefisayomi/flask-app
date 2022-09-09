

def error():
    try:
        print('Running...')
        34/0
        raise Exception('this is an error')
    except Exception as e:
        print(e.__traceback__)
    finally:
        print('I will run no matter what')


error()