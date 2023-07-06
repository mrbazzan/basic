#===================canConstruct===========================

# target - a string
# wordBank - an array of strings
#
# return a boolean indicating whether or not the "target" can
# be constructed by concatenating elements of the "wordBank"
# array.
#
# elements of "wordBank" can be re-used

def canConstruct(target, wordBank):

    length = len(target)
    arr = [False for _ in range(length+1)]
    arr[0] = True

    for i, state in enumerate(arr):
        for element in wordBank:
            word = i + len(element)
            if state and (word <= length) :
                if target[i:word] == element:
                    arr[word] = True


    return arr[length]

print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(canConstruct("", ["cat", "dog", "mouse"]))
print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeee"
]))
#===================canConstruct============================

