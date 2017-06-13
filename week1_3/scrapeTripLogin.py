import requests, re
from lxml import html

EMAIL = "2593099419@qq.com"
PASSWORD = "238604"
LOGIN_URL = "https://cn.tripadvisor.com/RegistrationController?flow=content_submission&pid=39776&returnTo=%2FSaves%2F63421440&fullscreen=true"
URL = "https://cn.tripadvisor.com/Saves/63421440"

def main():
    session = requests.session()
    result = session.get(LOGIN_URL)
    print(result.text)


if __name__ == '__main__':
    main()