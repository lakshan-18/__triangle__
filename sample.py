n=10
flames=["F", "L", "A", "M", "E", "S"]
for i in [1, 2, 3, 4, 5]:
  flames.pop((n*i)-(len(flames)*int((n*i)/len(flames)))-1)
print(flames)
