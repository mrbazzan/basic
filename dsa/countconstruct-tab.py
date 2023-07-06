#===================countConstruct===========================

# target - a string
# wordBank - an array of strings
#
# return the number of ways that the "target" can be
# constructed by concatenating elements of the "wordBank"
# array.
#
# elements of "wordBank" can be re-used

def countConstruct(target, wordBank, memory={}):
    arr = []
    length = len(target)
    arr = [0 for _ in range(length+1)]
    arr[0] = 1

    for i, state in enumerate(arr):
        for element in wordBank:
            word = i + len(element)
            if state and (word <= length):
                if target[i:word] == element:
                    arr[word] += arr[i]

    return arr[length]


print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(countConstruct("", ["cat", "dog", "mouse"]))
print(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeee"
]))
#===================countConstruct============================

