#===================canConstruct===========================

# target - a string
# wordBank - an array of strings
#
# return a boolean indicating whether or not the "target" can
# be constructed by concatenating elements of the "wordBank"
# array.
#
# elements of "wordBank" can be re-used

def canConstruct(target, wordBank, memory={}):

    if target in memory:
        return memory[target]

    if target == "":
        return True

    for element in wordBank:
        if target.startswith(element):
            remainder = target[len(element):]

            if canConstruct(remainder, wordBank, memory):
                memory[target] = True
                return True

    memory[target] = False
    return False


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

