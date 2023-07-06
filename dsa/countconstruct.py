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

    if target in memory:
        return memory[target]

    if target == "":
        return 1

    total = 0
    for element in wordBank:
        if target.startswith(element):
            result = countConstruct(target[len(element):], wordBank, memory)
            total += result

    memory[target] = total
    return total


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

