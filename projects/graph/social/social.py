import random
import queue 

class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments
        Creates that number of users and a randomly distributed friendships
        between those users.
        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # user.name = f"User {id}" giving a user a name
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(numUsers):
            self.addUser(f"User {i+1}")

        # create friendships
        possibleFriendships = []
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                possibleFriendships.append((userID, friendID))
        random.shuffle(possibleFriendships)
        print("possible Friendships: ", possibleFriendships[:10])
        print("possible Friendships length: ", len(possibleFriendships))
        for friendship in possibleFriendships[: (numUsers * avgFriendships)// 2]:
            self.addFriendship(friendship[0], friendship[1])
        # Create friendships
        # total == avg

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.
        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        
        # Create an empty queue
        q = queue.SimpleQueue()
        # Put UserID in our Queue as a list item
        q.put([userID])
        
        # while queue is not empty...
        while q.qsize() > 0:
            #Dequeue first path from queue
            path = q.get()
            # get the current node from the last element in the path
            v = path[-1]
            # if that node is not in the visited dict
            if v not in visited:
                # mark it as visited
                visited[v] = path
                
                # Then, iterate through all friendships in the set
                for friendship in self.friendships[v]:
                   #if a friendship is not in the visited dict
                   if friendship not in visited:
                       # add the path (As a list) plus the friendship to the queue
                       q.put(list(path) + [friendship])
                    
        return visited

    def social_paths(self, userID):
        visited = {}
        q = Queue()
        q.enqueue([userID])
        while q.size > 0:
            path = q.dequeue()
            newUserID = path[-1]
            if newUserID not in visited:
                visited[newUserID] = path
                for friendID in self.friendships[newUserID]:
                    if friendID not in visited:
                        new_path = list(path)
                        new_path.append(friendID)
                        q.enqueue(new_path)
        return visited                





if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    connections = sg.getAllSocialPaths(1)
    print(f"connections is {connections}")