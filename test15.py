'''
WAP to count frequency of characters in a given file.Can u use character frequency to test whether the given file is Python program file, C program file or a text file
'''

f = r"C:\Users\goura\Desktop\python\PEARSON\CHAPTER-15\filecontent.txt"
file = open ( f, "r" )

a=[]

b={}

for i in file:

    for j in range(0,len(i)):

        a.append(i[j])

for i in a:

    if i in b:

        b[i]+=1

    else:

        b[i]=1

print(b)

c=f.split(".")

if c[1]=="txt":

    print("\n\nit is a text file")

elif c[1]=="cpp":

    print("\n\nit is a c++ file")

else:

    print("\n\nit is a c file")

