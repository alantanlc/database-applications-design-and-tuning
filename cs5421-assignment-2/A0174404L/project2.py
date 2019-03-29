############################################################
## project2.py - Code template for Project 2 - Normalization
## Both for CS5421 and CS4221 students
############################################################


### IMPORTANT! Change this to your metric number for grading
student_no = 'A0174404L'

from itertools import combinations
from itertools import product
import copy
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

	# Remove all trivial dependencies
	non_trivial_fd = []
	for fd in singleton_fd:
		if not set(fd[1]).issubset(fd[0]):
			# print fd
			non_trivial_fd += [fd]

	# Remove extraneous attributes
	extraneous_free_fd = [None] * len(non_trivial_fd)
	for i in range(len(non_trivial_fd)):
		if len(non_trivial_fd[i][0]) > 1:   # Continue only if LHS has 2 or more attributes
			extraneous_free_fd[i] = [[], non_trivial_fd[i][1]]
			lhs = list(non_trivial_fd[i][0])
			for j in range(len(non_trivial_fd[i][0])):
				attr = non_trivial_fd[i][0][j]
				lhs.remove(attr)
				c = closure(R, non_trivial_fd, lhs)
				if not set(attr).issubset(c) and not set(non_trivial_fd[i][1]).issubset(c):
					extraneous_free_fd[i][0] += [attr]
					lhs.append(attr)
		else:
			extraneous_free_fd[i] = list(non_trivial_fd[i])

	# Remove redundant FDs
	redundant_free_fd = []
	redundant_fd = []
	for fd in extraneous_free_fd:
		removed_fd = [x for x in extraneous_free_fd if x != fd and x not in redundant_fd]
		attr = fd[0]
		c = closure(R, removed_fd, attr)
		if not set(fd[1]).issubset(c):
			redundant_free_fd += [fd]
		else:
			redundant_fd += [fd]

	minimal_cover = redundant_free_fd

	return minimal_cover

## Return all minimal covers reachable from the functional dependencies of a given schema R and functional dependencies F.
## NOTE: This function is not graded for CS4221 students.
def min_covers(R, FD):
	minimal_covers = []

	# Singleton right hand side
	singleton_fd = []
	for fd in FD:
		for rhs in fd[1]:
			singleton_fd += [[fd[0], [rhs]]]

	# Remove all trivial dependencies
	non_trivial_fd = []
	for fd in singleton_fd:
		if not set(fd[1]).issubset(fd[0]):
			# print fd
			non_trivial_fd += [fd]

	# Remove extraneous attributes for FDs where LHS contains 2 or more attributes
	extraneous_free_fd = [None] * len(non_trivial_fd)
	for i in range(len(non_trivial_fd)):
		if len(non_trivial_fd[i][0]) > 1:
			# print non_trivial_fd[i][0]
			extraneous_free_fd[i] = []
			for j in range(len(non_trivial_fd[i][0])-1):
				# Get all possible subset combinations of LHS up to length(LHS) - 1
				comb = combinations(non_trivial_fd[i][0], j + 1)
				# For each subset combination c, check if closure c can get back LHS
				for c in list(comb):
					z = list(c)
					c = closure(R, non_trivial_fd, z)
					# If yes, add on to list of extraneous_free_fd
					if set(non_trivial_fd[i][0]).issubset(c):
						extraneous_free_fd[i].append([z, non_trivial_fd[i][1]])
			# If none of the closure of any subset combinations of LHS can get back LHS, then LHS contains no extraneous attributes
			if len(extraneous_free_fd[i]) == 0:
				extraneous_free_fd[i] = list([non_trivial_fd[i]])
		else:
			extraneous_free_fd[i] = [non_trivial_fd[i]]

	# Get cartesian of FDs
	fd_cartesian = product(*extraneous_free_fd)
	fd_cartesian = list(fd_cartesian)
	for i in fd_cartesian:
		fd = list(i)
		# print '\t' + str(fd)

		# Remove redundant FDs
		redundant_free_fd = []
		redundant_fd = []
		for f in fd:
			removed_fd = [x for x in fd if x != f and x not in redundant_fd]
			attr = f[0]
			c = closure(R, removed_fd, attr)
			if not set(f[1]).issubset(c) and f not in redundant_free_fd:
				redundant_free_fd += [f]
			else:
				redundant_fd += [f]
		minimal_covers.append(copy.deepcopy(redundant_free_fd))

	return minimal_covers

## Return all minimal covers of a given schema R and functional dependencies F.
## NOTE: This function is not graded for CS4221 students.
def all_min_covers(R, FD):
	fd = all_closures(R, FD)
	return min_covers(R, fd)


### Test case from the project
R = ['A', 'B', 'C', 'D']
FD = [[['A', 'B'], ['C']], [['C'], ['D']]]

print closure(R, FD, ['A'])
print closure(R, FD, ['A', 'B'])
print all_closures(R, FD)
print candidate_keys(R, FD)

R = ['A', 'B', 'C', 'D', 'E', 'F']
FD = [[['A'], ['B', 'C']],[['B'], ['C','D']], [['D'], ['B']],[['A','B','E'], ['F']]]
print min_cover(R, FD)

R = ['A', 'B', 'C']
FD = [[['A', 'B'], ['C']],[['A'], ['B']], [['B'], ['A']]]
print min_covers(R, FD)
print all_min_covers(R, FD)

## Tutorial questions
R = ['A', 'B', 'C', 'D', 'E']
FD = [[['A', 'B'],['C']], [['D'],['D', 'B']], [['B'],['E']], [['E'],['D']], [['A', 'B', 'D'],['A', 'B', 'C', 'D']]]

print candidate_keys(R, FD)
print min_cover(R, FD)
print min_covers(R, FD)
print all_min_covers(R, FD)
