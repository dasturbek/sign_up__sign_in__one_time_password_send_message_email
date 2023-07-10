import json


def shefr():
    key = "abc"
    infor = {
        "open_key": "123456",
        "text": "Bekzod/dasturbek/dasturbek@gmail.com",
        "comp_name": "salom",
        "comp_key": "123456"
    }

    if len(key) != 0:
        for x in infor:
            strt = infor[x]
            shefr = ""
            if len(key) > len(strt):
                key = key[0:(len(strt) - 1)]
            for i in range(len(strt)):
                shefr += str(chr((ord(strt[i]) + ord(key[i % len(key)])) % 256))
            strt = shefr
            infor[x] = strt

    with open("sample2.json", "w") as outfile:
        json.dump(infor, outfile)


def deshefr(file):
    key = "abc"
    with open(file, 'r') as outfile:
        infor = json.load(outfile)

    if len(key) != 0:
        for x in infor:
            strt = infor[x]
            deshefr = ""
            if len(key) > len(strt):
                key = key[0:(len(strt) - 1)]
            for i in range(len(strt)):
                deshefr += str(chr((ord(strt[i]) - ord(key[i % len(key)])) % 256))
            strt = deshefr
            infor[x] = strt

    return infor


