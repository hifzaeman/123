word1 = "listen"
word2 = "silent"

# Check if they have same letters with same occurrences
if sorted(word1) == sorted(word2) and word1 != word2:
    print("They have the same letters and same occurrences but in different order.")
else:
    print("They do NOT match the condition.")
