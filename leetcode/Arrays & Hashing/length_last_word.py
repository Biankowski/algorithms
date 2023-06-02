## Works but it isn't efficient O(n)?
# def length_of_last_word(s):
#     s = s.strip()
#     s_arr = s.split(" ")
    
#     output = len(s_arr[-1])
#     print(output)

def length_of_last_word(s):
    s = s.strip()
    space_index = s.rfind(" ")
    word = s[space_index + 1:]
    print(word)
    
length_of_last_word("Hello World  moon")