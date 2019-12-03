user_array = list(input().split(','))
fixed_array = [1, 2, 3, 4, 5]

result = []
def reverse(list):
  for _ in range(len(list)):
    result.insert(0, list.pop(0))
  return result

# print(reverse(fixed_array))
print(reverse(user_array))