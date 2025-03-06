def solution(N):
    results = []

    def backtrack(sum, selected_nums, start):
        if sum == 10:
            results.append(selected_nums)
            return
        
        for i in range(start, N + 1):
            if sum + i <= 10:
                backtrack(
                    sum + i, selected_nums + [i], i + 1
                )

    backtrack(0, [], 1)
    return results






print(solution(5)) # 반환값 : [[1, 2, 3, 4], [1, 4, 5], [2, 3, 5]]
print(solution(2)) # 반환값 : []
print(solution(7)) # 반환값 : [[1, 2, 3, 4], [1, 2, 7], [1, 3, 6], [1, 4, 5], [2, 3, 5], [3, 7], [4, 6]]