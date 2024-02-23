A = 10
print(id(A))

B = A
print(id(B))

C = D = E = 50
print("C:{0} D:{1} E:{2}".format(C, D, E)) # deprecated formated

F, G, H = 10, 20, 30 
print("F:%d G:%d H:%d" %(F, G, H))
