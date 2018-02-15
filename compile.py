import sys, getopt
from boa.compiler import Compiler

def main(argv):
  inputfile = ''

  try:
    opts, args = getopt.getopt(argv,"hi:")
  except getopt.GetoptError:
    print ('compileSmartContract.py -i <inputfile>')
    sys.exit(2)

  for opt, arg in opts:
    if opt == '-h':
      print ('compileSmartContract.py -i <inputfile>')
      sys.exit()
    elif opt in ("-i"):
      inputfile = arg

  if inputfile == '':
    print ('ERROR: Please provide an input file. See -h for help.')
    sys.exit(2);

  Compiler.load_and_save(inputfile)

if __name__ == "__main__":
   main(sys.argv[1:])
