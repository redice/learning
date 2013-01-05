import os, sys
import pickle
import struct

class TheFile:
  def init(self):
    print("haha")

  def writeData(self):
    myfile = open('my_file.txt', 'w')
        
    myfile.write('goodby text file\n')
    myfile.write('good job text file\n')
    myfile.close()

  def readData(self):
    for line in open('my_file.txt', 'r'):
      print(line, end='')
    #print("data = {0}".format(myfile.readline()))

  def readBinaryData(self):
    data = open('my_file.txt', 'rb').read()
    print(data)
    print(data[4:8])
    print(data[0])
    print(bin(data[0]))

  def dataObject(self):
    x, y, z = 43, 44, 45
    s = 'spam'
    d = {'a': 1, 'b': 2}
    l = [1, 2, 3]

    file = open('datafile.txt', 'w')
    file.write(s + '\n')
    file.write('{0}, {1}, {2}\n'.format(x, y, z))
    file.write("dir = {0}\n".format(d))
    file.write("array = {0}\n".format(l))
    file.close()

    file = open('datafile.txt', 'r')
    #chars = file.read()
    #print(chars)

    for line in file:
      if(line.find('dir = ') == 0):
        print(line)
        list = line.rsplit('dir = ')
        print(eval(list[1]))

  def dataStruct(self):
    file = open('data.bin', 'wb')
#    data = struct.pack('>i4sh', 7, 'spam', 8)
#    file.write(data)
    file.close()

  def dataUnstruct(self):
    file = open('data.bin', 'r')
    data = file.read()
    values = struct.unpack('>i4sh', data)
    print("value result = {0}".format(values))
  
if __name__ == "__main__":
  app = TheFile()
  app.init()
  app.dataStruct()




