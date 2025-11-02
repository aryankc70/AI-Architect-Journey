#for loop
scores = [95,92,78,95,88]
for score in scores:
    print(f"Score: {score}")

# while loop
count = 0
while count < 5:
    print(f"Count: {count}")
    count +=1

# loop with conditionals
for score in scores:
    if score >=90:
        print(f"{score} is excellent!")
    else:
        print(f"{score} needs improvement.")

scores.append(56)
print(scores)
scores.remove(92)
scores.sort()
print(scores)