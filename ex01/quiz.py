import random
quizu = {}
quiz["問題1"] = {"問題":"サザエさんの旦那さんの名前は？"}
quiz["問題2"] = {"問題":"カツオの妹の名前は？"}
quiz["問題3"] = {"問題":"タラオはカツオから見てどんな関係？"}

random.choice(list(quiz.items()))

print(random.choice(quiz))

