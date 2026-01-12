def f(word):
    if not word:
        return ""
    wave_list = []
    for i in range(len(word)):
        wave_word = word[:i] + word[i].upper() + word[i+1:].lower()
        wave_list.append(wave_word)
    return "-".join(wave_list)
print(f("hello"))
