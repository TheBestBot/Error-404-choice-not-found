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

#story
piece("""It's a forest, a rather pretty one.
But that's not why your here, theres a job that has to be done.\n\n""")

piece("""As your sneaking through it you hear a sound.
It's low pitched, barely audible, but there none the less.\n\n""")

piece("It happens again, louder...\n")
time.sleep(1)
piece("Louder and faster,\n")
time.sleep(0.5)
for i in range(5):
  i += 1
  piece("and again,\n", 0.2, 0)


#choices
piece("It's comming, decide now. Are you hiding or running.")
choice = input().strip().lower()
time.sleep(0.5)
print("")

if len(choice) != 0:
  if choice[0][0] == "r":
    piece("""As you flee through the trees, you make quick moves, jumping, ducking and sliding, oblivious to your mistakes.\n\n""")
    time.sleep(2)
    piece("""Thoese mistakes have lead you here, a dead end. 400 feet of shear rock stright down, the only thing ahead. No trees, no bushes, nothing to hide behind  , except what's ahead.""")

    piece("It's going to be the fight of a life or the riskiest rock climbing ever seen.")

    if len(choice) != 0:
      if choice[0][0] == "r":
        piece("""As you flee through the trees, you make quick moves, jumping, ducking and sliding, oblivious to your mistakes.\n\n""")
        time.sleep(2)
        piece("""Thoese mistakes have lead you here, a dead end. 400 feet of shear rock stright down, the only thing ahead. No trees, no bushes, nothing to hide behind  , except what's ahead.""")

        piece("It's going to be the fight of a life or the riskiest rock climbing ever seen.")

        piece("So what is it? A fight or hiding?")
        choice = input().strip().lower()
        time.sleep(0.5)
        print("")

      elif difficultyC[0][0] == "h":
        piece("Enough? That's going to hurt, however much that is.\n\n")

      else:
        piece("It's over, {}, your indecision has been your downfall.\n".format(name))
    else:
      piece("It's over, {}, your indecision has been your downfall.\n".format(name))






    elif difficultyC[0][0] == "h":
      piece("Enough? That's going to hurt, however much that is.\n\n")


  print("the other way")
else:
  piece("It's over, {}, your indecision has been your downfall.\n".format(name))

piece("So what is it? A fight or hiding?")
      choice = input().strip().lower()
      time.sleep(0.5)
      print("")