#question 2
#testing
#return testing
import random 
import numpy as np 
import hashlib
import math


def calculateHeavyHitters():
  totalNumElements = 0
  heavyHitters = []
  dataStream = createDataStream()
  for tup in dataStream:
    freq = tup[1]
    totalNumElements += freq

  #threshold of 1% of total frequencies
  threshold = totalNumElements * 0.01 #Threshold = 879.25
  for tup in dataStream:
    if tup[1] >= threshold:
      heavyHitters.append(tup[0])

  return heavyHitters


  #frequencies required:
  #values: 1:1000; freq: 1
  #values: 1001:2000; freq: 2
  #values: 2001:3000; freq: 3
  #values: 3001:4000; freq: 4
  #... 
  #8001:9000; freq: 9
  #value: 9001; freq: 1
  #value: 9002; freq: 4
  #value: 9003; freq: 9
  #value: 9004; freq: 16 etc etc 
def createDataStream():
  dataStream = []
  for i in range(9):
    freq = i + 1
    for j in range(1000):
      value = j + i * 1000
      dataStream.append((value, freq))
  
  for j in range(50):
    i = j + 1
    freq = math.pow(i,2)
    value = 9000 + i 
    dataStream.append((value, freq))
    
  return dataStream 
  
  
def createDecreasingDataStream():
  dataStreamToReverse = createDataStream()
  dataStream = list(reversed(dataStreamToReverse))
  return dataStream


def createRandomDataStream():
  dataStreamTuples = createDataStream()
  dataStream = []
  for tup in dataStreamTuples:
    freq = tup[1]
    for i in range(int(freq)):
      dataStream.append(tup[0])


  random.shuffle(dataStream)
  return dataStream


def isHeavyHitter(minFrequency):
  if minFrequency > 879:
    return True
  else:
    return False

def RandomOrder(hashTable1, hashTable2, hashTable3, hashTable4, i):
  dataStream = createRandomDataStream()
  minFreq9050 = None
  heavyHittersClub = []

  for data in dataStream:
    #for each of the 4 independent hash tables
    x = data
    countFrequencies = []

    for j in range(4):

      newX = str(x) + str(i-1)

      #Calculate the MD5 score of the resulting string

      hexHash = hashlib.md5(newX).hexdigest()

      #The hash value is the j-th byte of the score.
      #incrementSlot is the decimal value 
      byteArray = bytearray.fromhex(hexHash)
      incrementSlot = byteArray[j + 1]


      #increment the count 
      if(j == 0):
        countFrequencies.append(hashTable1[incrementSlot])  
      elif(j == 1):
        countFrequencies.append(hashTable2[incrementSlot])
      elif(j == 2):
        countFrequencies.append(hashTable3[incrementSlot])
      elif(j == 3):
        countFrequencies.append(hashTable4[incrementSlot])

    minFrequency = min(countFrequencies)
    if(x == 9050):
      minFreq9050 = minFrequency
    if(isHeavyHitter(minFrequency)):
      heavyHittersClub.append(x)

  return minFreq9050, heavyHittersClub

def nonIncreasingOrder(hashTable1, hashTable2, hashTable3, hashTable4, i):
  dataStream = createDecreasingDataStream()
  minFreq9050 = None
  heavyHittersClub = []

  for numFrequencyPair in dataStream:
    #for each of the 4 independent hash tables
    x = numFrequencyPair[0]
    frequency = numFrequencyPair[1]
    countFrequencies = []

    for j in range(4):

      newX = str(x) + str(i-1)

      #Calculate the MD5 score of the resulting string

      hexHash = hashlib.md5(newX).hexdigest()

      #The hash value is the j-th byte of the score.
      #incrementSlot is the decimal value 
      byteArray = bytearray.fromhex(hexHash)
      incrementSlot = byteArray[j + 1]


      #increment the count 
      if(j == 0):
        countFrequencies.append(hashTable1[incrementSlot])  
      elif(j == 1):
        countFrequencies.append(hashTable2[incrementSlot])
      elif(j == 2):
        countFrequencies.append(hashTable3[incrementSlot])
      elif(j == 3):
        countFrequencies.append(hashTable4[incrementSlot])

    minFrequency = min(countFrequencies)
    if(x == 9050):
      minFreq9050 = minFrequency
    if(isHeavyHitter(minFrequency)):
      heavyHittersClub.append(x)

  return minFreq9050, heavyHittersClub

def nonDecreasingOrder(hashTable1, hashTable2, hashTable3, hashTable4, i):
  dataStream = createDataStream()
  minFreq9050 = None
  heavyHittersClub = []

  for numFrequencyPair in dataStream:
    #for each of the 4 independent hash tables
    x = numFrequencyPair[0]
    frequency = numFrequencyPair[1]
    countFrequencies = []

    for j in range(4):

      newX = str(x) + str(i-1)

      #Calculate the MD5 score of the resulting string

      hexHash = hashlib.md5(newX).hexdigest()

      #The hash value is the j-th byte of the score.
      #incrementSlot is the decimal value 
      byteArray = bytearray.fromhex(hexHash)
      incrementSlot = byteArray[j + 1]


      #increment the count 
      if(j == 0):
        countFrequencies.append(hashTable1[incrementSlot])  
      elif(j == 1):
        countFrequencies.append(hashTable2[incrementSlot])
      elif(j == 2):
        countFrequencies.append(hashTable3[incrementSlot])
      elif(j == 3):
        countFrequencies.append(hashTable4[incrementSlot])

    minFrequency = min(countFrequencies)
    if(x == 9050):
      minFreq9050 = minFrequency
    if(isHeavyHitter(minFrequency)):
      heavyHittersClub.append(x)

  return minFreq9050, heavyHittersClub

