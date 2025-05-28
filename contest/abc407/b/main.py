X, Y =  map(int, input().split())

count = 0

for dice_1 in range(1, 7):
  for dice_2 in range(1, 7):
    if dice_1 + dice_2 >= X or abs(dice_1 - dice_2) >= Y:
      count += 1

print(count/36)
