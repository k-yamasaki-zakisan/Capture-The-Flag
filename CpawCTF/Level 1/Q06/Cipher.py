#アルファベットを３文字戻すスクリプトを記述
def main(N:int) -> str:
    ans = []
    for n in N:
        ord_s = ord(n)
        if ord_s <= 90:
            ord_s -= 3
            if ord_s < 65:
                ord_s += 26
        else:
            ord_s -= 3
            if ord_s < 97:
                ord_s += 26
    
        chr_s = chr(ord_s)
        if n == '{':
            ans.append('{')
        elif n == '_':
            ans.append('_')
        elif n == '}':
            ans.append('}')
        else:
            ans.append(chr_s)
    return ''.join(ans)


if __name__ == "__main__":
    N = list(input())
    result = main(N)
    print(result)
