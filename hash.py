import hashlib

def generateMD5(stringData):
    result = hashlib.md5(stringData.encode())
    print(result.hexdigest())


generateMD5("Bootcamp")
