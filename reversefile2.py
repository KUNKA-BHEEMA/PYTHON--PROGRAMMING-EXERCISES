'''
reverse content of file
on giving text file name which is present in the same 
directory, content get reversed.
if not, display message file not found

'''

print(end="Enter File's Name: ")
fname = input()

try:
  fhand = open(fname, "r")

  fcont = ""
  for cont in fhand:
    fcont = fcont + cont

  print("\n----Content of \"" +str(fname)+ "\" in Original Order----")
  print(fcont)
  print("\n----Content of \"" +str(fname)+ "\" in Reverse Order----")
  fcont = fcont[::-1]
  print(fcont)

except IOError:
  print("\nThe file doesn't exist!")

