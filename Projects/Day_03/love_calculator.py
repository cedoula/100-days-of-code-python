print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

list_name = [name1, name2]
#Count number of occurences of letters in True
true_count = 0
for name in list_name:
  for letter in "true":
    count_letter = name.lower().count(letter)
    true_count += count_letter
#Count number of occurences of letters in Love
love_count = 0
for name in list_name:
  for letter in "love":
    count_letter = name.lower().count(letter)
    love_count += count_letter

#Combine counts
score = int(str(true_count) + str(love_count))

#Print output depending on score
if score < 10 or score > 90:
  print(f'Your score is {score}, you go together like coke and mentos.')
elif score >= 40 and score <= 50:
  print(f'Your score is {score}, you are alright together.')
else:
  print(f'Your score is {score}.')