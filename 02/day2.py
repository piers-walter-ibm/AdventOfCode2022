def calcScoreP1(me, opponent):
    score=(ord(me)-ord(opponent)-23) # Result Diff
    # 0 is win, 1 is loss, 2 is draw, 3 is win
    if score == -2: # -2 is same as 1 for win
        score = 1
    elif score == 2: # 2 is same as -2 for loss
        score = -1

    score += 1
    score=((score)*3)+(ord(me)-87) # 3*res
    return score


def part1(filename):
    inputText = open(filename,"r").read().splitlines()
    rounds = list(map(lambda x: x.split(" "),inputText))
    score = 0
    for round in rounds:
        me = round[1] # X,Y,Z
        opponent = round[0] # A,B,C
        score+=calcScoreP1(me, opponent)

    return score

def calcScoreP2(op, outcome):
    op = ord(op)-64 # 1,2,3
    match outcome:
        case "X": # lose, 
            op = op-1
            if op == 0:
                op = 3
            return op

        case "Y": # draw, pick same as opp 
            return op + 3

        case "Z":
            op += 1
            if op == 4:
                op = 1
            op += 6
            
    return op
            

def part2(filename):
    inputText = open(filename,"r").read().splitlines()
    rounds = list(map(lambda x: x.split(" "),inputText))
    score = 0
    for round in rounds:
        score += calcScoreP2(round[0], round[1])

    return score
    
if __name__ == '__main__':  # pragma: no cover
    filename = "demo.txt"
    print(f"Part 1: {part1(filename)}")
    print(f"Part 2: {part2(filename)}")