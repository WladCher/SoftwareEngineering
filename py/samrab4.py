import re

with open("input.txt", encoding="utf-8") as file:
    forbidden = file.read().split()

sample_text = "Приветствие, Спасибо, Ты готов? До завтра! Вчера было тепло"

for term in forbidden:
    mask = re.compile(term, re.IGNORECASE)
    sample_text = mask.sub("*" * len(term), sample_text)

print(sample_text)