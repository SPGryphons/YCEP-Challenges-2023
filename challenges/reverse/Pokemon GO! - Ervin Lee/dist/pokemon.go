// Mini Pokemon game in GO
// To run this file, type "go run pokemon.go" in the terminal

package main
import (
	"fmt"
	"math/rand"
	"time"
	"strconv"
	"os"
	"bufio"
	"encoding/base64"
)

func printTitle() {
	var ascii_art string 
	ascii_art = `
	██████╗░░█████╗░██╗░░██╗███████╗███╗░░░███╗░█████╗░███╗░░██╗	░██████╗░░█████╗░██╗
	██╔══██╗██╔══██╗██║░██╔╝██╔════╝████╗░████║██╔══██╗████╗░██║	██╔════╝░██╔══██╗██║
	██████╔╝██║░░██║█████═╝░█████╗░░██╔████╔██║██║░░██║██╔██╗██║	██║░░██╗░██║░░██║██║
	██╔═══╝░██║░░██║██╔═██╗░██╔══╝░░██║╚██╔╝██║██║░░██║██║╚████║	██║░░╚██╗██║░░██║╚═╝
	██║░░░░░╚█████╔╝██║░╚██╗███████╗██║░╚═╝░██║╚█████╔╝██║░╚███║	╚██████╔╝╚█████╔╝██╗
	╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝	░╚═════╝░░╚════╝░╚═╝
	`
	fmt.Println(ascii_art)
}

func printMenu() {
	fmt.Println(`
	[1] Start Game
	[2] Exit
	`)
}

