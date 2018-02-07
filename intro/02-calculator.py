def Main(operation, foo, bar):

    if operation == None or foo == None or bar == None:
        print('Operation, foo, and bar all required~!')
        return False

    if operation == 'plus':
        print('plus')
        return foo + bar

    if operation == 'minus':
        print('minus')
        return foo - bar

    if operation == 'multiply':
        print('multiply')
        return foo * bar

    if operation == 'divide':
        print('divide')
        return foo / bar

    print('invalid operation')
    print(operation)
    return False
