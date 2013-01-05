import os,sys

class MyDemo:
  def callWhile(self):
    while True:
      reply = input('Enter text:')
      if reply == 'stop':
        break
      elif not reply.isdigit():
        print('Bad!' * 8)
      else:
        print(int(reply) ** 2)
    print('Bye')

  def callTryExcept(self):
    while True:
      reply = input('Enter text:')
      if reply == 'stop':
        break
      try:
        num = int(reply)
      except:
        print('Bad!' * 8)
      else:
        print(int(reply) ** 2)
    print('Bye')
  def callAssign(self):
    for (a,b,c) in [(1,2,3), (4,5,6)]:
      print("a = {0}, b = {1}, c = {2}".format(a,b,c))

    for ((a,b), c) in [((1,2), 'aaa'), (('x', 'y'), 'good job')]:
      print("a = {0}, b = {1}, c = {2}".format(a,b,c))
  def callWhile(self):
    L = [1, 2, 3, 4]
    while L:
#      front, L = L[0], L[1:]
      front = L.pop(0)
      print(front, L)
    L = [4, 5, 6, 7]
    while L:
      front, *L = L
      print(front, L)

  def callListConcatenation(self):
    L = M = [1, 2]
    M += [3, 4]
    print(L, M)

    L = M = [1, 2]
    M = M + [3, 4]
    print(L, M)

  def callPrint(self):
    x = 'abc'
    y = 99
    z = ['1', 'cc']
    print(x, y, z, sep=' => ', end = '...\n')
    print(x, y, z, sep=' => ', end = '...\n', file=open('output/data.txt', 'w'))

  def callWriteToFile(self):
    sys.stdout = open('output/data.txt', 'a')
    print('good', 'job', 'ya')

  def callStdOut(self):
    temp = sys.stdout
    sys.stdout = open('output/data.txt', 'a')
    print('good', 'job', '斌')
    sys.stdout.close()
    sys.stdout = temp
    print('張', '宏', '斌')


if __name__ == '__main__':
  app = MyDemo()
  app.callStdOut()