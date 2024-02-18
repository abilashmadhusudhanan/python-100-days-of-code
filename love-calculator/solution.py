person1_name = input("Enter the name of the first person: ")
person2_name = input("Enter the name of the second person: ")

normalized_string = (person1_name.replace(" ", "") + person2_name.replace(" ", "")).lower()
normalized_string_len = len(normalized_string)
freq = [0] * 26
occurences_of_true = 0
occurences_of_love = 0

for i in range(0, normalized_string_len):
    freq[ord(normalized_string[i]) - 97] += 1

occurences_of_true = freq[ord("t") - 97] + freq[ord("r") - 97] + freq[ord("u") - 97] + freq[ord("e") - 97]
occurences_of_love = freq[ord("l") - 97] + freq[ord("o") - 97] + freq[ord("v") - 97] + freq[ord("e") - 97]

score = int(str(occurences_of_true) + str(occurences_of_love))

if score < 50:
    print("Your socre is low")
elif score >= 50 and score < 75:
    print("Your score is good")
else:
    print("Your score is excellent")