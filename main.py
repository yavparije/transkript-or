primer = "глУхонький"
nothingvow = "аоуэ"
softvow = "и"
jvow = "еёюя"
vow = "аоуэиеёюя"
# звонкий + глухой = звонкий
dingcon = ["б", "в", "г", "д", "ж", "з"]
shhcon = ["п", "ф", "к", "т", "ш", "с"]
reducts = {"а": ["а", "а", "ь"], "о": ["о", "а", "ъ"], "у": ["у", "у", "ъ"], "э": ["э", "э", "ъ"], "и": ["и", "и", "ь"],
           "е": ["'э", "'и", "'ь"], "ё": ["'о", "'о", "'о"], "ю": ["'у", "'у", "'ъ"], "я": ["'а", "'а", "'ь"]}


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
    return ans, reds


def softness(word):
    ans = [word[0]]
    prev = word[0]
    for i in range(1, len(word)):
        if word[i] == "ь":
            ans.append("'")
            ans.append(word[i])
        elif word[i] == "ъ" and prev == "'":
            ans.pop()
    ret = ''
    for c in ans:
        ret += c
    return ret


print(reduction(primer))


def transcr(word: str, stress: int):
    n = len(word)
    phoword = word
    return f"[{phoword}]"