def countMinSketchReverse(i):
  dataStream = createDecreasingDataStream()
  # print dataStream
  hashTable1 = [0]*256
  hashTable2 = [0]*256
  hashTable3 = [0]*256
  hashTable4 = [0]*256
  count = 0
  for numFrequencyPair in dataStream:
    count += 1
    #for each of the 4 independent hash tables
    x = numFrequencyPair[0]
    frequency = numFrequencyPair[1]
  

    for j in range(4):

      newX = str(x) + str(i-1)
      
      
      #Calculate the MD5 score of the resulting string
      

      hexHash = hashlib.md5(newX).hexdigest()
      
      #The hash value is the j-th byte of the score.
      #incrementSlot is the decimal value 
      byteArray = bytearray.fromhex(hexHash)
      incrementSlot = byteArray[j + 1]
      
      
      #increment the count 
      if(j == 0):
        hashTable1[incrementSlot] += frequency
      elif(j == 1):
        hashTable2[incrementSlot] += frequency
      elif(j == 2):
        hashTable3[incrementSlot] += frequency
      elif(j == 3):
        hashTable4[incrementSlot] += frequency

    # print(hashTable1)

  return nonIncreasingOrder(hashTable1, hashTable2, hashTable3, hashTable4, i)


  
def countMinSketchRandom(i):
  dataStream = createRandomDataStream()
  # print dataStream
  hashTable1 = [0]*256
  hashTable2 = [0]*256
  hashTable3 = [0]*256
  hashTable4 = [0]*256
  count = 0
  for data in dataStream:
    count += 1
    #for each of the 4 independent hash tables
    x = data
  

    for j in range(4):

      newX = str(x) + str(i-1)
      
      
      #Calculate the MD5 score of the resulting string
      

      hexHash = hashlib.md5(newX).hexdigest()
      
      #The hash value is the j-th byte of the score.
      #incrementSlot is the decimal value 
      byteArray = bytearray.fromhex(hexHash)
      incrementSlot = byteArray[j + 1]
      
      
      #increment the count 
      if(j == 0):
        hashTable1[incrementSlot] += 1
      elif(j == 1):
        hashTable2[incrementSlot] += 1
      elif(j == 2):
        hashTable3[incrementSlot] += 1
      elif(j == 3):
        hashTable4[incrementSlot] += 1

    # print(hashTable1)

  return RandomOrder(hashTable1, hashTable2, hashTable3, hashTable4, i)
      

  
def countMinSketch(i):
  dataStream = createDataStream()
  # print dataStream
  hashTable1 = [0]*256
  hashTable2 = [0]*256
  hashTable3 = [0]*256
  hashTable4 = [0]*256
  count = 0
  for numFrequencyPair in dataStream:
    count += 1
    #for each of the 4 independent hash tables
    x = numFrequencyPair[0]
    frequency = numFrequencyPair[1]
    

    for j in range(4):

      newX = str(x) + str(i-1)
      
      
      #Calculate the MD5 score of the resulting string
      

      hexHash = hashlib.md5(newX).hexdigest()
      
      #The hash value is the j-th byte of the score.
      #incrementSlot is the decimal value 
      byteArray = bytearray.fromhex(hexHash)
      incrementSlot = byteArray[j + 1]
    
      
      #increment the count 
      if(j == 0):
        hashTable1[incrementSlot] += frequency
      elif(j == 1):
        hashTable2[incrementSlot] += frequency
      elif(j == 2):
        hashTable3[incrementSlot] += frequency
      elif(j == 3):
        hashTable4[incrementSlot] += frequency

    # print(hashTable1)

  return nonDecreasingOrder(hashTable1, hashTable2, hashTable3, hashTable4, i)
      
def callerFunction():
  #9050
  lastNumFrequencyGuess = []
  numHeavyHitters = []
  for x in range(1, 11):
    minFreq9050, heavyHittersClub = countMinSketch(x)
    lastNumFrequencyGuess.append(minFreq9050)
    numHeavyHitters.append(len(set(heavyHittersClub)))
    
  #print the value averaged over the 10 trials
  print "Non Decreasing Order:"
  print sum(lastNumFrequencyGuess) / float(len(lastNumFrequencyGuess))
  print sum(numHeavyHitters) / float(len(numHeavyHitters))


  lastNumFrequencyGuess = []
  numHeavyHitters = []
  for x in range(1, 11):
    minFreq9050, heavyHittersClub = countMinSketchReverse(x)
    lastNumFrequencyGuess.append(minFreq9050)
    numHeavyHitters.append(len(set(heavyHittersClub)))

  #print the value averaged over the 10 trials
  print "Non Increasing Order:"
  print sum(lastNumFrequencyGuess) / float(len(lastNumFrequencyGuess))
  print sum(numHeavyHitters) / float(len(numHeavyHitters))


  lastNumFrequencyGuess = []
  numHeavyHitters = []
  for x in range(1, 11):
    minFreq9050, heavyHittersClub = countMinSketchRandom(x)
    lastNumFrequencyGuess.append(minFreq9050)
    numHeavyHitters.append(len(set(heavyHittersClub)))

  #print the value averaged over the 10 trials
  print "Random Order:"
  print sum(lastNumFrequencyGuess) / float(len(lastNumFrequencyGuess))
  print sum(numHeavyHitters) / float(len(numHeavyHitters))

  
callerFunction()
