## Made by Vanessa Rodriguez
## My Social Network

class User:
    def __init__(self, username, userID):
        self.username = username
        self.firstName = " "
        self.lastName = " "
        self.bio = " "
        self.friends = []
        self.posts = []
        self.userID = userID

    def addFriend(self, person):
        self.friends.append(person)

    def removeFriend(self, person):
                self.friends.remove(person)
        
    def addFirstName(self, firstName):
        self.firstName = firstName
    def addLastName(self, lastName):
        self.lastName = lastName
    def addBio(self, bio):
        self.bio = bio
                
    def addPost(self, post):
        self.posts.append(post)

    def showUsernames(self):
        for friend in self.friends:
            print (friend.username)
            
    def viewNewsFeed(self):
         for friend in self.friends:
            print (friend.posts)
            
    def createPost(self, content):
        myPost = post(content)
        self.post.append(myPost)
        myPost.createPostID(len(posts))

    def createUserID(self, num):
        self.userID = num
    
class Post:
    def __init__(self, content):
        self.content = content
        self.postID = " "
        self.comment = []
        
    def createPostID(self, num):
        self.postID = num

    def addComment(self, comment):
        self.comments.append(comment)

class Network:
    def __init__(self):
        self.users = []

    def createUser(self, username):
        for user in self.users:
            if (user.username == username):
                print ("Username Taken")
        mySize = len(self.users) + 1
        myUser = User(username, mySize)
        self.users.append(myUser)
        print ("User Created")
    def getOBJ(self, username):
        userID = self.getUserID(username)
        userOBJ = self.users[userID - 1]
        return userOBJ
    def getUserID(self, username):
        for user in self.users:
            if user.username == username:
                return user.userID

if __name__ == "__main__":
    network = Network()
    network.createUser("BandNerd")
    BandNerd = network.getOBJ("BandNerd")
    print (BandNerd.username)
    network.createUser("JamesIsApasta")
    JamesIsApasta = network.getOBJ("JamesIsApasta")
    print (JamesIsApasta.username)
    network.createUser("LandoDamndo")
    LandoDamndo = network.getOBJ("LandoDamndo")
    print (LandoDamndo.username)
    network.createUser("BarronCabezon")
    BarronCabezon = network.getOBJ("BarronCabezon")
    print (BarronCabezon.username)
    network.createUser("Chuck")
    Chuck = network.getOBJ("Chuck")
    print (Chuck.username)
    
##    username = "BandNerd"
##    
##    Ness = User("BandNerd")
##    James = User("JamesIsApasta")
##    Lando = User("LandoDamndo")
##    Erick = User("BarronCabezon")
##    Chuck = User("Chuck")
##
##    Ness.addFriend(James)
##    Ness.addFriend(Lando)
##    Ness.addFriend(Erick)
##    Ness.addFriend(Chuck)
##    
##    James.posts.append("I'm Apasta")
##    Lando.posts.append("Send Help")
##    Erick.posts.append("Quiero Comer")
##    Chuck.posts.append("I'm Chuck")
##    
##    Ness.viewNewsFeed()
##    Ness.showUsernames()
##    Ness.addPost("Go Away")
##
##    Ness.removeFriend(Chuck)
##    Ness.showUsernames()
##    Ness.addComment(postID,"Help")
##   
##    Ness.addFirstName("Vanessa")
##    Ness.addLastName("Rodriguez")
##    Ness.addBio("I like pie?")
##
##    print (len(network.users))

    ## 1) Have 2 Friends
    ## 2) Add friends to your friends list
    ## 3) Create a post for each friend
    ## 4) Output post of each friend in MAIN
    ## 5) Output post of each friend in viewNewsFeed() function
