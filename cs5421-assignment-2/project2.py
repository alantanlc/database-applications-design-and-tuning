############################################################
## project2.py - Code template for Project 2 - Normalization
## Both for CS5421 and CS4221 students
############################################################


### IMPORTANT! Change this to your metric number for grading
student_no = 'A0174404L'

from itertools import combinations
import sys

## Determine the closure of set of attribute S given the schema R and functional dependency F
def closure(R, F, S):
	# Convert S to set
	x_previous = set(S);
	x_current = set(S);

	while 1:
		# For each FD, if LHS is a subset of x_current, update x_current with the RHS of FD
		for i in F:
			if set(i[0]).issubset(x_current):
				x_current.update(i[1])

		if x_current == x_previous:
			break
		else:
			x_previous.update(x_current)

	return list(x_current)


## Determine the all the attribute closure excluding superkeys that are not candidate keys given the schema R and functional dependency F
def all_closures(R, F):
	x = []

	# Iterate through all combinations of R for lengths 1...len(R)
	ck_length = sys.maxint
	for i in range(len(R)):
		comb = combinations(R, i+1)
		for j in list(comb):
			# Compute closure of subset
			comb_closure = closure(R, F, list(j))

			# Check if is super key
			if set(comb_closure) == set(R):
				# Check if is candidate key
				# If yes, add pair to x, else don't add
				sk_length = len(list(j))
				if sk_length <= ck_length:
					ck_length = sk_length
					x += [[list(j), comb_closure]]
			else:
				# Add all pairs that are not super key to x
				x += [[list(j), comb_closure]]

	return x


## Return the candidate keys of a given schema R and functional dependencies F.
## NOTE: This function is not graded for CS5421 students.
def candidate_keys(R, F):
	return []


## Return a minimal cover of the functional dependencies of a given schema R and functional dependencies F.
def min_cover(R, FD):
	# Singleton right hand side
	singleton_fd = []
	for fd in FD:
		for rhs in fd[1]:
			singleton_fd += [[fd[0], [rhs]]]

	# Remove extraneous attributes
	extraneous_free_fd = [None] * len(singleton_fd)
	for i in range(len(singleton_fd)):
		if len(singleton_fd[i][0]) > 1:   # Continue only if LHS has 2 or more attributes
			print singleton_fd[i][0]
			extraneous_free_fd[i] = [[], []]
			extraneous_free_fd[i][1] = list(singleton_fd[i][1])
			for j in range(len(singleton_fd[i][0])):
				lhs =  list(singleton_fd[i][0])
				attr = lhs[j]
				lhs.remove(attr)
				if attr not in closure(R, singleton_fd, lhs):
					extraneous_free_fd[i][0] += [attr]
		else:
			extraneous_free_fd[i] = list(singleton_fd[i])

	# Remove redundant FDs
	redundant_free_fd = []
	for fd in extraneous_free_fd:
		removed_fd = [x for x in extraneous_free_fd if x != fd]
		# print removed_fd
		if fd[1][0] not in closure(R, removed_fd, fd[0]):
			redundant_free_fd += [fd]

	minimal_cover = redundant_free_fd

	return minimal_cover

## Return all minimal covers reachable from the functional dependencies of a given schema R and functional dependencies F.
## NOTE: This function is not graded for CS4221 students.
def min_covers(R, FD):
	return []


## Return all minimal covers of a given schema R and functional dependencies F.
## NOTE: This function is not graded for CS4221 students.
def all_min_covers(R, FD):
	return []


### Test case from the project
R = ['A', 'B', 'C', 'D']
FD = [[['A', 'B'], ['C']], [['C'], ['D']]]
# print closure(R, FD, ['A'])
# print closure(R, FD, ['A', 'B'])
# print all_closures(R, FD)

R = ['A', 'B', 'C', 'D', 'E', 'F']
FD = [[['A'], ['B', 'C']], [['B'], ['C', 'D']], [['D'], ['B']], [['A', 'B', 'E'], ['F']]]
print min_cover(R, FD)

# R = ['A', 'B', 'C', 'D', 'E']
# FD = [[['A'], ['B']], [['A', 'B'], ['C']], [['D'], ['A', 'C']], [['D'], ['E']]]
# print min_cover(R, FD)

R = ['A', 'B', 'C']
FD = [[['A', 'B'], ['C']], [['A'], ['B']], [['B'], ['A']]]
# print min_covers(R, FD)
# print all_min_covers(R, FD)

## Tutorial questions
R = ['A', 'B', 'C', 'D', 'E']
FD = [[['A', 'B'], ['C']], [['D'], ['D', 'B']], [['B'], ['E']], [['E'], ['D']], [['A', 'B', 'D'], ['A', 'B', 'C', 'D']]]

# print candidate_keys(R, FD)
# print min_cover(R, FD)
# print min_covers(R, FD)
# print all_min_covers(R, FD)

print "End of program"