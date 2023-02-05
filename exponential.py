from pylab import plot, show, legend, title, xlabel, ylabel
import numpy as np

def program():
    b = int(round((y2/y1)**(1/(x2-x1))))
    a = int(round((y1/b**x1)))

    x = np.linspace(x1+10,x1-10, endpoint = True)
    y = (a * np.exp(b*x)) 

    plot(x,y)
    plot(x1,y1,'r*')
    plot(x2,y2,'r*')
    legend([[x1,y1],[x2,y2]])
    title("y = {0}*{1}^x".format(a,b))
    show()

if __name__ == '__main__':
    x1 = int(input("Enter your x1 value: "))
    y1 = int(input("Enter your y1 value: "))
    x2 = int(input("Enter your x2 value: "))
    y2 = int(input("Enter your y2 value: "))

    program()


