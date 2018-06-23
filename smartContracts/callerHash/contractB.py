from boa.interop.Neo.App import RegisterAppCall

contractA = RegisterAppCall('a5813ff2d3825caf2a52396f23b9e50a9aa7a7c8', 'operation', 'args')

def Main(operation, args):

  contractA('testtesttest', [12345])
