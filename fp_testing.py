import sys
import requests as re

print(sys.version)
print(sys.executable)


def greet(who):
    greeting = "Hello, {}".format(who)
    return greeting


r = re.get("https://coreyms.com")
print(r.status_code)
