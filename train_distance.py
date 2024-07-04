#Distance Traveled by Two Trains together in the same Direction
# Python3 program to find the distance
# traveled together by the two trains

# Function to find the distance 
# traveled together
def calc_distance(A, B, n):

	# Stores distance travelled by A
	distance_traveled_A = 0

	# Stores distance travelled by B
	distance_traveled_B = 0

	# Stores the total distance
	# travelled together
	answer = 0

	for i in range(5):

		# Sum of distance travelled
		distance_traveled_A += A[i]
		distance_traveled_B += B[i]

		# Condition for traveling
		# together
		if ((distance_traveled_A ==
			distance_traveled_B) and
			(A[i] == B[i])):
			answer += A[i]
	
	return answer

# Driver Code
A = [ 1, 2, 3, 2, 4 ] 
B = [ 2, 1, 3, 1, 4 ]

N = len(A)

print(calc_distance(A, B, N))

