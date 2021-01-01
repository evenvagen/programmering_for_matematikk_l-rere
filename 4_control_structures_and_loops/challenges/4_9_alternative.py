word = "Googolplex"
new_word = ""
for i in range(len(word), 0, -1):
    new_word = new_word + word[i - 1]
print(new_word)

concat_numbers = ""
for i in range(11, -1, -1):
    concat_numbers = concat_numbers + ' ' + str(i)
print(concat_numbers)




