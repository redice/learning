import sys, os
import pickle

class ThePickle:
  def writePickleData(self):
    dir = {'a': '11', 'b': '22'}
    list = ['x', 'y', 'z']
    file = open('pickleData.txt', 'wb')
    pickle.dump(dir, file)
    pickle.dump(list, file)
    file.close()
          
  def readPickleData(self):
    file = open('pickleData.txt', 'rb')
    dir = pickle.load(file)
    list = pickle.load(file)
    print("dir = {0}".format(dir))
    print("list = {0}".format(list))

if __name__ == "__main__":
  app = ThePickle()
  app.writePickleData()
  app.readPickleData()