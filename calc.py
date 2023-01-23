import sys
def add(n1, n2):
    return n1+n2

def mul(n1,n2):
    return n1*n2

def divabs(n1, n2):
    return n1//n2

if(len(sys.argv) < 4):
    print("Error: Usage: python script.py num1 num2 operation")
    exit()
n1 = int(sys.argv[1])
n2 = int(sys.argv[2])

function_toRun = sys.argv[3]

ret = 0
print("Operation Passed : {}".format(function_toRun))
try:
    if (function_toRun == "add"):
        ret = add(n1, n2)
    elif(function_toRun == "mul"):
        ret = mul(n1,n2)
    elif(function_toRun == "div"):
        if(n2==0):
            print("Division by Zero Not Possible !")
            exit()
        else:
            ret = divabs(n1,n2)

    else:
        ret = "Invalid Operation Passed"
    print(ret)
except:
    print("Error!!")
