import Queue

def isPrime(num):
    if num > 1:
        i = 2
        while i*i <= num:
            if num % i == 0:
                return False
            i += 1
        return True
    else:
        return False 


def queue_and_stack (inputArr):
    q = Queue.Queue()
    s = []
    for i in inputArr:
        if isPrime(i):
            q.put(i)
        else:
            s.append(i)
    while not q.empty():
        print q.get(),
    print 
    s.reverse()
    print ' '.join([str(i) for i in s])

inputArr = []
n = int(input())
data = raw_input().split()
for i in range(n):
    inputArr.append(int(data[i]))

out_ = queue_and_stack(inputArr)
