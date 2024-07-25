def reverse(s):
    return s[:-1][::-1] + "\0"

print(reverse("abcd\0"))