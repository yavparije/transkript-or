# тестовые примеры: молокО, глУхонький, снЕдь, предэкзаменациОнный
# длинношеее
primer = input()
nothingvow = "аоуэ"
softvow = "и"
jvow = "еёюя"
vow = "аоуэиеёюя"
a = chr(39)  # апостроф / знак мягкости
# звонкий + глухой = звонкий
dingcon = ["б", "в", "г", "д", "ж", "з"]
shhcon = ["п", "ф", "к", "т", "ш", "с"]
paircons = {'п': 'б', 'ф': 'в', 'к': 'г', 'т': 'д', 'ш': 'ж', 'с': 'з'}
reducts = {"а": ["а́", "а", "ъ"], "о": ["о́", "а", "ъ"], "у": ["у́", "у", "ъ"], "э": ["э́", "э", "ъ"],
           "и": [f"{a}и́", f"{a}и", f"{a}ь"],
           "е": [f"{a}э́", f"{a}и", f"{a}ь"], "ё": [f"{a}о́", f"{a}о́", f"{a}о́"], "ю": [f"{a}у́", f"{a}у", f"{a}ъ"],
           "я": [f"{a}а́", f"{a}а", f"{a}ь"]}


def reduction(word: str) -> str:
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
    for i in range(len(result)):
        if result[i] == 'ъ' and result[i - 1] == a:
            result[i] = 'ь'
    for i in reds:
        result[i[1]] = i[0]
    #        print(i, result)
    ans = ""
    for i in result:
        ans += i
    return ans


def softness(word: str) -> str:
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


def assimilation(word: str):
    ans = [word[0]]
    prev = word[0]
    for i in range(1, len(word)):
        if word[i] == prev:
            ans.pop()
            ans.append(f'{prev}:')
        elif prev in shhcon and word[i] in dingcon:
            ans.pop()
            ans.append(paircons[prev])
            ans.append(word[i])
        else:
            ans.append(word[i])
        prev = word[i]
    ret = ''
    for c in ans:
        ret += c
    return ret


def transcr(word: str) -> str:
    n = len(word)
    phoword = reduction(softness(assimilation(word)))
    return f"[{phoword}]"


print(transcr(primer))
