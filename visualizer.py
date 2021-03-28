import pygame 
import algorithims
import sys 
import os 

dim = (1024, 512)

algorithims = {"MergeSort": algorithims.MergeSort()}

win = pygame.display.set_mode(dim)

win.fill(pygame.color("#a48be0"))

def check_quit():
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

def update(algorithim, swap1=None, swap2=None, win=win):
  win.fill(pygame.color("#a48be0"))
  pygame.display.set_caption("Merge Sort Algorithim")
  k = int(dim([0]/len(algorithim.array)))
  for i in range(len(algorithim.array)):
    # Green when sorting
    colour = (0, 0, 255)
    if swap1 == algorithim.array[i]:
      colour = (0 ,255, 0)
    elif swap2 == algorithim.array[i]:
      colour = (255, 0, 0)
    
    pygame.draw.rect(win, colour, (i*k), dim[i], k, -algorithim.array[i])
  
  check_quit()
  pygame.display.update()

def main(args):

  try:
    algorithim = algorithims[args[0]]
    _, timeElapsed = algorithim.run()
  except:
    print("An error has occured")

if __name__ == "__main__":
  sys.argv.append("MergeSort")
  main(sys.argv)