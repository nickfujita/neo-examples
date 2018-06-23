from boa.interop.System.ExecutionEngine import GetCallingScriptHash

def printTest():
    caller = GetCallingScriptHash()
    print('caller_printCaller')
    print(caller)
