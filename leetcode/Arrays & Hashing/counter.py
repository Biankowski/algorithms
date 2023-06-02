# Possível solução de um problema do leetcode - https://leetcode.com/problems/valid-anagram/description/
# A classe Counter() é capaz de receber uma string de input e transformá-la em um dicionário, onde cada letra da string será a key, e a ocorrência será o valor.


from collections import Counter

nums = '12343'

print(Counter(nums))

nums2 = "2435345"

print(Counter(nums2))