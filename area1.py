def areaRectangle(length,breadth):
    area=length*breadth
    return area


def areaSquare(side):
    area=areaRectangle(side,side)
    return area

def main():
    print('Enter the following values for rectangle')
    lengthRect=int(input('Length'))
    breadthRect=int(input('Breadth'))
    areaRect=areaRectangle(lengthRect,breadthRect)
    print('Area of rectangle is', areaRect)
    sideSqr=int(input('Enter side of the squre'))
    areaSqr=areaSquare(sideSqr)
    print('Area of square is ', areaSqr)

if __name__=='__main__':
    main()

print('\nEnd of program')      