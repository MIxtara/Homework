text = input()
data = {i: text.count(i) for i in set(text)}
