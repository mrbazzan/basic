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
    if target == "":
        return [[]]

    total = []
    for element in wordBank:
        if target.startswith(element):
            result = allConstruct(target[len(element):], wordBank)
            for seq in result:
                total.append([element, *seq])

    return total


print(allConstruct("hello", ["ab", "abc", "cd", "abcd"]))
print(allConstruct("", ["cat", "dog", "mouse"]))
print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
print(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(allConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeee"
]))

#===================allConstruct===========================
#
# NOTE: memoization does not have a lot of impact.
