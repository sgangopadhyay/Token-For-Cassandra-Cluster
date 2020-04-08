# PROGRAM NAME : Token Generation for Apache Cassandra Nodes
# PROGRAMMER : SUMAN GANGOPADHYAY
# DATE : 01-April-2020
# PYTHON : 3.7
# APACHE CASSANDRA : 3.11

import sys
if (len(sys.argv) > 1):
    num=int(sys.argv[1])
else:
    num=int(input("Number of Cassandra Clusters : "))
    print("")
for i in range(1, num +1):
    token = int(i*(2**127)/num)
    print("Token ",i," : ",token)