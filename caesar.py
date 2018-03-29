def alphabet_position(char):
    if ord(char)>64 and ord(char)<91:
        return ord(char) - 65
    if ord(char)>96 and ord(char)<123: 
        return ord(char) - 97
    return ord(char)

def rotate_character(char, rot):
    adj_rot = rot
    if alphabet_position(char) + adj_rot > 25:
        while alphabet_position(char) + adj_rot > 25:
            adj_rot = adj_rot - 26
        return chr(adj_rot + ord(char))
    if 96<ord(char) and 123>ord(char):
        if ord(char) + rot>122:
            return chr(rot + ord(char) - 26)
        return chr(ord(char) + rot)
    return char

def encrypt(text, rot):
    new_str = ""
    for i in range(len(text)):
        if text[i].isalpha():
            new_str = new_str + rotate_character(text[i], rot)
        else:
            new_str = new_str + text[i]
    return new_str
