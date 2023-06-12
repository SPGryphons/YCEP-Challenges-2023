banner = '''
  _____       _   _                                 _   _                _   _           _             
 |  __ \     | | | |                     /\        | | | |              | | (_)         | |            
 | |__) |   _| |_| |__   ___  _ __      /  \  _   _| |_| |__   ___ _ __ | |_ _  ___ __ _| |_ ___  _ __ 
 |  ___/ | | | __| '_ \ / _ \| '_ \    / /\ \| | | | __| '_ \ / _ \ '_ \| __| |/ __/ _` | __/ _ \| '__|
 | |   | |_| | |_| | | | (_) | | | |  / ____ \ |_| | |_| | | |  __/ | | | |_| | (_| (_| | || (_) | |   
 |_|    \__, |\__|_| |_|\___/|_| |_| /_/    \_\__,_|\__|_| |_|\___|_| |_|\__|_|\___\__,_|\__\___/|_|   
         __/ |                                                                                         
        |___/                                                                                          
'''
print(banner)


with open("flag/flag.txt", "r") as f:
    password = f.read()

def errHandler():
    print('Error: Incorrect password.')
    exit()

try:
    userInput = input("> ")
    if userInput == password:
        with open('flag/flag.txt') as f:
            print(f.read())
    else:
        errHandler()

except:
    errHandler()