func playGame() {

	var printPokemon = func() {
		fmt.Println(`
		[1] Bulbasaur
		[2] Charmander
		[3] Squirtle
		`)
	}

	var printOptions = func() {
		fmt.Println(`
		[1] Attack
		[2] Run
		`)
	}

	var printMoves = func(array [4]string) {
		fmt.Println(`
		[1] ` + array[0] + `
		[2] ` + array[1] + `
		[3] ` + array[2] + `
		[4] ` + array[3] + `
		`)
	}

	var printHPBar = func(hp int, max_hp int) {
		var hp_bar string
		for i := 0; i < hp / 10; i++ {
			hp_bar += "█"
		}
		for i := 0; i < (max_hp - hp) / 10; i++ {
			hp_bar += "░"
		}
		fmt.Println(hp_bar + "\n")
	}

	var name string
	fmt.Println("Enter your name: ")
	fmt.Scanln(&name)
	fmt.Println("Hello, " + name + "! Welcome to Pokemon GO! Are you ready for some exciting Pokemon adventures?")
	
	type Pokemon struct {
		name string
		hp int
		speed int
		moves [4]string
		move1_damage int
		move2_damage int
		move3_damage int
		move4_damage int
	}

	var chosen_pokemon Pokemon
	var enemy_pokemon Pokemon

	var pokemon_list = [3]string{"Bulbasaur", "Charmander", "Squirtle"}
	var pokemon_enemy_list = [3]string{"Pikachu", "Charazard", "Snorlax"}
	var pokemon_stats = [3]Pokemon{
		{"Bulbasaur", 125, 10, [4]string{"Tackle", "Vine Whip", "Razor Leaf", "Solar Beam"}, 15, 22, 31, 41},	
		{"Charmander", 120, 11, [4]string{"Scratch", "Ember", "Flamethrower", "Fire Blast"}, 20, 24, 34, 42},
		{"Squirtle", 150, 10, [4]string{"Tackle", "Bubble", "Water Gun", "Hydro Pump"}, 15, 20, 30, 40},
	}

	var pokemon_enemy_stats = [3]Pokemon{
		{"Pikachu", 100, 9, [4]string{"Tackle", "Thunder Shock", "Thunderbolt", "Thunder"}, 10, 24, 33, 41},
		{"Charazard", 200, 20, [4]string{"Scratch", "Ember", "Flamethrower", "Fire Blast"}, 15, 25, 35, 44},
		{"Snorlax", 300, 30, [4]string{"Tackle", "Headbutt", "Body Slam", "Hyper Beam"}, 10, 22, 36, 42},
	}

	var choose_pokemon int
	fmt.Println("Choose your Pokemon: ")
	printPokemon()
	fmt.Scanln(&choose_pokemon)
	for choose_pokemon != 1 && choose_pokemon != 2 && choose_pokemon != 3 {
		fmt.Println("Invalid choice.")
		printPokemon()
		fmt.Println("Choose your Pokemon: ")
		fmt.Scanln(&choose_pokemon)
	}

	fmt.Println("You chose " + pokemon_list[choose_pokemon-1] + "! Let's go!")

	chosen_pokemon.name = pokemon_list[choose_pokemon-1]
	chosen_pokemon.hp = pokemon_stats[choose_pokemon-1].hp
	chosen_pokemon.speed = pokemon_stats[choose_pokemon-1].speed
	chosen_pokemon.moves = pokemon_stats[choose_pokemon-1].moves
	chosen_pokemon.move1_damage = pokemon_stats[choose_pokemon-1].move1_damage
	chosen_pokemon.move2_damage = pokemon_stats[choose_pokemon-1].move2_damage
	chosen_pokemon.move3_damage = pokemon_stats[choose_pokemon-1].move3_damage
	chosen_pokemon.move4_damage = pokemon_stats[choose_pokemon-1].move4_damage
	
	var chosen_enemy_pokemon int = rand.Intn(3)
	enemy_pokemon.name = pokemon_enemy_list[chosen_enemy_pokemon]
	enemy_pokemon.hp = pokemon_enemy_stats[chosen_enemy_pokemon].hp
	enemy_pokemon.speed = pokemon_enemy_stats[chosen_enemy_pokemon].speed
	enemy_pokemon.moves = pokemon_enemy_stats[chosen_enemy_pokemon].moves
	enemy_pokemon.move1_damage = pokemon_enemy_stats[chosen_enemy_pokemon].move1_damage
	enemy_pokemon.move2_damage = pokemon_enemy_stats[chosen_enemy_pokemon].move2_damage
	enemy_pokemon.move3_damage = pokemon_enemy_stats[chosen_enemy_pokemon].move3_damage
	enemy_pokemon.move4_damage = pokemon_enemy_stats[chosen_enemy_pokemon].move4_damage

	time.Sleep(1 * time.Second)

	fmt.Println("Your Pokemon: " + chosen_pokemon.name)
	fmt.Println("Enemy Pokemon: " + enemy_pokemon.name)
	
	for chosen_pokemon.hp > 0 || enemy_pokemon.hp > 0 {
		fmt.Println("Your Pokemon's HP: " + strconv.Itoa(chosen_pokemon.hp) + "/" + strconv.Itoa(pokemon_stats[choose_pokemon-1].hp))
		printHPBar(chosen_pokemon.hp, pokemon_stats[choose_pokemon-1].hp)
		fmt.Println("Enemy Pokemon's HP: " + strconv.Itoa(enemy_pokemon.hp) + "/" + strconv.Itoa(pokemon_enemy_stats[chosen_enemy_pokemon].hp))
		printHPBar(enemy_pokemon.hp, pokemon_enemy_stats[chosen_enemy_pokemon].hp)
		printOptions()
		var option int
		fmt.Println("Enter choice: ")
		fmt.Scanln(&option)
		for option != 1 && option != 2 {
			fmt.Println("Invalid choice.")
			printOptions()
			fmt.Println("Enter choice: ")
			fmt.Scanln(&option)
		}

		if option == 1 {
			printMoves(chosen_pokemon.moves)
			var move int
			fmt.Println("Enter move: ")
			fmt.Scanln(&move)
			for move < 1 || move > 4 {
				fmt.Println("Invalid choice.")
				printMoves(chosen_pokemon.moves)
				fmt.Println("Enter move: ")
				fmt.Scanln(&move)
				time.Sleep(1 * time.Second)
			}

			var chosen_pokemon_attack = func(move int) {
				fmt.Println(chosen_pokemon.name + " used " + chosen_pokemon.moves[move-1] + "!")
				if move == 1 {
					enemy_pokemon.hp -= chosen_pokemon.move1_damage
				} else if move == 2 {
					enemy_pokemon.hp -= chosen_pokemon.move2_damage
				} else if move == 3 {
					enemy_pokemon.hp -= chosen_pokemon.move3_damage
				} else {
					enemy_pokemon.hp -= chosen_pokemon.move4_damage
				}
			}

			var enemy_pokemon_attack = func(move int) {
				fmt.Println(enemy_pokemon.name + " used " + enemy_pokemon.moves[rand.Intn(4)] + "!")
				if move == 1 {
					chosen_pokemon.hp -= enemy_pokemon.move1_damage
				} else if move == 2 {
					chosen_pokemon.hp -= enemy_pokemon.move2_damage
				} else if move == 3 {
					chosen_pokemon.hp -= enemy_pokemon.move3_damage
				} else {
					chosen_pokemon.hp -= enemy_pokemon.move4_damage
				}
			}

			if chosen_pokemon.speed > enemy_pokemon.speed {
				enemy_pokemon_attack(rand.Intn(4))
				time.Sleep(3 * time.Second)
				chosen_pokemon_attack(move)
				time.Sleep(3 * time.Second)
			} else {
				chosen_pokemon_attack(move)
				time.Sleep(3 * time.Second)
				enemy_pokemon_attack(rand.Intn(4))
				time.Sleep(3 * time.Second)
			}

			if chosen_pokemon.hp <= 0 {
				fmt.Println("You lost!")
				break
			} else if enemy_pokemon.hp <= 0 {
				fmt.Println("You won!")
				fmt.Println("Enter anything to end the program...")
				var input string
				fmt.Scanln(&input)
				var word string = "YmFja2Rvb3I="
				var ZGVjb2RlZF93b3Jk, _ = base64.StdEncoding.DecodeString(word)
				if input == "pokemon" {
					fmt.Println("You found a secret! Here's a hint: " + string(ZGVjb2RlZF93b3Jk))
				} else if input == string(ZGVjb2RlZF93b3Jk) {
					fmt.Println("you found a backdoor! but there's nothing here... find another backdoor maybe? this might help you: " + string(ZGVjb2RlZF93b3Jk) + "2")
				} else if input == string(ZGVjb2RlZF93b3Jk) + "2" {
					fmt.Println("you found another backdoor! someone named cetacean dumped some data somewhere in the temporary directory. what if we played this game again with this text file?")
					cHJpbnRYT1JGbGFn()
				}
			}	
		} else {
			fmt.Println("You ran away!")
			break
		}
	}
}

