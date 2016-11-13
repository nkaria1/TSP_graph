# Filename: 		TSP_A3_BruteForce.py
# Creatde by: 		Niharika Karia [A20364461]
# Created on: 		23 Nov 2015


#usr/bin/python

def route(s,num,cost):
	st=s
	#cost=[[6,2,3],[4,5,2],[7,3,9]]
	total=0
	num.remove(s)
	#print num
	min=1000
	while (len(num)!=0):
		#find nearest neighbour of 's' from rem, say 'a'
		min=1000
		for i in range (0,len(num)):
			if (cost[s-1][num[i]-1]<min):
				min=cost[s-1][num[i]-1]
				a=num[i]
		print "nearest neighbour from %d is %d at distance :%d" %(s,a,min)
		total=total+min
		num.remove(a)	#changes the index of other nodes in num
		s=a #a is the new s
	#now add the length of path from a-st
	print "The distance from %d to starting point %d :%d" %(a,st,cost[a-1][st-1])
	total=total+cost[a-1][st-1]

	print "\nTotal cost of route = %d" %total
	return;
		

num=[]
cost=[]
n=0
z=input("enter the number of nodes you wish to include:")
a=1
for an in range(1,z+1):
	num.append(an)
print num
#for i in range (1,z+1):
#	node_cost_list=[]
#	for j in range (1,z+1):	
#		w= int(raw_input("the distance from %d to %d: " %(i,j)))
#		node_cost_list.append(w)
#	cost.append(node_cost_list)
#print cost
cost=[[1, 1, 2, 2,3,4,5,23,35,46,57,12,24,21,4,5,21,3,31,5,8,7,7,6,13,4,5,7,7,6],
      [2,6,34,1,21,3,31,5,8,22, 3, 3,7,4,6, 21,3, 43,2,1,11,12,13,42,53,31,53,18,19,20],
 [4,2,6,7,21,3,31,5,8,7,4,6, 21,3, 8,20,30,40,12,24,82,27,51,11,13,12, 5,2,4, 56], 
[6,2,5,45,21,3,31,5,8,32,41,7,4,6, 21,3,12,3,26,81,7,4,6, 21,3,13,20,6, 7, 7],
[1,3,6,12,35,46,74,23,14,30,31,21,3,31,5,8,7,4,6, 21,3,31,5,8,5,8,5,3,6,10],
[34,5,3,8,1,6,41,11,1,21,3,31,5,8,4,23,6,34,26,6,41,11,1,4,12,5,7,1,7,2],
[4,5,21,3,31,5,8,12,4,17,8,2,9,16,13,4,34,45,6,41,11,1,4,56,12,13,17,81,51,40],
[14,2,3,45,3,4,5,8,20,11,6,41,11,1,4,14,15,3,21,3,31,5,8,4,5,6,7,8,9,10],
[10,9,8,21,3,31,5,8,7,6,5,4,3,21,42,53,6,41,11,1,4,74,35,4,36,7,9,3,2,1],
[32,12,23,34,45,16,17,46,13,9,2,21,3,31,5,8,6,41,11,1,4,4,6,8,10,12,14,16,18,20],[11,3,6,31,31,5,8,6,41,11,1,21,3,31,5,8,4,5,8,5,3,61,12,35,75,53,42,31,20,10,3],
[13,2,21,3,31,5,8,11,14,15,32,12,6,6,4,6,41,11,1,4,3,2,1,41,7,4,6,1,15,7],
[10,9,8,7,8,10,12,14,14,16,18,1,21,3,31,5,8,6,41,11,1,4,3,4,4,5,6,7,8,9],
[16,13,4,56,12,31,65,24,47,82,13,6,41,11,1,4,23,1,5,1,21,3,31,5,8,2,11,14,15,3],
[18,2,3,45,3,4,5,8,4,23,6,30,40,17,46,13,9,2,21,3,31,5,8,12,24,82,34,26,20,11],
[1,2,30,40,17,46,13,9,2,12,24,82,3,4,23,6,34,26,45,3,4,5,8,20,11,21,3,31,5,8],
[21,3,31,5,8,17,46,13,9,2,1,2,3,45,3,4,5,8,20,11,4,23,6,34,26,30,40,12,24,82],
[30,40,12,24,17,46,13,9,2,82,4,23,6,21,3,31,5,8,34,26,1,2,3,45,3,4,5,8,20,11],
[17,46,13,9,2,1,2,4,23,6,34,26,3,45,3,21,3,31,5,8,4,30,40,12,24,82,5,8,20,11],
[1,2,3,45,3,4,4,23,6,34,26,5,8,20,17,46,13,9,2,21,3,31,5,8,11,30,40,12,24,82],
[2,6,21,3,31,5,8,3,56,43,2,8,5,9,17,18,19,10,23,72,18,37,29,19,10,22,55,33,12,25],
[10,9,8,7,6,5,6,41,11,1,21,3,31,5,8,4,40,17,46,13,9,2,5,8,5,3,11,1,4,5],
[6,41,21,3,31,5,8,40,17,11,1,4,5,46,13,9,2,11,1,4,5,8,5,3,10,9,8,7,6,5],
[32,12,6,3,4,5,23,35,46,57,12,24,11,21,3,31,5,8,1,4,14,15,21,6,4,6,41,11,1,4,],
[40,17,46,3,21,3,31,5,8,4,5,23,35,46,57,12,24,21,32,12,6,6,4,6,41,11,1,4,13,2,],
[5,8,7,4,6, 21,3,31,5,8,6,41,11,5,8,1,3,6,12,35,12,24,82,3,4,23,6,34,26,45,],
[12,24,82,3,4,23,6,34,26,45,5,8,7,4,5,8,6,41,11,6, 21,3,31,5,8,11,3,6,31,3],
[1,3,6,12,9,8,7,8,10,12,5,8,6,41,11,14,14,16,18,1,35,5,8,7,4,6, 21,3,31,5,8],
[12,24,82,5,8,7,4,6, 21,3,31,5,8,3,4,23,5,8,6,41,11,6,34,26,45,11,3,6,31,3],
[5,8,7,4,6, 21,3,31,11,3,6,5,8,6,41,11,31,3,5,8,1,3,6,12,35,5,8,6,41,11]
]

s=input("enter the starting node: ")

route(s,num,cost)
print "program completed. Have a happy day."

