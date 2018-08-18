# CS761-CNF
##complete_data.txt contains all the information about every trial run so far. Each vector contains the following fields: 
[formulaID, n, m, density, totalRuns, success, [runs], mean, stdev, worst, best, formula]

##All formulas used can be found in formulas.txt
##trials.py is the central file to run. pip install pycosat to install SAT solver first. 
1. trials(fid, permitted) takes the formula ID and amount of runs before it terminates. It returns "Fail" if the trial is a fail. Otherwise, it returns the number of runs. 
2. random_formula(m,k,n) takes three parameters and generates a random formula with that property. If it can't find such a formula, it returns "UNSAT". Otherwise it returns all information about the formula including how long Walksat took to solve it. 