N, M, K = map(int, input().split())

data = list(map(int, input().split()))

data.sort(reverse=True)

first_data = data[0]
second_data = data[1]

first_count = M // (K + 1) * K + M % (K + 1)
second_count = M - first_count

result = first_data * first_count + second_data * second_count

print(result)