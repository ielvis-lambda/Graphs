from room import Room
from player import Player
from world import World

import random

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.

# roomGraph={0: [(3, 5), {'n': 1}], 1: [(3, 6), {'s': 0, 'n': 2}], 2: [(3, 7), {'s': 1}]}

roomGraph={0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}], 1: [(3, 6), {'s': 0, 'n': 2}], 2: [(3, 7), {'s': 1}], 3: [(4, 5), {'w': 0, 'e': 4}], 4: [(5, 5), {'w': 3}], 5: [(3, 4), {'n': 0, 's': 6}], 6: [(3, 3), {'n': 5}], 7: [(2, 5), {'w': 8, 'e': 0}], 8: [(1, 5), {'e': 7}]}

world.loadGraph(roomGraph)
player = Player("Name", world.startingRoom)


traversalPath = []

# init dictionary of visited rooms
visited_rooms = {}
visited_rooms[player.currentRoom.id] = {x: '?' for x in player.currentRoom.getExits()}

print(f'visited_rooms are {visited_rooms}')
# print('visited_rooms:', visited_rooms)
# print(player.currentRoom.id)

# init set of unexplored exits for base condition
unexplored_exits = set()
for exit in player.currentRoom.getExits():
    unexplored_exits.add(f'{player.currentRoom.id}{exit}')
print('unexplored_exits:', unexplored_exits)

#assign current room
current_room = player.currentRoom.id
move = None


def oppositeDir(dir):
  if dir == 's':
    return 'n'
  elif dir == 'n':
    return 's'  
  elif dir == 'e':
    return 'w'
  elif dir == 'w':
    return 'e'  


# backtracking
# inverseDirections = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
# visited_rooms[current_room] = inverseDirections
# print('backtrack:', visited_rooms)   

# depth first search to find a dead end
while unexplored_exits:
    # print('visited room values:', visited_rooms[player.currentRoom.id].values())
    if '?' in visited_rooms[player.currentRoom.id].values():
        print('in room:', player.currentRoom.id)
        #find a room that hasn't been visited
        # print('find room n value:',visited_rooms[player.currentRoom.id]['n'])
        for exit in player.currentRoom.getExits():
            unexplored_exits.add(f'{player.currentRoom.id}{exit}')
            print(f"PRINTING unexplored_exits {unexplored_exits}")

        try:
          if visited_rooms[player.currentRoom.id]['n'] == '?':
              move = 'n'
          elif visited_rooms[player.currentRoom.id]['s'] == '?':
              move = 's'
          elif visited_rooms[player.currentRoom.id]['e'] == '?':
              move = 'e'
          elif visited_rooms[player.currentRoom.id]['w'] == '?':
              move = 'w'
        except:
          print("All directions explored in this room")
          move = oppositeDir(move)

    # remove unvisited room, move to the next room, add move to traversalPath
    print('unexplored 2:', unexplored_exits )

    prevRoom = player.currentRoom.id

    player.travel(move) 

    if player.currentRoom.id == prevRoom:
      move = oppositeDir(move)
      player.travel(move)

    try:
      unexplored_exits.remove(f'{prevRoom}{move}')
    except:
      print('already passed thru here')

    # add new room to visited room
    if player.currentRoom.id not in visited_rooms:
        visited_rooms[prevRoom] = {move: player.currentRoom.id}

        visited_rooms[player.currentRoom.id] = {x: '?' for x in player.currentRoom.getExits()}

        visited_rooms[player.currentRoom.id] = {oppositeDir(move): prevRoom}

        for exit in visited_rooms[player.currentRoom.id]:
          print(f"IM AN EXIT {exit}")
          unexplored_exits.add(f'{player.currentRoom.id}{exit}')

    print(f'visited_rooms are {visited_rooms}')
    print(f'unexplored_exits are {unexplored_exits}')
    print(f"the prevRoom is: {prevRoom}")

    try:
        for exit in visited_rooms[player.currentRoom.id]:
          opposite = oppositeDir(exit)
          if visited_rooms[player.currentRoom.id][opposite]:
            print("already visited")
            pass
          elif opposite == move:
            visited_rooms[player.currentRoom.id] = {exit: prevRoom}
            visited_rooms[prevRoom] = {move: player.currentRoom.id}
            # unexplored_exits.add(f'{player.currentRoom.id}{exit}')
            move = oppositeDir(move)
            print('YESSSS')
            print(visited_rooms)
    except:
        print(f"no exit")

      # if exit != 'n':
      #   print('Maybe??????')
      #   unexplored_exits.add(f'{player.currentRoom.id}"?"')
    else:
      print(f"visited rooms ARE: {visited_rooms}")
      # print(f"exit is {exit}")
      # print(f"move is {move}")
      # unexplored_exits.add(f'{player.currentRoom.id}{exit}')
      # print('NOOOO')

    print(f"visited rooms after conditional check {visited_rooms}")
    print('current room after loop', player.currentRoom.id)
    # print('travel:', player.travel(move))
    traversalPath.append(move)
    print('traversalPath:', traversalPath)


    
    #update current_room and room
    visited_rooms

    # backtracking

    # inverseDirections = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
    # visited_rooms[current_room] = inverseDirections
    # print(visited_rooms)    

#BFS looking for nearest unexplored exit
    # else:
    #     q = Queue()
    #     q.put([userID])
    #     while q.qsize() > 0:
    #         path = q.get()
    #         v = path[-1]
    #         if v not in visited:
    #             visited[v] = path
    #             for friendship in self.friendships[v]:
    #                 if friendship not in visited:
    #                     q.put(list(path) + [friendship])

    #     return visited    