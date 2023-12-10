def readvals(op):
    print("Enter two values for {} operation:".format(op))
    a,b=int(input()),int(input())
    return a,b
def addop():
    s,b=readvals("Addition")
    print("sum({},{})={}".format(s,b,s+b))
def subop():
    s,b=readvals("subtraction")
    print("sub=({},{})={}".format(s,b,s-b))
def mulop():
    s,b=readvals("Multiplication")
    print("mul=({},{})={}".format(s,b,s*b))
def divop():
    s,b=readvals("Division")
    print("div=({},{})={}".format(s,b,s/b))
def moddivop():
    s,b=readvals("Modulo Division")
    print("mod=({},{})={}".format(s,b,s%b))
def expop():
    s,b=readvals("Exponentiation")
    print("exp=({},{})={}".format(s,b,s**b))



