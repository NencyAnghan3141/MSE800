dict1 = {'a':1,'b':2 ,'c':3}
dict2 = {'d':4, 'e':5,'f':6}


merged_dict = {**{k: v for k, v in dict1.items() if k in 'aeiou'},
               **{k: v for k, v in dict2.items() if k in 'aeiou'}}
print(merged_dict)


# Output: {'a': 1, 'e': 5}
# The merged dictionary contains only the keys 'a' and 'e' from dict1 and dict2, respectively.
# This is because the dictionary comprehension filters the keys based on the condition that they are vowels.
# The merged dictionary contains only the keys 'a' and 'e' from dict1 and dict2, respectively.