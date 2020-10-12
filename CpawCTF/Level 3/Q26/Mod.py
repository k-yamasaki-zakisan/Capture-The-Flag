def main():
    for i in range(1000000):
        k = i * 3438478 + 193127
        if k % 1584891 == 32134:
            print('答え：{}, 余り1:{}, 余り2:{}'.format(k,k%1584891,k%3438478))
            break

if __name__ == "__main__":
    main()

