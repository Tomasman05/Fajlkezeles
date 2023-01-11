from worker import Worker

class FeketeBt:
	
	def __init__(self):
		self.workerlist = []
		self.miskolciak = 0
		self.miskolcfizu = 0
		self.gyorjutalom = 0
	def readFile(self):
		file = open("dolgozok100.txt","r",encoding="UTF-8")
		row = file.readline()
		while( row ):
			row=file.readline()
			rowsp = row.split(":")
			if( len(rowsp) > 1):
				w = Worker()
				w.name = rowsp[0]
				w.city = rowsp[1]
				w.address = rowsp[2]
				w.salary = rowsp[3]
				w.bonus = rowsp[4]
				w.born = rowsp[5]
				w.hire = rowsp[6]
				self.workerlist.append(w)
		file.close()
		print(len(self.workerlist))
	def MiskolciaAtlag(self):
		
		for worker in self.workerlist:
			if(worker.city == "Miskolc"):
				self.miskolciak+= 1
				self.miskolcfizu += float(worker.salary)
				atlag = self.miskolcfizu / self.miskolciak
		print (atlag)
		
	def Gyorijutalom(self):
		for worker in self.workerlist:
			if(worker.city == "Győr"):
				self.gyorjutalom += float(worker.bonus)
		alma = open("gyorijutalom.txt", "w", encoding = "UTF-8")
		alma.write("fasz:{} cm".format (self.gyorjutalom))
				
fb = FeketeBt()
fb.readFile()
fb.MiskolciaAtlag()
fb.Gyorijutalom()
