import os

def erase_love_live(S:str) -> str:
    S = S.replace('lovelive!', '')
    return S

def get_upper_str(S:str) -> str:
    tmp = []
    #大文字を集める
    for i in range(len(S)):
        if S[i].isupper() or S[i] == '{' or S[i] == '}':
            tmp.append(S[i])
    #３文字の頭のアルファベットのみを抽出
    flag = []
    for i in range(0,len(tmp),3):
        if tmp[i].isupper():
            flag.append(tmp[i].lower())
        else:
            flag.append(tmp[i])
    return ''.join(flag)

def main() -> str:
    path = os.getcwd()
    path = path+'/CpawCTF/Level 2/Q18/misc100'
    with open(path) as m:
        S = m.read()
        not_love_live = erase_love_live(S)
        flag = get_upper_str(not_love_live)
        print(flag)

if __name__ == "__main__":
    main()
