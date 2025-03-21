print("__________________________________________________")
def count_lower_upper(s):
   
    lower_count = 0
    upper_count = 0
    
    
    for char in s:
        if char.islower():
            lower_count += 1
        elif char.isupper():
            upper_count += 1
    
    
    return {"lowercase": lower_count, "uppercase": upper_count}


sample_string = "Hello World! Python IS Fun"
result = count_lower_upper(sample_string)
print(result)
print("__________________________________________________")
def compute(n):
    
    n_str = str(n)
    
    result = int(n_str) + int(n_str*2) + int(n_str*3) + int(n_str*4)
    return result


for digit in range(4, 8):
    print(f"Result for n={digit}: {compute(digit)}")

print("__________________________________________________")
import numpy as np

def create_array(depth, rows, cols, initial_value):
    
    array = np.full((depth, rows, cols), initial_value)
    return array

depth = 3
rows = 4
cols = 5
initial_value = 7

array = create_array(depth, rows, cols, initial_value)


print(array)
print("__________________________________________________")
def sum_avg(marks):
    total = sum(marks)
    avg = total / len(marks)
    return total, avg


marks = [85, 90, 78, 92, 88]
total, avg = sum_avg(marks)
print(f"Total: {total}, Average: {avg}")
print("__________________________________________________")
def ispangram(sentence):
    alphabet_set = set('abcdefghijklmnopqrstuvwxyz')
    sentence_set = set(sentence.lower())
    return alphabet_set <= sentence_set


test_strings = [
    "The quick brown fox jumps over the lazy dog",
    "Crazy Fredrick bought many very exquisite opal jewels"
]

for s in test_strings:
    print(f"'{s}' is a pangram: {ispangram(s)}")

print("__________________________________________________")
def create_tuples_list(end):
    return [(x, x**2, x**3) for x in range(1, end+1)]


end_value = 5
result = create_tuples_list(end_value)
print(result)

print("__________________________________________________")
def ispalindrome(s):
    cleaned_str = ''.join(s.split()).lower()
    return cleaned_str == cleaned_str[::-1]


test_strings = [
    "A man a plan a canal Panama",
    "hello"
]

for s in test_strings:
    print(f"'{s}' is a palindrome: {ispalindrome(s)}")

print("__________________________________________________")
def convert(s):
    words = s.split()
    unique_words = sorted(set(words))
    return ' '.join(unique_words)


sentence = "the quick brown fox the quick brown dog"
result = convert(sentence)
print(result)

print("__________________________________________________")
def count_alpha_digits(s):
    counts = {'alphabets': 0, 'digits': 0}
    for char in s:
        if char.isalpha():
            counts['alphabets'] += 1
        elif char.isdigit():
            counts['digits'] += 1
    return counts


input_str = "Hello123, this is 456."
result = count_alpha_digits(input_str)
print(result)
print("__________________________________________________")
def frequency(s):
    words = s.split()
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    sorted_word_freq = dict(sorted(word_freq.items()))
    return sorted_word_freq


sentence = "hello world hello python hello"
result = frequency(sentence)
print(result)

print("__________________________________________________")
def create_list(list1, list2):
    return list(set(list1) & set(list2))


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = create_list(list1, list2)
print(result)

print("__________________________________________________")


