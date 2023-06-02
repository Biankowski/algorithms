from collections import Counter, defaultdict
   
#def group_anagrams(strs):
#     grouped = defaultdict(list)
    
#     for i in strs:
#         words = "".join(sorted(i))
#         grouped[words].append(i)
        
#     output = list(grouped.values())
#     print(output)
    
    
def group_anagrams(strs):
    word_dict = {}
    
    for i in strs:
        words = "".join(sorted(i))
        if words in word_dict:
            word_dict[words].append(i)
        else:
            word_dict[words] = [i]
    
    output = list(word_dict.values())
    print(output)
    
    
group_anagrams(["eat","tea","tan","ate","nat","bat"])