from MapReduce import MapReduce
from FindCitations import FindCitations
from FindCyclicReferences import FindCyclicReferences
import sys
import os.path

if __name__ == '__main__':
    n = len(sys.argv)

    if (n != 4):
        print("Four arguments expected")
        exit(1)

    if (sys.argv[1] != "COUNT" and sys.argv[1] != "CYCLE"):
        print("COUNT and CYCLE are the only valid operation types")
        exit(1)

    if (sys.argv[2].isnumeric() == False):
        print("Third argument should be an integer")
        exit(1)

    numWorkers = int(sys.argv[2])
    if (numWorkers > 10):
        print("Maximum of 10 workers")
        exit(1)
        
    filename = sys.argv[3]
    if (os.path.exists(filename) == False):
        print(filename, "does not exist")
        exit(1)

    if (sys.argv[1] == "COUNT"):
        print("Find Citations called")
        func = FindCitations(numWorkers)
        func.start(filename)
    else:
        print("Find Cyclic References called")
        func = FindCyclicReferences(numWorkers)
        func.start(filename)
