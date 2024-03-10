import random;
from hangman_art import stages;
from hangman_words import word_list;
from hangman_art import logo;

print(logo);

choosen_word = random.choice(word_list);
guessed_word = [];
hit = 0;
isHit = False;
lives = 6;

for i in range(0, len(choosen_word)):
    guessed_word.append('_');

while(hit < len(choosen_word) and lives > -1):
    guessed_letter = input("Guess a letter: ").lower();
    isHit = False;

    if guessed_word.count(guessed_letter) == 0:
        for i in range(0, len(choosen_word)):
            if choosen_word[i] == guessed_letter:
                guessed_word[i] = guessed_letter;
                hit += 1;
                isHit = True;
    else:
      print(f"You already guessed the letter { guessed_letter }");
      isHit = True;

    print("".join(guessed_word));
    if not isHit:
        print(stages[lives]);
        lives -= 1;

print("");
if lives == -1:
    print("You lost!");
    print(f"The correct word is { choosen_word }");
else:
    print("You won!");