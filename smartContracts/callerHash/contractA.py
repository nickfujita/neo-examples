from boa.interop.System.ExecutionEngine import GetCallingScriptHash
from src.printCaller import *

def Main(operation, args):
  caller = GetCallingScriptHash()
  print('caller_main')
  print(caller)
  printTest()
