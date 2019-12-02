import sys, time

fails = 0
difficulty = 0

health = 100
attack = 10
blockAmount = 10
block = 0

def piece(text = """Lorem Ipsum,
Neque porro quisquam est qui dolorem ipsum quia dolor sit amet,
consectetur, adipisci velit...\n\n""", delay = 0.2, speed = 0.03):
  for c in text:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(speed)
  print
  time.sleep(delay)


#intro scene

piece("Welcome to something new.\n\n", 0.5, 0.15)

piece("""A short story...        
Happy fun, simple morals and a little story.\n\n""", 0.5)

piece("What is your name?\n")
name = input().strip().lower()
time.sleep(0.5)
print("")
piece(name + "\n", 0.5, 0.15)

while True:
  time.sleep(0.05)
  piece("\b\b")
while True:
  piece("How much do you regret? Low or enough?\n")
  difficultyC = input().strip().lower()
  time.sleep(0.5)
  print("")

  if len(difficultyC) != 0:
    if difficultyC[0][0] == "l":
      piece("Low? It's a simple start.\n\n")
      difficulty = 0
      break
    elif difficultyC[0][0] == "e":
      piece("Enough? That's going to hurt, however much that is.\n\n")
      difficulty = 1
      break
    else:
      piece("Thats not what I asked for.\n")
      fails += 1
  else:
    piece("Thats not what I asked for.\n")
    fails += 1



if difficulty ==0:
  piece("""It's a day in the forest.
There isn't much here but your small camp.
Then you rember, what has happened, it hits you like a truck.
The day is young but time is the most valualbe resource here.
There is no escaping what is comming.
Only a few days remain until the last bridge will be blocked.\n\n""")
  piece("""You'r still hurt from the prevous day, you could rest here for the day or travel on.
What are you doing?""")
  choice = input().strip().lower()
  

