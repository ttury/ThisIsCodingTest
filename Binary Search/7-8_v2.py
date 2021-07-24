def binary_search(array, target, start, end):
  while(start <= end):
    mid = (start + end) // 2
    if get_food(array, mid) > target:
      start = mid + 1
      continue
    elif get_food(array, mid) < target:
      end = mid - 1
      continue
    else:
      return mid
  return mid

def get_food(sticks, height):
  result = 0
  for stick in sticks:
    if stick > height:
      result += stick - height
  return result

n, m = map(int, input().split())
sticks = list(map(int, input().split()))
print(binary_search(sticks, m, 0, max(sticks) - 1))