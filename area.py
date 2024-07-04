def areaRectangle(length,breadth):
    area=length*breadth
    return area

def main():
    print('Enter the following values for rectangle')
    lengthRect=int(input('Length'))
    breadthRect=int(input('Breadth'))
    areaRect=areaRectangle(lengthRect,breadthRect)
    print('Area of rectangle is', areaRect)

if __name__=='__main__':
    main()
print('\nEnd of program')     