import requests, re, itertools
from lxml import html

EMAIL = "2593099419@qq.com"
PASSWORD = "238604"
CSRFTOKEN = ""
LOGIN_URL = "https://cn.tripadvisor.com/RegistrationController?flow=content_submission&pid=39776&returnTo=%2FSaves%2F63421440&fullscreen=true"
URL = "https://cn.tripadvisor.com/Saves/63421440"

def main():
    session = requests.session()
    result = session.get(LOGIN_URL)
    pattern = re.compile(".+data-csrf-token=\"(.+?)\"")
    # print(result.text)
    with open("tripadvisor.html", "w") as file:
        file.write(result.text)
    with open("tripadvisor.html", "r") as text_file:
        for line in itertools.islice(text_file, 390, 400):
            m = pattern.match(line)
            if m:
                CSRFTOKEN = m.group(1)
                print(CSRFTOKEN)
                break
    payload = {
        "email" : EMAIL,"Invalid Checkin date: Please enter a valid checkin and checkout dates,entered date is already passed"
        "password" : PASSWORD,
        "csrfToken" : CSRFTOKEN
    }
    result = session.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))
    result = session.get(URL, headers = dict(referer = URL))
    print(result.text)
if __name__ == '__main__':
    main()