// note to self to not delete this function
// someone named cetacean dumped some data some
func cHJpbnRYT1JGbGFn() {
	ZmlsZVBhdGgg := os.Args[1]
	cmVhZEZpbGUg, err := os.Open(ZmlsZVBhdGgg)
	if err != nil {
		fmt.Println("Now, do you see your error?!")
		fmt.Println(err)
	}

	var ZmlsZXNjYW5uZXIg = bufio.NewScanner(cmVhZEZpbGUg)
	ZmlsZXNjYW5uZXIg.Split(bufio.ScanLines)
	var ZmlsZUxpbmVz []string

	for ZmlsZXNjYW5uZXIg.Scan() {
		ZmlsZUxpbmVz = append(ZmlsZUxpbmVz, ZmlsZXNjYW5uZXIg.Text())
	}

	cmVhZEZpbGUg.Close()

	fmt.Println(ZmlsZUxpbmVz)
}

func main() {
	printTitle()
	fmt.Println("Welcome to Pokemon GO!")
	printMenu()
	var choice int
	fmt.Println("Enter choice: ")
	fmt.Scanln(&choice)
	for choice != 2 {
		if choice == 1 {
			fmt.Println("Starting game...")
			playGame()
			break
		} else {
			fmt.Println("Invalid choice.")
			printMenu()
			fmt.Println("Enter choice: ")
			fmt.Scanln(&choice)
		}
	}
}