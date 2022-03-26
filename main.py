import sys
import controller

VERSION = "./version.txt"

if __name__ == "__main__":
    title = "Hand Puppets Version: %s" % open(VERSION).read()[:-1]
    controller.Controller(title)


