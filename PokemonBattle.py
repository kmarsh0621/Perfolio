import random

player_health = 100
enemy_health = 100
pokemonlist = ["bulbasaur", "charmander", "squirtle"]
#start of pokemon move set dictonary
bulbasaur_move_set = {
	"tackle" : 15,
	"vine whip" : 25,
	"razor leaf" : 35,
	"solar beam": 40
}

charmander_move_set = {
	"scratch" : 15, 
	"ember" : 25,
	"flamethrower" : 35,
	"fire spin" : 40
}

squirtle_move_set = {
	"tackle" : 15,
	"bubble" : 25,
	"water gun" : 35,
	"hydro pump" : 40
}

pokemon_movelist = [bulbasaur_move_set, charmander_move_set, squirtle_move_set]

def typing_effective() :
	typing = {
		"grass" : {"water" : 2.0, "fire" : 0.5, "grass" : 0.5, "normal" : 1},
		"fire" : {"grass" : 2.0, "water" : 0.5, "fire" : 0.5, "normal" : 1},
		"water" : {"fire" : 2.0, "grass" : 0.5, "water" : 0.5, "normal" : 1}
	}
	return typing
	
def asaign_types():
	pokemontypes = {
		"bulbasaur" : "grass",
		"charmander" : "fire",
		"squirtle" : "water"
	}
	return pokemontypes
type_effectivness = typing_effective()

move_types = {
	"tackle" : "normal",
	"vine whip" : "grass",
	"razor leaf" : "grass",
	"solar beam" : "grass",
	"scratch" : "normal",
	"ember" : "fire",
	"flamethrower" : "fire",
	"fire spin" : "fire",
	"bubble" : "water",
	"water gun" : "water",
	"hydro pump" : "water"
}

def peffective() :
	if type_effectivness[move_type][enemy_type] == 2 :
		print("Your attack was super effective!")
	elif type_effectivness[move_type][enemy_type] == 0.5 :
		print("Your attack wasn't very effective!")
						
def e_effective() :
	if type_effectivness[enemy_move_type][player_type] == 2 :
		print("Enemy's attack was super effective!")
	elif type_effectivness[enemy_move_type][player_type] == 0.5 :
		print("Enemy's attack wasn't very effective!")

def main() :
	global move_type, enemy_move_type
	global player_type, enemy_type
	#start of pokemon selection logic
	pokemontypes = asaign_types()
	global player_health, enemy_health
	pokemon = input(f"Please enter a pokemon {pokemonlist}: ")
	while pokemon not in pokemonlist :
		print(f"Please select a pokemon from the list: {pokemonlist}")
		pokemon = input()
	if pokemon == "bulbasaur" :
		player_move_set = bulbasaur_move_set 
		enemy_pokemon = random.choice(pokemonlist) 
		enemy_move_set = globals()[f"{enemy_pokemon}_move_set"]
	elif pokemon == "charmander" :
		player_move_set = charmander_move_set 
		enemy_pokemon = random.choice(pokemonlist) 
		enemy_move_set = globals()[f"{enemy_pokemon}_move_set"]
	elif pokemon == "squirtle" :
		player_move_set = squirtle_move_set
		enemy_pokemon = random.choice(pokemonlist)
		enemy_move_set = globals()[f"{enemy_pokemon}_move_set"]
	print(f"You have picked {pokemon}!")
	print(f"Enemy has picked {enemy_pokemon}!")
	#start of while loop game logic
	while player_health > 0 and enemy_health > 0 :
		player_type = pokemontypes[pokemon]
		enemy_type = pokemontypes[enemy_pokemon]
		starting_player = random.choice(["player", "enemy"])
		print(starting_player)
		#start of player battle logic
		if starting_player == "player" :
			if player_health <= 0 :
				print(f"Enemy's Health: {enemy_health}")
				print("You lost to the enemy!")
				break
			player_move = input(f"Please pick an attack: {player_move_set}")
			while player_move not in player_move_set :
				print("Please enter an attack from the list.")
				player_move = input(f"Please pick an attack: {player_move_set}")
			else :
				player_damage = player_move_set[player_move]
				move_type = move_types[player_move]
				if move_type in type_effectivness and enemy_type in type_effectivness[move_type] :
					peffective()
					player_damage *= type_effectivness[move_type][enemy_type]		
				enemy_health -= player_damage
				if enemy_health <= 0 :
					print(f"Player's Health {player_health}")
					print("You beat the enemy!")
					break	
				enemy_move = random.choice(list(enemy_move_set.keys()))
				enemy_damage = enemy_move_set[enemy_move]
				enemy_move_type = move_types[enemy_move]
				if enemy_move_type in type_effectivness and player_type in type_effectivness[enemy_move_type] :
					e_effective()
					enemy_damage *= type_effectivness[enemy_move_type][player_type]
				player_health -= enemy_damage
				print(f"Player's Health: {player_health}")
				print(f"Enemy's Health: {enemy_health}")
				if player_health <= 0 :
					print("You lost to the enemy!")
		#start of enemy battle logic
		else :
			enemy_move = random.choice(list(enemy_move_set.keys()))
			player_move = input(f"Please pick an attack: {player_move_set}")
			while player_move not in player_move_set :
				print("Please eneter an attack from the list.")
				player_move = input(f"Please pick an attack: {player_move_set}")
			enemy_damage = enemy_move_set[enemy_move]
			enemy_move_type = move_types[enemy_move]
			if enemy_move_type in type_effectivness and player_type in type_effectivness[enemy_move_type] :
				e_effective()
				enemy_damage *= type_effectivness[enemy_move_type][player_type]
			player_health -= enemy_damage
			if player_health <= 0 :
				print(f"Enemy's Health {enemy_health}")
				print("You lost to the enemy!")
				break
			else :
				player_damage = player_move_set[player_move]
				move_type = move_types[player_move]
				if move_type in type_effectivness and enemy_type in type_effectivness[move_type] :
					peffective()
					player_damage *= type_effectivness[move_type][enemy_type]
				enemy_health -= player_damage
				if enemy_health <= 0 :
					print(f"Player's Health: {player_health}")
					print("You beat the enemy!")
					break
				print(f"Player's Health: {player_health}")
				print(f"Enemy's Health: {enemy_health}")
main()