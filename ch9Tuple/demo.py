import os,sys

class MyTuples:
  def doIt(self):
        print('good job!')

  def doSample(self):
        tup = (1, 2) + (3, 4)
        print("the result is {0}".format(tup))
        print("the result is {0} and {1}".format(tup[0], tup[1:3]))
        t1 = (4)
        t2 = (4,)
        print("t1 = {0}, t2 = {1}".format(t1, t2))

  def doSort(self):
        tup = ('cc', 'aa', 'bb', 'dd')
        tmp = list(tup)
        tmp.sort()
        print("data = {0}".format(tmp))
        print("data 2 = {0}".format(sorted(tup)))

        tup = (1, 2, 3, 4, 5)
        lt = [x+20 for x in tup]
        print("result = {0}".format(lt))

        tup = ('aa', 'bb', 'cc', 'aa', 'bb', 'aa')
        print("{0}, {1}, {2}".format(tup.index('aa'), tup.count('aa'), tup.index('aa', 4)))

        tup = (1, 2, [3, 4], 5)
        tup[2][1] = 'spam'
        print("result = {0}".format(tup))

  def doList(self):
    L = ['abc', [(1, 2), ([3], 4)], 5]
    print("L[1] = {0}".format(L[1]))
    print("L[1][1] = {0}".format(L[1][1]))
    print("L[1][1][0] = {0}".format(L[1][1][0]))
    print("L[1][1][0][0] = {0}".format(L[1][1][0][0]))

  def callRef(self):
    X = [1, 2, 3]
    L = ['a', X, 'b']
    D = {'x':X, 'y': 2}
    X[1] = 'surprise'
    print("D = {0}".format(D))

  def callVal(self):
    L = [1, 2, 3]
    D = {'a': 1, 'b': 2}
    A = L[:]
    B = D.copy()
    A[1] = 'Ni'
    B['c'] = 'spam'
    print("L = {0}, D = {1}".format(L, D))
    print("A = {0}, B = {1}".format(A, B))

  def callDeepCopy(self):
    import copy
    A = [1, [2, [3, 4], 5], 6]
    B = {'x':'x1', 'a':copy.deepcopy(A), 'y':'y1'}
    C = {'x':'x1', 'a':A[:], 'y':'y1'}
    A[1][1][0] = 10
    print("A = {0}".format(A))
    print("B = {0}".format(B))
    print("C = {0}".format(C))

  def testEquivalence(self):
    L1 = [1, ['a', 3]]
    L2 = [1, ['a', 3]]
    print("== => {0}, is => {1}".format(L1 == L2, L1 is L2))

  def sortForDict(self):
    D1 = {'a': 1, 'b': 2}
    D2 = {'a': 1, 'b': 3}
    print("D1 < D2 => {0}".format(sorted(D1.items()) < sorted(D2.items())))

if __name__ == '__main__':
    app = MyTuples()
    app.sortForDict()






