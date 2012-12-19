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

        

if __name__ == '__main__':
    app = MyTuples()
    app.doSort()

