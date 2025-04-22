times = [int(x) for x in input("秒數: ").split()]
rounds = int(input("圈數:"))
cp = float(input("圈疲:"))
tp = float(input("趟疲:"))

def min_time(n, t):
    row = len(times)
    col = rounds - 2
    arr = [[float('inf')] * col for _ in range(row)]
    for i in range(row):
        for j in range(col):
            arr[i][j] = times[i] * (cp ** (j))
    total_time = []

    for i in range(row):
        total_time.append(arr[i][0])
        arr[i][0] *= tp
    max_search_col = 1
    k = [1] * row

    while len(total_time) < rounds:
        min_time, min_time_row, min_time_col = float('inf'), 0, 0
        for i in range(row):
            for j in range(max_search_col + 1):
                if arr[i][j] <= min_time:
                    if j == 0 and k[i] - k[-1] >= 1:
                        continue
                    min_time = arr[i][j]
                    min_time_row, min_time_col = i, j
        if min_time_col == 0:
            k[min_time_row] += 1

        total_time.append(arr[min_time_row][min_time_col])
        arr[min_time_row][min_time_col] *= tp
        max_search_col = max(max_search_col, min_time_col + 1)

    return sum(total_time)

print(min_time(rounds, times))