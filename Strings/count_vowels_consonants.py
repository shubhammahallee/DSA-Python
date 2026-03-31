ch = input().lower()

vowel = 0
consonant = 0

for i in ch:
    if i in "aeiou":
        vowel += 1
    elif i.isalpha():
        consonant += 1

print(f"Vowels: {vowel}, Consonants: {consonant}")
