'''. Stwórz program “Zgadnij jakie to słowo”. Program ma działać w następujący sposób: program powinien przechowywać kilka słów do odgadnięcia wraz z krótkim opisem.
 Na początku rozgrywki program losuje słowo, następnie każda litera ze sowa jest zamieniania na znak podłogi “_” i wyświetla użytkownikowi.
 Zadaniem gracz jest odgadnięcie słowa, gracz może podawać po jednym literze i jeżeli będzie występować dana litera w słowie to wyświetl w odpowiednim miejscu.
 Gracz może podać całe słowo sprawdź czy podane słowo zgadza się z zagadką, jeżeli tak to poinformuj o poprawnym odgadnięciu, jeżeli nie to poinformuj o dalszych próbach.
 Program powinien zliczać po którym kroku gracz odgadł szukane słowo.'''
import random

def guess_word():
    words = ["butterfly", "mouse", "chamster", "cat", "dog"]
    random_number = random.randint(0,4)
    random_word =words[random_number]
    letters_guessed = 0
    word_to_guess = []
    iterations = 0
    for i in random_word:
        word_to_guess.append('_')
    while(letters_guessed < len(word_to_guess)):
        print(word_to_guess)
        i = input("Write a letter or word to guess\n")
        iterations += 1
        is_in_word = False
        if(len(i)== 1):
            for x in range(len(random_word)):
                if(i[0] == random_word[x]):
                    word_to_guess[x] = i[0]
                    letters_guessed += 1
                    is_in_word = True
            if(is_in_word):
                print("You guessed the letter correctly\n")
            else:
                print("The letter is not in the guessing word\n")
        else:
            if(i == random_word):
                letters_guessed = len(random_word)
                for x in range(len(random_word)):
                    word_to_guess[x] = random_word[x]
                break
            else:
                print("The word you guessed is not correctly\n")
    print(word_to_guess)
    print("Congratulations you guessed the word correctly\n")

