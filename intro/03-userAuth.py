from boa.blockchain.vm.Neo.Runtime import CheckWitness

def Main(callerHash):

    isMatch = CheckWitness(callerHash);

    if isMatch:
        print("Caller hash matches provided hash!")
        return True

    print("IMPOSTER!!!")
    return False
