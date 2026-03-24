s1 = input("enter first word")
s2 = input("enter second word")

s1_sorted = sorted(s1)
s2_sorted = sorted(s2)

if s1 == s2:
    print("Anagram")
else:
    print("Not Anagram")
