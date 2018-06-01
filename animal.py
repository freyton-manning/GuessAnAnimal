# This is a terminal-based "guess an animal game." the human user thinks of an animal, and the computer has 20 tries to guess and narrow down the animal
# questions to ask next are based on the user's responses
# added the ability to have the computer ask the questions out loud (it talks to you!)
# added a bunch of 'try' statements so it doesn't crash on non-macs when it tries to talk
try:
	from os import system
except:
	pass
import random
qprefixes = [
	'Is it',
	'Are you thinking of',
	'Would it happen to be',
	'Is the animal',

]



animalquestions = {
	#first
	():'a mammal',
	#mammals
	(True,):'a carnivore',

	#Carnivores
	(True,True):'a Northern Hemisphere animal',
	#Northern

	#Bear?
	(True,True,True):'a type of bear',
	#Guess bear types
	(True,True,True,True):'bear_list',


	#NotBear
	(True,True,True,False):'a type of canine',
	#Guess Canine types
	(True,True,True,False,True):'canine_list',
	(True,True,True,False,False):'a type of feline',
	(True,True,True,False,False,True):'nh_feline_list',
	(True,True,True,False,False,False):'an aquatic mammal',
	(True,True,True,False,False,False,True):'aquatic_mammal_list',
	(True,True,True,False,False,False,False):'small_carnivores_list',




	#Southern
	(True,True,False):'a type of feline',
	#Guess cats
	(True,True,False,True):'sh_feline_list',

	(True,True,False,False):'sh_non_feline_carnivores',









	#Non-Mammals
	(False):'a reptile',
	(False,True):'reptile_list',

	(False,False):'a bird',
	(False,False,True):'bird_list',


	(False,False,False):'a fish',
	(False,False,False,True):'fish_list',
	(False,False,False,False):'an amphibian',
	(False,False,False,False,True):'amphibian_list',



	#NonCarnivore Mammals
	(True,False):'a domesticated animal?',
	(True,False,True):'domestic_list',

	(True,False,False):'an animal larger than a basset hound?',
	(True,False,False,True):'wild_large_noncarnivores',

	(True,False,False,False):'a rodent',
	(True,False,False,False,True):'rodent_list',
	(True,False,False,False,False):'wild_small_noncarnivores',
}

cheatlist ={
	'bear_list':[
		'a polar bear',
		'a grizzly bear'],
	'canine_list':['a fox',
				   'a dog',
				   'a wolf',
				   'a coyote'],
	'sh_feline_list':['a lion',
					  'a tiger',
					  'a cheetah',
					  'a leopard',
					  'a jaguar',
					  'an ocelot'],
	'sh_non_feline_carnivores':['an aardvark',
								'a hyena',],
	'nh_feline_list':['a cougar/mountain lion',
					  'a leopard',
					  'a panther',
					  'a bob cat/linx',
					  'a jaguar',
					  'a house cat'],
	'reptile_list':['a turtle',
					'a crocodile',
					'an aligator',
					'a snake',
					'a chameleon',
					'a gecko',
					'an iguana',
					'a komodo dragon'],
	'bird_list':['an eagle',
				 'a falcon',
				 'a blue jay',
				 'a cardinal',
				 'a chicken',
				 'a turkey',
				 'a pheasant',
				 'a peacock',
				 'a crow',
				 'an ostrich',
				 'an emu',
				 'a penguin',
				 'an owl',
				 'a woodpecker',],
	'domestic_list':['a pig',
					 'a cow',
					 'a horse',
					 'a sheep',
					 'a llama',
					 'a guinea pig',
					 'a hamster',],
	'aquatic_mammal_list':['a dolphin',
						   'a whale',
						   'a seal',
						   'a walrus',
						   'a manatee',
						   'a sea lion',
						   'an otter',],
	'rodent_list':['a mouse',
				   'a mole',
				   'a rat',
				   'a gopher',
				   'a groundhog/woodchuck',
				   'a beaver',
				   'a squirell',
				   'a chipmunk',
				   'a mole',
				   'a hamster',
				   'a prarie dog',],
	'wild_large_noncarnivores':['a wolverine',
								'an elk',
								'a deer',
								'a goat',
								'a wild boar',
								'a sasquatch',
								'a gorrilla',
								'an elephant',
								'a hippo',
								'a rhino',
								'a sloth',
								'a gazelle',
								'a moose',
								'a zebra',
								'a badger',],
	'wild_small_noncarnivores':['a raccoon',
								'an opossum',
								'a bat',
								'a monkey',
								'a lemur',
								'a meerkat',
								'a rabbit',],
	'small_carnivores_list':[
		'a weasel',
		'a mink',
		'a mongoose',]
}

#This is the Game Wrapper Function
def twentyq():
	#List to hold our answers
	answers = []
	#Initial value of True so our While Loop won't end before it starts
	askagain = True
	#Loop while the Question to ask function tells us that we are still looping
	while askagain == True:
		#This gets the questions to ask, but only asks the question if we are in the final guesses (animal guesses)
		qtoask(answers)

		instring = raw_input()
		#This lets us exit the game
		if instring == 'exit':
			return
		#Append answers to the list so we know what was tried.
		answers.append(yntotf(instring))
	return

# Does a really fast NLP conversion of Yes / No's as a person might say them to a True / False
def yntotf(instring):
	#This is not a comprehensive list of affirmatives
	if len({'yes','yeah','sure','yep','yup','y'}.intersection(instring.lower().split(' '))) > 0:
		return True
	#If they didn't say yes they said no
	else:
		return False

# This converts list to a tuple so it can be fetched from a dictionary
def qtoask(answers):
	#Tupleize the List
	tupanswers = tuple(answers)
	#This was a debug print so I could see which answers I had given,
	#print tupanswers

	#if the tuple is in the dictionary decide what to do. If not Give up.
	if tupanswers in animalquestions:
		#if there is not an Underscore we ask a question.
		if '_' not in animalquestions[tupanswers]:
			say = random.choice(qprefixes) + " "+  animalquestions[tupanswers] + '?'
		# If there is an underscore we guess animals from a "cheat list"
		else:

			success = cheatgroup(animalquestions[tupanswers])
			#if the animal was in our cheat list we won
			if success == True:
				print 'I win'
				try:
					system('say I win')
				except:
					pass
				return False
			#if the animal was not in our cheat list we lost
			else:
				print 'I give up'
				try:
					system('say I give up')
				except:
					pass

				return False
		#If the tuple was not in our dictionary we don't know what the animal is, and we lost.
	else:
		print 'I give up!'
		try:
			system('say I give up')
		except:
			pass
		return False

	print say
	ssay = 'say ' + say
	try:
		system(ssay)
	except:
		pass

	return True

def cheatgroup(animallist):
	userin = True
	for animal in cheatlist[animallist]:

		say = random.choice(qprefixes) + " "+  animal + '?'
		print say
		ssay = 'say ' + say
		try:
			system(ssay)
		except:
			pass
		instring = raw_input()
		userin = yntotf(instring)
		if userin == True:
			return True
	return False