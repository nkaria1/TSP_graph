# Filename: 		TSP_demo_start.py
# Creatde by: 		Niharika Karia [A20364461]
# Created on: 		8 Dec 2015

	
#usr/bin/python
welcome="""Welcome to the Demo for TSP algorithms. \nThis demo is prepared by Graduate student, Niharika Karia [A20364461], of Illinois Institute of technology. You may begin testing."""
print welcome
options="""The available options are: \n \t 1. Brute force \n \t 2. Greedy \n \t 3. Branch and Bound \n \t 4. Exit """

choice = 0
while choice != 4:
	print options
   	choice = int(input("enter choice"))
	if choice==1:
		print ("we are implementing Brute force method.")
		import TSP_A1_BruteForce
	if choice==2:
		print ("we are implementing Greedy method.")
		import TSP_A2_Greedy
	if choice==3:
		print ("we are implementing Branch and Bound method.")
		import TSP_A3_BranchNBound_naive
	if choice==4:
		print ("Exiting")

print (" Have a nice day. :)")
