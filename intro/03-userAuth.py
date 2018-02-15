from boa.blockchain.vm.Neo.Runtime import CheckWitness

# A simple function to demonstrate the usage of CheckWitness
# This contract will validate the provided input key/hash matches that of callerHash

def Main(callerHash):

    isMatch = CheckWitness(callerHash);

    if isMatch:
        print("Caller hash/key matches provided hash/key!")
        return True

    print("IMPOSTER!!!")
    return False
