import badformulas
from random import randint, choice, uniform
import math
import pycosat
import sys, getopt
from math import sqrt
from completedata import data

def instance(k, m, n):
	l = []
	for i in range (0,m):
		newList = []
		for i in range(0,k):
			x = randint(1,n+1)
			if randint(0,1) == 0:
				x = x
			else:
				x = -x
			newList.append(x)
		l.append(newList)
	return l 

def satisfied(formula, x):
	final = True
	k = 0
	notSatisfied = []
	for conj in formula:
		val = False
		for j in conj:
			if j < 0:
				l = j*-1
				if x[l-1] < 0:
					val = val or True
				else:
					val = val or False
			else:
				if x[j-1] < 0:
					val = val or False
				else:
					val = val or True
		notSatisfied.append(k)
		k = k + 1
		final = final and val
	if final == False:
		return notSatisfied
	return final

def random_assignment(n):
	x = []
	for i in range(1,n+2):
		if randint(0,1) == 0:
			l = i
		else:
			l = -1*i
		x.append(l)
	return x

def randwalk(formula, x, n):
	for i in range(0,3*n):
		f = satisfied(formula, x)
		if f == True:
			return f
		else:
			clause = 0
			randClause = formula[choice(f)]
			for i in range(0,len(formula)):
				if i == randClause:
					clause = i
			randVariable = choice(randClause)
			for i in range(0, len(formula[clause])):
				if formula[clause][i] == randVariable:
					formula[clause][i] = formula[clause][i] * -1
	return False


def random_formula(m,k,n):
	flag = 0
	formula = instance(k,m,n)
	form = formula
	sat = pycosat.solve(formula)
	bad = 0
	while sat == "UNSAT" and bad < 300: #If all 300 trials fail to satisfying assignment, kill
		formula = instance(k,m,n)
		sat = pycosat.solve(formula)
		bad = bad + 1
	runs = 1
	if sat == "UNSAT":
		return "UNSAT"
	x = random_assignment(n)
	while randwalk(formula, x, n) == False:
		x = random_assignment(n)
		runs = runs + 1
	return runs, formula, m, k, n


def stddev(lst):
	mean = float(sum(lst)) / len(lst)
	return sqrt(float(reduce(lambda x, y: x + y, map(lambda x: (x - mean) ** 2, lst))) / len(lst))
	
def permitted(t):
	if t >=3 and t <=3.5:
		return 10000
	elif t > 3.5 and t <= 4:
		return 25000
	elif t > 4 and t <= 4.5:
		return 35000
	elif t > 4.5 and t <= 5:
		return 65000
	else:
		return 0

#Return runs if trial is a success
#Fail otherwise
def trials(fid, permitted):
	formula = badformulas.formulas[fid]
	times = 0 
	success = 0
	runs = 1
	n = data[fid][1]
	x = random_assignment(n)
	while randwalk(formula, x, n) == False and runs < permitted:
		x = random_assignment(n)
		runs = runs + 1
	if runs < permitted: #success
		return runs 
	return "Fail"


