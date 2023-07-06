#===================allConstruct===========================

# target - a string
# wordBank - an array of strings
#
# return a 2D array containing all of the ways that 
# the "target" can be  constructed by concatenating
# elements of the "wordBank" array.
#
# elements of "wordBank" can be re-used

def allConstruct(target, wordBank):
    length = len(target)
    arr = [[] for _ in range(length+1)]
    arr[0] = [[]]

    for i, state in enumerate(arr):
        for element in wordBank:
            word = i + len(element)
            if state and (word <= length):
                if target[i:word] == element:
                    arr[word] += [ w + [element] for w in arr[i]]

    return arr[length]


print(allConstruct("hello", ["ab", "abc", "cd", "abcd"]))
print(allConstruct("", ["cat", "dog", "mouse"]))
print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
print(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(allConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(allConstruct("eeeeeeeeeeeeeeeeee", [
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeee"
]))
#===================allConstruct===========================
