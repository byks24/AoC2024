from functools import cache
with open("text.txt", "r") as file:
  stones = []
  for line in file:
    for i in line.strip().split():
        print(i)
        number = int(i)  
        stones.append(number)


@cache
def count(stone,steps):
    if steps == 0:
        return 1
    if stone ==0:
        return count(1,steps-1)
    string = str(stone)
    length = len(string)
    if length % 2 ==0:
        return count(int(string[:length // 2]), steps - 1) + count(int(string[length //2:]),steps - 1)
    return count(stone * 2024, steps - 1)
print(sum(count(stone, 75)for stone in stones))