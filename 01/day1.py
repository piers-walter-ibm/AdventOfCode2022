
def getElvesTotals(filename):
    inputText = open(filename,"r").read()
    elvesRaw = inputText.split("\n\n")

    elves = map(sumElf, elvesRaw)

    return elves

def sumElf(elf):
    return sum(map(int,elf.split("\n")))

def part1(filename):
    elves = getElvesTotals(filename)
    return max(elves)

def part2(filename):
    # Turn iterator into a list
    elves = list(getElvesTotals(filename))
    elves.sort()
    top3Elves = sum(elves[-3:])

    return top3Elves
    
if __name__ == '__main__':  # pragma: no cover
    print(f"Part 1: {part1('input.txt')}")
    print(f"Part 2: {part2('input.txt')}")