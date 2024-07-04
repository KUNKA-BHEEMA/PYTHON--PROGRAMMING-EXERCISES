#reverse the content of file
#give text file name which is present in the same directory
#give file name as filecontent.txt



print("Enter the Name of File: ")
fileName = input()

fileHandle = open(fileName, "r")
fileContent = ""
for content in fileHandle:
  fileContent = fileContent+content

print("\n----Content in Reverse Order----")
fileContent = fileContent[::-1]
print(fileContent)
