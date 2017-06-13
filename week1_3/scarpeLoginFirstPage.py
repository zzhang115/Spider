import requests, re
from lxml import html

USERNAME = "blueghost98@sina.cn"
PASSWORD = "23860423"
authenticity_token = ""
LOGIN_URL = "https://bitbucket.org/account/signin/?next=/"
URL = "https://bitbucket.org/dashboard/projects"

def main():
    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)
    # print(result.text)
    tree = html.fromstring(result.text)
    pattern = re.compile('.+([\r|\n]+.+)+.+?name=\'csrfmiddlewaretoken\'.*value=\'(.+?)\'')
    m = pattern.match(result.text)
    if m:
        authenticity_token = m.group(2)
    # authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]
    # authenticity_token = list(set(tree.xpath("//input[@type='hidden']/@name")))[0]
    # print("authenticity_token:", authenticity_token)

    # Create payload
    payload = {
        "username": USERNAME,
        "password": PASSWORD,
        "csrfmiddlewaretoken": authenticity_token
    }

    # Perform login
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))
    # # Scrape url
    result = session_requests.get(URL, headers = dict(referer = URL))
    print(result.text)
    # tree = html.fromstring(result.content)
    # bucket_names = tree.xpath("//div[@class='repo-list--repo']/a/text()")
    #
    # print(bucket_names)

if __name__ == '__main__':
    main()

# payload = {
#     "UserName" : "",
#     "Password" : "",
#     "hidToken" : ""
# }

# from __future__ import print_function
# import argparse
# import mechanicalsoup
# from getpass import getpass
#
# parser = argparse.ArgumentParser(description="Login to GitHub.")
# parser.add_argument("username")
# #parser.add_argument("username")
# args = parser.parse_args()
#
# args.password = getpass("Please enter your GitHub password: ")
#
# browser = mechanicalsoup.StatefulBrowser(
#     soup_config={'features': 'lxml'},
#     raise_on_404=True
# )
# # Uncomment for a more verbose output:
# # browser.set_verbose(2)
# print("**********************************")
# browser.open("https://github.com")
# browser.follow_link("login")
# browser.select_form('#login form')
# browser["login"] = args.username
# browser["password"] = args.password
# resp = browser.submit_selected()
#
# # Uncomment to launch a web browser on the current page:
# # browser.launch_browser()
#
# # verify we are now logged in
# page = browser.get_current_page()
# messages = page.find("div", class_="flash-messages")
# if messages:
#     print(messages.text)
# assert page.select(".logout-form")
#
# print(page.title.text)
#
# # verify we remain logged in (thanks to cookies) as we browse the rest of
# # the site
# page3 = browser.open("https://github.com/hickford/MechanicalSoup")
# assert page3.soup.select(".logout-form")