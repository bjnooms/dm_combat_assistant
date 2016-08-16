#!/usr/bin/python 

import collections

class PlayerCharacter(object):

#    def __init__(self):
#        self.name = raw_input("Name: ")
    def __init__(self, name):
        self.name = name
        self.ac = raw_input("AC: ")
        self.hp = raw_input("HP: ")
        self.initiative = raw_input("Initiative Roll: ")

class NonPlayerCharacter(object):

    def __init__(self, name):
        self.name = name
        self.ac = raw_input("AC: ")
        self.hp = raw_input("HP: ")
        self.initiative = raw_input("Initiative Roll: ")

# Begin Character and NPC setup
# create list of player character's names depending on number user enters

num_pc = raw_input("How many Player Characters are there? (ex. 1, 2, 3...): ")
pc_list = []
count = int(num_pc)
while count > 0:
    pc_list.append(raw_input("PC Name: "))
    count -= 1

# create PlayerCharacter object for each name in the list generated above

for n in range(0,int(num_pc)):
    print "Creating PlayerCharacter object for: %s" % pc_list[n]
    pc_list[n] = PlayerCharacter(pc_list[n])

# create dictionary to store ongoing health totals for each player character

pc_hp_tracker = {}
for n in range(0,int(num_pc)):
    player = pc_list[n].name
    pc_hp_tracker[player] = pc_list[n].hp


# create list of npc names depending on number user enters

num_npc = raw_input("How many Non-Player Characters are there? (ex. 1, 2, 3...): ")
npc_list = []
count = int(num_npc)
while count > 0:
    npc_list.append(raw_input("NPC Name: "))
    count -= 1

# create NPC object for each name in the list generated above

for n in range(0,int(num_npc)):
    print "Creating NPC object for: %s" % npc_list[n]
    npc_list[n] = NonPlayerCharacter(npc_list[n])

# create dictionary to store ongoing health totals for each npc

npc_hp_tracker = {}
for n in range(0,int(num_npc)):
    npc = npc_list[n].name
    npc_hp_tracker[npc] = npc_list[n].hp



### need to find a way to determine the initiative order
# first need to get all pc's and npc's into a dictionary with their init rolls associated with name

initiative_order = {}
for i in range(0,int(num_pc)):
    pc_init = int(pc_list[i].initiative)
    initiative_order[pc_init] = pc_list[i].name

for i in range(0,int(num_npc)):
    npc_init = int(npc_list[i].initiative)
    initiative_order[npc_init] = npc_list[i].name

print initiative_order
ordered_initiative = collections.OrderedDict(sorted(initiative_order.items(), key=lambda t: t[0]))
for k, v in ordered_initiative.iteritems():
    print k, v




#print len(initiative_order)

#for i in range(0, len(initiative_order)):



#init_order(**initiative_order)

#for each in pc_list:
#    print initiative_order[each]
#for each in npc_list:
#    print initiative_order[each]


