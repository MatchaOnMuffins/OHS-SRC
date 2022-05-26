import datetime
import pyrebase
import requests.exceptions
import sys
import json

config_json = open(r"auth/config.json")

config = json.load(config_json)


def db_init() -> bool:
    try:
        firebase = pyrebase.initialize_app(config)
        global db
        db = firebase.database()
        global stream
        stream = db.child("coms").child("msg").stream(stream_handler)
        return True
    except Exception as e:
        print(e)
        return False


def stream_handler(message):
    try:
        print(f"{message['data']['author']}: "
              f"{message['data']['content']} at "
              f"{message['data']['time']}")
    except KeyError:
        pass


def send(content: str, author: str):
    message = {
        "content": f"{content}",
        "author": f"{author}",
        "time": f"{datetime.datetime.utcnow()}"
    }
    try:
        db.child("coms").child("msg").push(message)
        return True
    except requests.exceptions.ConnectionError:
        return False


if __name__ == "__main__":
    user = input("Who are you? >>>")
    if db_init():
        if send(f"{user} has logged in!", user):
            print(f"{user} has logged in!")
        else:
            sys.exit(1)
    else:
        sys.exit(1)
    try:
        while True:
            msg = input()
            if msg == "exit()":
                break
            if send(msg, user):
                continue
            else:
                print("error!")
                continue

        stream.close()
        sys.exit(0)
    except NameError:
        print("database undefined.")
