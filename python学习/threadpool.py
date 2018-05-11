from concurrent import futures

MAX_WORKS = 20

def worker(cc):
    print("{}hello".format(cc))

def many_workers(cc_list):
    with futures.ThreadPoolExecutor(MAX_WORKS) as executor:
        res = executor.map(worker,cc_list)
    print(res)
    return len(list(res))

cc_list = []
for i in range(100):
    cc_list.append(i)
    many_workers(cc_list)