import random

ALL_ABC = 26
T_ABC = 9
K_ABC = 2
ty = 2
ABClist = ['A','B','C','D','E','F','G','H','I']
a = random.shuffle(ABClist)
a = random.choice(ABClist)
abclist = ''
for i in ABClist:
    if i != a:
        abclist = abclist+i
print("対象文字:",ABClist)
print("欠損文字:",abclist)

ans = input("欠損文字は？")
if ans == a:
    print("正解です")
else:
    print("残念")