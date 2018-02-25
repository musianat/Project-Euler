
end = 1000
threes = list(range(3,end,3))
fives  = list(range(5,end,5))
threesAndFives= threes + list(set(fives) - set(threes))
print(sum(threesAndFives))