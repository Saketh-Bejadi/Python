a = input("Enter input :")
s = ''
f = '01111110'
l = []
s1 = []
c = 0
x = ''
for i in a:
    if i == '1':
        c += 1
        s = s + i
        s1.append(i)
    else:
        c = 0
        s = s + i
        s1.append(i)
    if c == 5:
        s = s + '0'
        s1.append('!')
        
print("transmitted Data :",f +' ' + s + ' ' + f)

for i in s1:
    if i != '!':
        l.append(i)
        x = x + i
print("Reciverside :",x)
        



    
        
        
        