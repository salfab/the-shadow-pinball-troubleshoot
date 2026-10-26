import sys

path, new_section_path = sys.argv[1], sys.argv[2]
with open(path, "r", encoding="utf-8", newline="") as f:
    text = f.read()
with open(new_section_path, "r", encoding="utf-8", newline="") as f:
    new_section = f.read()

nl = "\r\n" if "\r\n" in text else "\n"
start = text.index("## 8. Prochaine étape")
end = text.index("## 9. Questions en suspens")
new_section = new_section.replace("\r\n", "\n").rstrip("\n") + "\n\n"
text = text[:start] + new_section.replace("\n", nl) + text[end:]

with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(text)
print("ok")
