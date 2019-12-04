import sys, time, os

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

piece("Welcome to a New Choice.\n\n", 0.5, 0.15)

piece("""A short story...        
Happy fun, simple morals and a little story.\n\n""", 0.5)

while True:
  piece("What is your name?\n")
  name = input().strip().lower()
  time.sleep(0.5)
  print("")
  if len(name) >= 9:
    rng = "Well, "
  elif len(name) <=7:
    rng = "Ah, "
  else:
    rng = "Truly Tragic, "
  piece(rng + name + "\n", 0.5, 0.15)

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
  print("")


  #choices
  piece("It's comming, decide now. Are you hiding or running.\n")
  choice = input().strip().lower()
  time.sleep(0.5)
  print("")

  if len(choice) != 0:
    if choice[0][0] == "r":
      #run
      piece("""As you flee through the trees, you make quick moves, jumping, ducking and sliding, oblivious to your mistakes.\n\n""")
      time.sleep(1)
      piece("""Thoese mistakes have lead you here, a dead end. 400 feet of shear rock stright down, the only thing ahead.
  No trees, no bushes, nothing to hide behind,
  except what's ahead.\n\n""")

      piece("It's going to be the fight of a life or the riskiest rock climbing ever seen.\n")

      piece("So what is it? A fight or hiding?\n")
      choice = input().strip().lower()
      time.sleep(0.5)
      print("")

      if len(choice) != 0:
        if choice[0][0] == "f":
          #fight
          piece("After unsheathing your weapon, you turn and face toward the woods.\n\nWaiting.\n\n")
          time.sleep(0.5)
          piece("But just then the cliff collapses and {} falls, into the void that awaits.\n".format(name))

        elif choice[0][0] == "h":
          #hide
          piece("The only place to hide, is hanging off the cliff.\nAs you climb down the side.\n3 feet down.\n5 feet down.\n9 feet down.\n\nNo sounds to hear.\n\n")
          piece("Waiting.\n\nUntill your grip flaters,\n{} falls into the void bellow.\n".format(name))

        else:
          piece("It's over, {}, indecision has been {}'s downfall.\n".format(name, name))
      else:
        piece("It's over, {}, indecision has been {}'s downfall.\n".format(name, name))


    elif choice[0][0] == "h":
      #hide
      piece("As you search in panic, you realise there are only two options.\nUp a tree or down a cave.\n\n")
      time.sleep(0.5)
      piece("")

      piece("So what is it? A tree or cave?\n")
      choice = input().strip().lower()
      time.sleep(0.5)
      print("")

      if len(choice) != 0:
        if choice[0][0] == "t":
          #tree
          piece("While scambling up the tree you realize your mistake:\n")
          time.sleep(0.5)
          piece("What has been following you,\n\ncan fly.\n\n")
          time.sleep(0.5)
          piece("Panic strikes and you fall out of the tree.\nAfter landing, {} barely retains conscious.\nThe only thing left for {} to do is...\n\nWait.\n".format(name, name))

        elif choice[0][0] == "c":
          #cave
          piece("Decending into the cave you pull out your torch.\nOnly to learn of it's nonfunctinal state.\n")
          time.sleep(1)
          piece("Turning around, you lose your footing and fall.\nDown,\nDown,\nDown.\n\n")
          piece("Sore, but alive you open your eyes.\n\nIt was just the same as when they were closed.\n\nThere is nothing left for {} to do, except... \n\nWait".format(name))

        else:
          piece("It's over, {}, indecision has been {}'s downfall.\n".format(name, name))
      else:
        piece("It's over, {}, indecision has been {}'s downfall.\n".format(name, name))
    else:
      piece("It's over, {}, indecision has been {}'s downfall.\n".format(name, name))
  else:
    piece("It's over, {}, indecision has been {}'s downfall.\n".format(name, name))

  os.system("clear") 

  piece("Only {} and the darkness.\n", 0.5, 0.2)
  piece("Was there ever a choice, or was all destined to end here?\n\n", 0.5, 0.2)


  while True:
    piece("Was there?\n", 0.5, 0.4)
    choice = input().strip().lower()
    time.sleep(0.5)
    print("")

    if len(choice) != 0:
      if choice[0][0] == "y":
        piece("Well, there is at some hope left.\n\n")
        time.sleep(1)
        piece("That leaves only one option.")
        os.system("clear") 

      elif choice[0][0] == "n":
        piece("The end is all that was wanted.\n\n", 0.5, 0.2)
        break

      else:
        piece("Thats not what I asked for.\n")
    else:
      piece("Thats not what I asked for.\n")

os.system("clear")
piece("There will be no more.",  0.5, 0.1)
time.sleep(3)
os.system("clear")