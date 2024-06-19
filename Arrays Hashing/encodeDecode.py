def encode(strs):

    to_ret = ""
    for word in strs:
        to_ret += word + "#"
    return (to_ret)

def decode(s):


    temp = s.split("#")

    return temp[:-1]


encode(["neet","code","love","you"])

print(decode(encode(["neet","code","love","you"])))