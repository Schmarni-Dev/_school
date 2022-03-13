from asyncio.subprocess import Process
from concurrent.futures import process
import sys
import main
import multiprocessing

def run(v,i = 0):
    n = v + 3
    i1:list[str] = [str(n),str(v)]
    i2:list[str] = ["1","3"]

    out = main.calculate(i1,i2)
    if out.split(" ")[-1] == "24/5":
        print(out,i2)

        sys.stdout.flush()


if __name__ == '__main__':
    processes:list[multiprocessing.Process] = []
    for i in range(1,201):
        # for v in range(1,200):
        #     run(v,i)
        p = multiprocessing.Process(target=run,args=(i,))
        processes.append(p)
        p.start()
    print(processes.__len__())
    for p in processes:
        p.join()
