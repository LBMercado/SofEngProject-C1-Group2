# This class will manipulate integers and turn them into suitable indices for
# hash tables

import copy
import random

class hasher:
	#table size for this class hasher = 3000
	def __init__(self):
		#value, data, and collsnCount are parallel lists
		self.value = []
		self.data = []
		self.key = []
		self.collsnCount = []
		self.TABLE_SIZE = 3000
	
	def hash(self, value):
		#uses folding methods and rotation method if necessary
		
		#count number of digits
		value = str(value)
		numOfDigits = len(value)
		value = int(value)
		sum = 0
		
		#use folding method first
		while numOfDigits > 0:
			num = value % 1000
			sum += num
			value = int(value / 1000)
			
			numOfDigits -= 3
		
		#must keep the key 3 digits only, truncate to 3 digits
		numOfDigits = len(str(sum))
		
		while numOfDigits > 3:
			sum = int(sum / 10)
			
			numOfDigits -= 1
		
		#use rotation method
		sum = str(sum)
		
		temp = copy.deepcopy(sum)
		sum = sum[1:-1]
		sum = temp[-1:] + sum + temp[:1]
		
		return int(sum)
		
	def linearProbe(self, key):
		#this method receives the key with the collision, and uses linear probing
		if key > self.TABLE_SIZE:
			return 0
		else:
			return key + 1

	def pseudoRandomProbe(self, key):
		#this method uses pseudorandom numbers to probe
		baseNumber = random.randrange(0,self.TABLE_SIZE,1)

		if key > self.TABLE_SIZE:
			return 0
		else:
			return key + baseNumber

	def getCollsnCount(self, dataItem):
		try:
			return self.collsnCount[self.data.index(dataItem)]
		except ValueError:
			return 0
		
	def setData(self, newData):
		self.data = newData
		
	def setValue(self, newValue):
		self.value = newValue
		counter = 0
		
		for value in self.value:	
			
			temp = self.convertValToNum(value)
			self.value[counter] = temp
			
			counter += 1
		
	def convertValToNum(self, value):
		#necessary method for values with type = string
		numValue = 0
		
		#have to keep whitespaces out of this calculation
		value = value.replace(' ', '')
		
		for char in value:
			numValue += ord(char)
		
		return numValue
		
	def hashAndGetTable(self):
		#using folding method and rotation method
		
		if len(self.data) == 0 or len(self.value) == 0:
			return None
		
		for repeat in range(len(self.data)):
			self.collsnCount.append(0)
		
		table = {}
		counter = 0
		
		while counter < len(self.data):
			key = self.hash(self.value[counter])
			
			#collision checking
			while key in self.key or key > self.TABLE_SIZE:
				self.collsnCount[counter] += 1
			
				key = self.pseudoRandomProbe(key)
			
			self.key.append(key)
			
			table[key] = self.data[counter]
			
			counter += 1
		
		return table

class hashTable:

	def __init__(self, tableSize = 5000):
		#item is a list of lists

		self.item = [[None] for i in range(tableSize)]
		self.key = [[None] for i in range(tableSize)]
		self.tableSize = tableSize

	def hasKey(self, searchKey):
		if searchKey in self.key:
			return True
		else:
			return False

	def getItemWith(self, searchKey):

		return self.item[searchKey]

	def setItemWith(self, addKey, addItem):
	# Uses hash function to generate key

		addKey = self.hashNewKey(addKey)

		if addKey in self.key: #collision

			self.chainItem(addKey, addItem)

		else:

			self.item[addKey] = [addItem]
			self.key[addKey] = addKey

	def __getitem__(self, key):
		return self.getItemWith(key)

	def __setitem__(self, key, item):
		self.setItemWith(key, item)

	def hashNewKey(self, valueKey):
		#Use midCube method then modulo

		#midCube method
		hashKey = int(valueKey) * int(valueKey) * int(valueKey)

		# get digit count
		keyDigitCount = len(str(hashKey))

		#get middle
		middleDigit = round(keyDigitCount / 2)
		obtainDigitCount = middleDigit

		currentDigit = 1

		atMiddle = False
		middleKey = ''
		while not atMiddle:

			if currentDigit == middleDigit - int(obtainDigitCount / 2):

				for i in range(obtainDigitCount):
					middleKey = middleKey + (str( hashKey % 10 ))
					hashKey = int(hashKey / 10)
					keyDigitCount -= 1
				atMiddle = True

			else:
				hashKey = int(hashKey / 10)

				keyDigitCount -= 1

			currentDigit += 1

		hashKey = int(middleKey)
		keyDigitCount = len(str(hashKey))

		maxDigit = 0
		tableSize = self.tableSize

		#get maximum allowable digits
		while tableSize != 0:
			tableSize = int(tableSize / 10)
			maxDigit += 1

		#reduce digit count to maximum allowable digits in hashtable
		while keyDigitCount > maxDigit:
			hashKey = int(hashKey / 10)
			keyDigitCount -= 1

		#also if the key falls within the range of the tableSize
		if hashKey > self.tableSize:
			hashKey = hashKey % 1000

		return hashKey

	def chainItem(self, chainKey, item):
		#chains the item to the end of the list

		chainList = self.item[chainKey]

		chainList.append(item)

		self.item[chainKey] = chainList

	def getOrdSumEquiv(self, key):
		sumValue = 0

		for char in str(key):
			sumValue += ord(char)

		return sumValue