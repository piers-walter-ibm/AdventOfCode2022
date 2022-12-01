n="\n"
c=sorted(list(map(lambda x: sum(list(map(int,x.split(n)))),open("input.txt").read().split(n*2))))
print(c[-1],sum(c[-3:]))