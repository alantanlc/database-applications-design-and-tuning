############################################################
## project2.py - Code template for Project 2 - Normalization
## Both for CS5421 and CS4221 students
############################################################


### IMPORTANT! Change this to your metric number for grading
student_no = 'A0174404L'


## Determine the closure of set of attribute S given the schema R and functional dependency F
def closure(R, F, S):
	# Convert S to set
	x_previous = set(S);
	x_current = []

	# while hasChanged is true
	while x_current != x_previous:
		# Update x_current with x_previous
		x_current = x_previous

		# For each FD, if FD is a subset of x_previous, update x_current with the RHS of FD
		for i in F:
			if set(i[0]).issubset(x_previous):
				x_current.update(i[1])

	return list(x_current)

## Determine the all the attribute closure excluding superkeys that are not candidate keys given the schema R and functional dependency F
def all_closures(R, F):
	return []


## Return the candidate keys of a given schema R and functional dependencies F.
## NOTE: This function is not graded for CS5421 students.
def candidate_keys(R, F):
	return []


## Return a minimal cover of the functional dependencies of a given schema R and functional dependencies F.
def min_cover(R, FD):
	return []


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
print closure(R, FD, ['A'])
print closure(R, FD, ['A', 'B'])

# print all_closures(R, FD)
# print candidate_keys(R, FD)

R = ['A', 'B', 'C', 'D', 'E', 'F']
FD = [[['A'], ['B', 'C']], [['B'], ['C', 'D']], [['D'], ['B']], [['A', 'B', 'E'], ['F']]]
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