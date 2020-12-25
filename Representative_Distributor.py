#State Congressional Seat Distributor

#Names of states
stateNames = []
#Populations of States
statePops = []
#How much each state makes up of national population
percePops = []
#Number of representatives per state
representatives = []
#How much each state makes up of total representatives
perceRep = []
#Error between representative and population share
perceErr = []
#If all states have been added to
hasBeenAddedTo = []
#Total population
totalPop = 0
#Total Representatives
totalReps = 0

#Assign the names of each state
def Assign_Names():
	stateNames.append("California")
	stateNames.append("Texas")
	stateNames.append("Florida")
	stateNames.append("New York")
	stateNames.append("Pennsylvania")
	stateNames.append("Illinois")
	stateNames.append("Ohio")
	stateNames.append("Georgia")
	stateNames.append("North Carolina")
	stateNames.append("Michigan")
	stateNames.append("New Jersey")
	stateNames.append("Virginia")
	stateNames.append("Washington")
	stateNames.append("Arizona")
	stateNames.append("Massachusetts")
	stateNames.append("Tennessee")
	stateNames.append("Indiana")
	stateNames.append("Missouri")
	stateNames.append("Maryland")
	stateNames.append("Wisconsin")
	stateNames.append("Colorado")
	stateNames.append("Minnesota")
	stateNames.append("South Carolina")
	stateNames.append("Alabama")
	stateNames.append("Louisiana")
	stateNames.append("Kentucky")
	stateNames.append("Oregon")
	stateNames.append("Oklahoma")
	stateNames.append("Connecticut")
	stateNames.append("Utah")
	stateNames.append("Puerto Rico")
	stateNames.append("Iowa")
	stateNames.append("Nevada")
	stateNames.append("Arkansas")
	stateNames.append("Mississippi")
	stateNames.append("Kansas")
	stateNames.append("New Mexico")
	stateNames.append("Nebraska")
	stateNames.append("Idaho")
	stateNames.append("West Virginia")
	stateNames.append("Hawaii")
	stateNames.append("New Hampshire")
	stateNames.append("Maine")
	stateNames.append("Montana")
	stateNames.append("Rhode Island")
	stateNames.append("Delaware")
	stateNames.append("South Dakota")
	stateNames.append("North Dakota")
	stateNames.append("Alaska")
	stateNames.append("Washington D.C.")
	stateNames.append("Vermont")
	stateNames.append("Wyoming")
	stateNames.append("Guam")
	stateNames.append("U.S Virgin Islands")
	stateNames.append("Northern Mariana Islands")
	stateNames.append("American Samoa")

#Assigns the populations of each state
def Assign_Pops():
	statePops.append(39368078)
	statePops.append(29360759)
	statePops.append(21733312)
	statePops.append(19336776)
	statePops.append(12783254)
	statePops.append(12587530)
	statePops.append(11693217)
	statePops.append(10710017)
	statePops.append(10600823)
	statePops.append(9966555)
	statePops.append(8882371)
	statePops.append(8590563)
	statePops.append(7693612)
	statePops.append(7421401)
	statePops.append(6893574)
	statePops.append(6886834)
	statePops.append(6754953)
	statePops.append(6151548)
	statePops.append(6055802)
	statePops.append(5832655)
	statePops.append(5807719)
	statePops.append(5657342)
	statePops.append(5218040)
	statePops.append(4921532)
	statePops.append(4645318)
	statePops.append(4477251)
	statePops.append(4241507)
	statePops.append(3980783)
	statePops.append(3557006)
	statePops.append(3249879)
	statePops.append(3189068)
	statePops.append(3163561)
	statePops.append(3138259)
	statePops.append(3030522)
	statePops.append(2966786)
	statePops.append(2913805)
	statePops.append(2106319)
	statePops.append(1937552)
	statePops.append(1826913)
	statePops.append(1784787)
	statePops.append(1407006)
	statePops.append(1366275)
	statePops.append(1350141)
	statePops.append(1080577)
	statePops.append(1057125)
	statePops.append(986809)
	statePops.append(892717)
	statePops.append(765309)
	statePops.append(731158)
	statePops.append(712816)
	statePops.append(623347)
	statePops.append(582328)
	statePops.append(168485)
	statePops.append(106235)
	statePops.append(51433)
	statePops.append(49437)

#Assigns the starting number of representatives
def Assign_Reps():
	for i in range(len(stateNames)):
		representatives.append(1)

#Initializes the added to array
def Assign_Added_To():
	for i in range(len(stateNames)):
		hasBeenAddedTo.append(False)

#Initializes the percent representation array
def Assign_Perce_Rep():
	for i in range(len(stateNames)):
		perceRep.append(0.00)

#Initializes the percent error array
def Assign_Perce_Err():
	for i in range(len(stateNames)):
		perceErr.append(0.00)

#Assigns the total population
def Calc_Total_Pop():
	global totalPop
	for i in statePops:
		totalPop += i

#Initializes the percent population array
def Calc_Perce_Pop():
	for i in range(len(stateNames)):
		percePops.append(100*(statePops[i]/totalPop))

#Calculates the total number of representatives
def Calc_Total_Reps():
	global totalReps
	totalReps = 0
	for i in representatives:
		totalReps += i

#Calculates the percent representation each state has
def Calc_Perce_Rep():
	for i in range(len(stateNames)):
		#print(i)
		perceRep[i] = 100*(representatives[i]/totalReps)

#Calculates the percent Error between the state's representation and their share of the population
def Calc_Perce_Err():
	for i in range(len(stateNames)): 
		perceErr[i] = 100*((percePops[i] - perceRep[i])/percePops[i])

#Finds the greatest percent error
def Find_Greatest_Err():
	#print(str(perceErr.index(max(perceErr))))
	return perceErr.index(max(perceErr))

#Iterates the number of representatives of the state with the greatest error by one
def Iterate_Greatest_Err():
	representatives[Find_Greatest_Err()] += 1
	hasBeenAddedTo[Find_Greatest_Err()] = True

def initialize():
	Assign_Names()
	Assign_Pops()
	Assign_Reps()
	Assign_Added_To()
	Assign_Perce_Rep()
	Assign_Perce_Err()
	Calc_Total_Pop()
	Calc_Total_Reps()
	Calc_Perce_Pop()
	Calc_Perce_Rep()
	Calc_Perce_Err()

def Distributor():
	allAddedTo = False
	
	while allAddedTo == False:
		Iterate_Greatest_Err()
		Calc_Total_Reps()
		Calc_Perce_Rep()
		Calc_Perce_Err()
		
		for i in hasBeenAddedTo:
			if i == False:
				allAddedTo = False
			else:
				allAddedTo = True

initialize()
Distributor()

for i in range(len(stateNames)):
	print(str(i+1) + ")\tState Name: " + stateNames[i] + "\tState Population: " + str(statePops[i]) + "\tPercent of National Population: %" + str(round(percePops[i], 3)) + "\tNumber of Representatives: " + str(representatives[i]) + "\tPercent Representation: %" + str(round(perceRep[i], 3)) + "\tPercent Error vs Share of Population: %" + str(round(perceErr[i], 3)))
	
print("Total Number of Representatives:\t" + str(totalReps))