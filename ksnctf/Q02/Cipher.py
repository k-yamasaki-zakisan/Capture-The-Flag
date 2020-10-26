def main(N:int) -> str:
    ans = []
    for n in N:
        if n.isalpha() == False:
            ans.append(n)
            continue

        ord_s = ord(n)
        if ord_s <= 90:
            ord_s -= 13
            if ord_s < 65:
                ord_s += 26
        else:
            ord_s -= 13
            if ord_s < 97:
                ord_s += 26
    
        chr_s = chr(ord_s)
        ans.append(chr_s)
    print(''.join(ans))


if __name__ == "__main__":
    N = list('EBG KVVV vf n fvzcyr yrggre fhofgvghgvba pvcure gung ercynprf n yrggre jvgu gur yrggre KVVV yrggref nsgre vg va gur nycunorg. EBG KVVV vf na rknzcyr bs gur Pnrfne pvcure, qrirybcrq va napvrag Ebzr. Synt vf SYNTFjmtkOWFNZdjkkNH. Vafreg na haqrefpber vzzrqvngryl nsgre SYNT.')
    main(N)
