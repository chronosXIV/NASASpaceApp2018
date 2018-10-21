import time
import random

def main():
    
    answer = input("Do you want to see:\n1. Spaceship Fuel Check\n2. Location\n3. Fuel of station.\n4. Load fuel\n")
    if answer == "1":
        print_spaceship_fuel()
    elif answer == "2":
        print("https://www.nasa.gov/sites/default/files/images/515061main_newapollo14_close.png")
    elif answer == "3":
        print_fuelbar()
    elif answer == "4":
        print_fuelbar_increasing()

def print_spaceship_fuel():

    spaceship_fuel = random.randint(0,100)
    print("Your fuel is:",spaceship_fuel)

def print_fuelbar():

    fuel = random.randint(0,100)
    print("Total fuel left at the station is:",fuel)
    
def print_fuelbar_increasing():

    fuel = random.randint(0,100)
    print("Current fuel:",fuel)
    
    while fuel < 100:
        time.sleep(3)
        print('\n',
          '─\n')
        time.sleep(3)
        print('\n',
          '─-\n')
        time.sleep(3)
        print('\n',
          '─--\n')
        time.sleep(3)
        print('\n',
          '─---\n')
        time.sleep(3)
        print('\n',
          '─----\n')
        time.sleep(3)
        print('\n',
          '─-----\n')
        time.sleep(3)
        print('\n',
          '─-------\n')
        fuel = 100
        
    time.sleep(3)
    print("Finished filling up!")
        
main()
              
