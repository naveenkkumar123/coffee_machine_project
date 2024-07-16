inputs_lists = input().split(".")

str = ""
for i in range(len(inputs_lists)):
    c = inputs_lists[i][0]
    str += c

print("".join(sorted(str)))
