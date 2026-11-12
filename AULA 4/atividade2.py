l1 = int(input('>>'))
l2 = int(input('>>'))
l3 = int(input('>>'))

if l1  != l2 != l3 and l3 != l2 != l1 and l3 != l1 :
   print('Escaleno')
elif l1 == l2 == l3  and l3 == l1:
   print('Equilatero')
else: 
   print('isoceles')
