from boa.blockchain.vm.Neo.Storage import GetContext, Put, Delete, Get
from boa.blockchain.vm.Neo.Runtime import Notify

def Main(operation, args):

    if operation == None:
        print('Operation required~!')
        return False

    if operation == 'testAll':
        return testAll()

    if operation == 'put':
        key = args[0]
        value = args[1]
        return putOperation(key, value)

    if operation == 'delete':
        key = args[0]
        return deleteOperation(key)

    if operation == 'get':
        key = args[0]
        return getOperation(key)

    print('invalid operation')
    print(operation)
    return False

def testAll():
    Put(GetContext, 'original', 1)

    amount = Get(GetContext, 'original')
    amount += 20

    Put(GetContext, 'original', amount)
    Put(GetContext, 'copy', amount)

    Delete(GetContext, 'copy')

    copy = Get(GetContext, 'copy')
    original = Get(GetContext, 'original')

    Put(GetContext, 'storeString', 'this is a string')
    storeString = Get(GetContext, 'storeString')

    test = [original,copy,amount,storeString]
    Notify(test)

    return original

def putOperation(key, value):
    print('put attempt')

    if key == None:
        print('Key required')
        return False

    Put(GetContext, key, value)
    print('put successful')
    return True

def deleteOperation(key):
    print('delete attempt')

    if key == None:
        print('no key to delete')
        return False

    Delete(GetContext, key)
    print('delete successful')
    return True

def getOperation(key):
    print('get')
    return Get(GetContext, key)
