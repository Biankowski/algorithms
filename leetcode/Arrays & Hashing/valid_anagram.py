from collections import Counter

# Bad version - sorting takes too much time
def is_anagram(s, t):
    sort_s = ""
    sort_t = ""
    for letter in s:
        sort_s += "".join(sorted(letter))
    s_dict = Counter(sort_s)
    for letter in t:
        sort_t += "".join(sorted(letter))
    t_dict = Counter(sort_t)
        
    if s_dict == t_dict:
        print('True')
    else:
        print('False')

# Better version  
def isAnagram(s, t):
        dict_s = {}
        dict_t = {}

        for letter in s:
            if letter in dict_s:
                dict_s[letter] += 1
            else:
                dict_s[letter] = 1
        for letter in t:
            if letter in dict_t:
                dict_t[letter] += 1
            else:
                dict_t[letter] = 1
        if dict_s == dict_t:
            return True
        return False
        
        
is_anagram("anagram", "anagram")
is_anagram("rat", "car")
is_anagram("ab", "ba")