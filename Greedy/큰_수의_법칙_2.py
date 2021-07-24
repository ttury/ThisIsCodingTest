N, M, K = map(int, input().split())

data = list(map(int, input().split()))

data.sort(reverse=True)

first_data = data[0]
second_data = data[1]

result = 0
limit = 0

for _ in range(M):
  if limit < K:
    result += first_data
    print('plus first data')
    limit += 1
  else:
    result += second_data
    print('plus second data')
    limit = 0
    
print(result)