import sys

sys.setrecursionlimit(10000)

def solution(c, num, infos):
    if costs[num] >= c:
        answers.append(num)
        return
    
    for value, customer in infos:
        if costs[num] + customer > costs[num+value]:
            costs[num+value] = costs[num] + customer #update
            solution(c, num+value, infos)
            


if __name__ == '__main__':
    c, n = map(int,input().split())# customer, num of city
    infos =  [list(map(int, input().strip().split())) for _ in range(n)]
    costs = [0] * 100 * 1000 + [0] # dp[비용] = 사람수
    answers = []
    solution(c, 0, infos)
    print(min(answers))