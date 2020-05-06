import time

def check(n):
    if done(n):
        return 0
    else:
        steps = recur(n)
        return steps


def recur(n):
    #print(n)
    step = 0
    digits = [int(x) for x in str(n)]
    prod = 1
    for d in digits:
        prod *= d
    
    if done(prod):
        #print(prod)
        return step + 1
    else:
        return recur(prod) + 1
    

def done(n):
    if len(str(n)) == 1:
        return True
    else:
        return False


def create_2d():
    return [[],[],[],[],[],[],[],[],[],[],[],[],[],[]]


def print_mp(result):
    index = 0
    for arr in result:
        size = len(arr)
        if size == 0:
            print("M.P. of {}: No numbers found".format(index))
        else:
            small = arr[0]
            print("M.P. of {}: {} numbers found, {} is the smallest".format(index,size,small))
        index += 1
            

def per_range(n):
    start_time = time.time()
    sums = create_2d()
    
    for x in range(n):
        sums[check(x)].append(x)
    print_mp(sums)
    print("Runtime of {}s".format(time.time() - start_time))  



def per_sel(n):
    start_time = time.time()
    
    free = ["7","8","9"]
    restricted = ["2","3","4","6","26"]
    prev_arr = [""]
    sums = create_2d()
    
    for i in range(n):                  # i represents i+1 digits of 7,8,9
        print("{} after {}s".format(i, time.time() - start_time))
        arr = []
        for p in prev_arr:              # adds a 7 to the front of each array
            arr.append(free[0] + p)
            #print(arr)
        
        nxt = free[1] * (i+1)           # a string of "8", length i+1
        arr.append(nxt)
        for j in range(i+1):            # creates all other strings length i+1 of just 8,9
            nxt = free[1] * (i-j) + free[2] * (j+1)
            arr.append(nxt)
        #print(arr)
        for r in restricted:
            for x in arr:
                num = int(r+x)
                sums[check(num)].append(num)
                #print(num)
        prev_arr = arr

    print_mp(sums)
    print("Runtime of {}s".format(time.time() - start_time))        



