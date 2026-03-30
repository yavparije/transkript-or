primer = "глУхонький"
nothingvow = "аоуэ"
softvow = "и"
jvow = "еёюя"
vow = "аоуэиеёюя"
a = chr(39)  # апостроф / знак мягкости
# звонкий + глухой = звонкий
dingcon = ["б", "в", "г", "д", "ж", "з"]
shhcon = ["п", "ф", "к", "т", "ш", "с"]
reducts = {"а": ["а", "а", "ь"], "о": ["о", "а", "ъ"], "у": ["у", "у", "ъ"], "э": ["э", "э", "ъ"],
           "и": [f"{a}и", f"{a}и", f"{a}ь"],
           "е": [f"{a}э", f"{a}и", f"{a}ь"], "ё": [f"{a}о", f"{a}о", f"{a}о"], "ю": ["'у", "'у", "'ъ"],
           "я": [f"{a}а", f"{a}а", f"{a}ь"]}


def reduction(word):
    reds = []
    udar = False
    for i in range(len(word)):
        c = word[i]
        low = c.lower()
        if low in vow:
            if ord(c) < ord("а"):
                if reds:
                    reds[-1] = (reducts[prev[0]][1], prev[1])
                reds.append((reducts[low][0], i))
                udar = True
            elif udar:
                reds.append((reducts[low][2], i))
                udar = False
            else:
                reds.append((reducts[low][2], i))
            prev = (low, i)
    result = []
    for c in word:
        result.append(c)
    for i in reds:
        result[i[1]] = i[0]
        print(i, result)
    ans = ""
    for i in result:
        ans += i
    return ans


def softness(word):
    ans = [word[0]]
    prev = word[0]
    for i in range(1, len(word)):
        if word[i] == "ь":
            ans.append(a)
            ans.append(word[i])
        elif word[i] == "ъ" and prev == a:
            ans.pop()
        else:
            ans.append(word[i])
    ret = ''
    for c in ans:
        ret += c
    return ret


def transcr(word: str):
    n = len(word)
    phoword = reduction(softness(word))
    return f"[{phoword}]"


print(transcr(primer))
