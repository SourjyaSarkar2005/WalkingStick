import sys

class program():
	def __init__(self, filename, c_list, execstring):

		self.filename = filename
		self.c_list = []
		self.execstring = """ """

		# opening the text file
		with open(self.filename,'r') as file:
		   
		    # reading each line    
		    for line in file:
	
		        # reading each word        
		        for word in line.split():

		        	if isinstance(word, str):
		        		self.c_list.append(word)

		        	if word == "times":
		        		word = "*"
		        	else:
		        		try:
				        	if int(word) != 0:
				        		word = int(word)
				        		del self.c_list[-1]
				        	elif float(word) != 0:
				        		word = float(word)
				        		del self.c_list[-1]

				        except:
				        	continue

		        	self.c_list.append(word)

	def prepare(self):
		functions = ("say", "know", "=")
		operators = ("+", "-", "*", "/")

		for i in range(len(self.c_list)):

			# Checking if it is a function
			if self.c_list[i] in functions:

				# Variable assignment and "know" function
				if self.c_list[i] == "=":
					if self.c_list[i+1] == "know":
						if self.c_list[i+2] == "number":
							pequi = f"{self.c_list[i-1]} = int(input({self.c_list[i+3]}))"
							self.execstring += f"\n{pequi}"
						else:
							pequi = f"{self.c_list[i-1]} = input({self.c_list[i+2]})"
							self.execstring += f"\n{pequi}"							
					else:
						pequi = f"{self.c_list[i-1]} = {self.c_list[i+1]}"
						self.execstring += f"\n{pequi}"

				# The "say" function
				if self.c_list[i] == "say":

					try:
						# Basic "say" syntax
						if i+2 > (len(self.c_list) - 1):
							pequi = f"print({self.c_list[i+1]})"
							self.execstring += f"\n{pequi}"

						# With operators in syntax
						elif self.c_list[i+2] in operators:
							
							if isinstance(self.c_list[i+1], int) or isinstance(self.c_list[i+1], float):
								pequi = f"print({self.c_list[i+1]} {self.c_list[i+2]} {self.c_list[i+3]})"
								self.execstring += f"\n{pequi}"
							else:
								pequi = f"print({self.c_list[i+1]} + ' ' {self.c_list[i+2]} {self.c_list[i+3]})"
								self.execstring += f"\n{pequi}"

						# With "times" operator in syntax
						elif self.c_list[i+3] == "*":
							pequi = f"print({self.c_list[i+1]} * {self.c_list[i+2]})"
							self.execstring += f"\n{pequi}"
					except:
						print("Compilation error. Possibly, syntax is wrong.")
						sys.exit()


	def execute(self):
		try:
			print("\nDebug components:")
			print(self.c_list)
			print(self.execstring)
			print("\nProgram:")
			exec(self.execstring)
			print()
		except:
			print("Execution error. Logical error most proabably.")


filename = input("Enter file path: ")
p = program(filename, None, None)
p.prepare()
p.execute()