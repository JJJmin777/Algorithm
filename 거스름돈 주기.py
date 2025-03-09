def solution(amount):
    denominations = [1, 10, 50, 100]
    denominations.sort(reverse=True)

    change = []

    for coin in denominations:
        while amount >= coin:
            change.append(coin)
            amount -= coin

    return change

print(solution(123)) # 반환값 : [100, 10, 10, 1, 1, 1]
print(solution(350)) # 반환값 : [100, 100, 100, 50]