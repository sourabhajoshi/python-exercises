"""
Write a loop that makes seven calls to print(), so we get on the output the following triangle:

  #
  ##
  ###
  ####
  #####
  ######
  #######
"""

for i in range(0, 8):
    for j in range(0, i):
        print("#", end="")
    print()