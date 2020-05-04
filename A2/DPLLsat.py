#!/usr/bin/python3
# CMPT310 A2
#####################################################
#####################################################
# Please enter the number of hours you spent on this
# assignment here
"""
num_hours_i_spent_on_this_assignment = 25
"""
#
#####################################################
#####################################################

#####################################################
#####################################################
# Give one short piece of feedback about the course so far. What
# have you found most interesting? Is there a topic that you had trouble
# understanding? Are there any changes that could improve the value of the
# course to you? (We will anonymize these before reading them.)
"""
<Your feedback goes here>
I am having trouble understanding pure literals in the DPLL algorithm, 
"""
#####################################################
#####################################################
import sys, getopt
import copy
import random
import time
import numpy as np
sys.setrecursionlimit(10000)

class SatInstance:
    def __init__(self):
        pass

    def from_file(self, inputfile):
        self.clauses = list()
        self.VARS = set()
        self.p = 0
        self.cnf = 0
        with open(inputfile, "r") as input_file:
            self.clauses.append(list())
            maxvar = 0
            for line in input_file:
                tokens = line.split()
                if len(tokens) != 0 and tokens[0] not in ("p", "c"):
                    for tok in tokens:
                        lit = int(tok)
                        maxvar = max(maxvar, abs(lit))
                        if lit == 0:
                            self.clauses.append(list())
                        else:
                            self.clauses[-1].append(lit)
                if tokens[0] == "p":
                    self.p = int(tokens[2])
                    self.cnf = int(tokens[3])
            assert len(self.clauses[-1]) == 0
            self.clauses.pop()
            if (maxvar > self.p):
                print("Non-standard CNF encoding!")
                sys.exit(5)
        # Variables are numbered from 1 to p
        for i in range(1, self.p + 1):
            self.VARS.add(i)

    def __str__(self):
        s = ""
        for clause in self.clauses:
            s += str(clause)
            s += "\n"
        return s

def main(argv):
    inputfile = ''
    verbosity = False
    inputflag = False
    try:
        opts, args = getopt.getopt(argv, "hi:v", ["ifile="])
    except getopt.GetoptError:
        print('DPLLsat.py -i <inputCNFfile> [-v] ')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('DPLLsat.py -i <inputCNFfile> [-v]')
            sys.exit()
        ##-v sets the verbosity of informational output
        ## (set to true for output veriable assignments, defaults to false)
        elif opt == '-v':
            verbosity = True
        elif opt in ("-i", "--ifile"):
            inputfile = arg
            inputflag = True
    if inputflag:
        instance = SatInstance()
        instance.from_file(inputfile)
        #start_time = time.time()
        solve_dpll(instance, verbosity)
        #print("--- %s seconds ---" % (time.time() - start_time))

    else:
        print("You must have an input file!")
        print('DPLLsat.py -i <inputCNFfile> [-v]')

# Finds a satisfying assignment to a SAT instance,
# using the DPLL algorithm.
# Input: a SAT instance and verbosity flag
# Output: print "UNSAT" or
#    "SAT"
#    list of true literals (if verbosity == True)
#
#  You will need to define your own
#  DPLLsat(), DPLL(), pure-elim(), propagate-units(), and
#  any other auxiliary functions
def solve_dpll(instance, verbosity):
    # print(instance)
    # instance.VARS goes 1 to N in a dict
    # print(instance.VARS)
    # print(verbosity)
    ###########################################
    # Start your code
    sentenceCheck = instance.clauses
    sentence = instance.clauses
    variables = instance.VARS

    model = set()
    model = DPLL(sentenceCheck, sentence, variables, model)
    if model == "Failure":
        print("UNSAT")
    else:
        print("SAT")
        listModel = list(model)
        if verbosity == True:
            for i in listModel:
                if i < 0:
                    listModel.remove(i)
            print(listModel)
        
###########################################
def DPLLsat(sentence, model):
    sentence = copy.deepcopy(sentence)
    #print("model: ", model)
    #print(sentence,"\n")
    for currClause in list(sentence):
        for item in model:
            if item in currClause:
                sentence.remove(currClause)
                #print(clauses)
                break
    if len(sentence) == 0:
        return True
    else:
        return False

# Finds a unit clause within an instance.
# Returns False if no unit clauses found
def propagate_units(sentence, unitClause):
    sentence = copy.deepcopy(sentence)
    #print("sentence: ", sentence, "\n")
    for item in unitClause:
        for clause in sentence:
            #print("clause: ", clause, "\n")
            if len(clause) != 1 and (item in clause or -item in clause):
                # print("clause to remove: ", clause)
                sentence.remove(clause)
    return sentence

def DPLL(sentenceCheck, sentence, variables, model):
    #print("current model: ",model, "\n")
    sentence = copy.deepcopy(sentence)
    variables = copy.deepcopy(variables)
    model = copy.deepcopy(model)

    # Base case
    if len(variables) == 0:
        if DPLLsat(sentenceCheck, model) == True:
            return model
        else:
            return "Failure"

    popVal = variables.pop()
    # print(popVal)
    model.add(popVal)
    
    # check for unit clauses 
    unitClause = []
    for clause in sentence:
        if len(clause) == 1:
            unitClause.append(clause[0])
            if clause[0] not in model:
                model.add(clause[0])
            elif -clause[0] in model:
                model.remove(-clause[0])
                model.add(clause[0])
            if DPLLsat(sentenceCheck, model) == True:
                return model
            else:
                return "Failure"
        else:
            if len(model) > 1:
                for entry in model:
                    if -entry in clause:
                        clause.remove(-entry)
            if len(clause) == 1:
                unitClause.append(clause[0])
                if clause[0] not in model:
                    model.add(clause[0])
                elif -clause[0] in model:
                    model.remove(-clause[0])
                    model.add(clause[0])
    sentence = propagate_units(sentence, unitClause)
    
    # print(unitClause)
    # print(sentence)
    # input()

    
    # Recursion:
    returnValue = DPLL(sentenceCheck, sentence,variables,model)
    if returnValue == "Failure":
        # print(model)
        # print(popVal)
        model.remove(popVal)
        model.add(-popVal)
        return DPLL(sentenceCheck ,sentence,variables,model)
    else:
        return returnValue

if __name__ == "__main__":
    main(sys.argv[1:])
