
# C3 ALGORITHM

def merge(seqs):

    res = [];
    while True:
      nonemptyseqs=[seq for seq in seqs if seq]
      if not nonemptyseqs: return res

      # find merge candidates among seq heads
      for seq in nonemptyseqs:
          cand = seq[0]
          nothead=[s for s in nonemptyseqs if cand in s[1:]]

          if nothead: cand=None #reject candidate
          else: break

      if not cand: raise "Inconsistent hierarchy"
      res.append(cand)
      for seq in nonemptyseqs: # remove cand
          if seq[0] == cand: del seq[0]


def mro(k):
    def inner(klass):
        b = []
        for k in klass:
            b += [[k] + inner(k.__bases__)]
        return b

    return merge([[k]] + [inner(k.__bases__)] + [list(k.__bases__)])

class Example:
    class D: pass
    class E: pass
    class F: pass
    class X(F): pass
    class B(D,E): pass
    class C(D,F): pass
    class A(B,C): pass


import pprint; pprint.pprint(mro(Example.C))
