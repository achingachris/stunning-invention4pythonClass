# def isVowel(c): 
#     return (c == 'A' or c == 'E' or c == 'I' or
#             c == 'O' or c == 'U' or c == 'a' or
#             c == 'e' or c == 'i' or c == 'o' or
#             c == 'u'); 
  
  
# def pigLatin(s): 
  
#     # the index of the first vowel is stored. 
#     length = len(s); 
#     index = -1; 
#     for i in range(length): 
#         if (isVowel(s[i])): 
#             index = i; 
#             break; 
  
#     # Pig Latin is possible only if vowels 
#     # is present 
#     if (index == -1): 
#         return "-1"; 
  
#     # Take all characters after index (including 
#     # index). Append all characters which are before 
#     # index. Finally append "ay" 
#     return s[index:] + s[0:index] + "ay"; 
  
# str = pigLatin("category"); 
# if (str == "-1"): 
#     print("No vowels found. Pig Latin not possible"); 
# else: 
#     print(str); 


user_input = input("Enter word to be translated:\n")
#change_1
vowels = ['a','e','i','o','u']
def translate(user_input): 
    first = user_input[0]
#change_2
    if first in vowels: 
         user_input = user_input.lower()
         user_input += "way" 
         return user_input
    else: 
        user_input = user_input.lower()
#change_3
        for letter in user_input:
            if letter in vowels:
                index_value = user_input.index(letter)
                break
#change_4
        user_input = user_input[index_value:] +user_input[:index_value]+ "ay" 
        return user_input 

print(translate(user_input))