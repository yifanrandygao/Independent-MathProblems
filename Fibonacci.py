import sys

j = 2
k = 7
modval = 256

val = "8675309"

# if (len(sys.argv) > 1):
#     val = str(sys.argv[1])
# if (len(sys.argv) > 2):
#     modval = int(sys.argv[2])


def conv(val):
    arr = []
    for i in range(len(val)):
        arr.append(int(val[i]))
    return arr

def squared_number():
    while True:
        input_var = input('Number to enter: ')
        if input_var =='stop':
            break
        try:
            input_var_num = float(input_var)
        except:
            print ('Please enter a number!')
        else:
            print (input_var_num**2)

# def showvals(val, j, k):
#     for i in range(len(val)):
#         if (i == j - 1):
#             print("[%3d]" % val[i], end='')
#         elif (i == k - 1):
#             print("[%3d]" % val[i], end='')
#         else:
#             print("%3d" % val[i], end='')


s = conv(val)

print("j=", j, " k=", k)
print("Seed:\t", val)

if (len(s) < k):
    print("Value needs to be larger than 7")
    exit()

# showvals(s, j, k)
arr1 = []
for n in range(100):
    out = (s[j - 1] + s[k - 1]) % modval
    arr1.append(out)
    for i in range(len(s) - 1):
        s[i] = s[i + 1]
    s[len(s) - 1] = out