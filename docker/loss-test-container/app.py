from urllib import request
from time import sleep

while True:

    print("Attempting request")
    print(request.urlopen("http://loss-entrypoint:5000/loss?url=aaaa").read())
    sleep(10)
