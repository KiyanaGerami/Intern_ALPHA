import re

sentence = input("enter a sentence: ")
clean = sentence.strip()

chars_with_space = len(clean)
chars_without_space = len(clean) - clean.count(" ")

words = re.split(r'[^a-zA-Z\u0600-\u06FF]+', sentence.lower())
clean_words = [word for word in words if word]
len_words = len(clean_words)

upper = clean.upper()

reversed = clean[::-1]

count_a = sentence.lower().count("a")
slug = "_".join(sentence.lower().split())

first_word = clean_words[0]
last_word = clean_words[-1]

python = "python" in sentence

print(f"{'Sentence':<22}: {sentence}")
print(f"{'chars (with space)':<22}: {chars_with_space}")
print(f"{'chars (without space)':<22}: {chars_without_space}")
print(f"{'words:':<22}: {len_words}")
print(f"{'upper:':<22}: {upper}")
print(f"{'reversed:':<22}: {reversed}")
print(f"{'count of a:':<22}: {count_a}")
print(f"{'slug:':<22}: {slug}")
print(f"{'first word:':<22}: {first_word}")
print(f"{'last word:':<22}: {last_word}")
print(f"{'mentions python:':<22}: ", python)







