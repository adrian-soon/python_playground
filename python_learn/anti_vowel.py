def anti_vowel(text):
    vowel = "aeiouAEIOU"
    result = ""
    for each in text:
        if each in "aeiouAEIOU":
            continue
        else:
            result += each
    
    return result
        