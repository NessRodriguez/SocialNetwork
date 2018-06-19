## Made by Vanessa Rodriguez
## My Social Network

class User:
    def __init__(self, username):
        self.username = username
##        self.firstName = " "
##        self.lastName = " "
##        self.bio = " "
        self.friends = []
        self.posts = []

    def addFriend(self, person):
        self.friends.append(person)

    def removeFriend(self, username):
        for friend in self.friends:
            if friend.username == username:
                self.friends.remove(User(username))
        
##    def addFirstName(self, firstName):
##        self.firstName = firstName
##    def addLastName(self, lastName):
##        self.lastName = lastName
##    def addBio(self, bio):
##        self.bio = bio
                
    def addPost(self, post):
        self.posts.append(post)

    def showUsernames(self):
        for friend in self.friends:
            print (friend.username)
            
    def viewNewsFeed(self):
         for friend in self.friends:
            print (friend.posts)

if __name__ == "__main__":

    username = "BandNerd"

    Vanessa = User("BandNerd")
    James = User("JamesIsApasta")
    Lando = User("LandoDamndo")
    Erick = User("BarronCabezon")
    Chuck = User("ChuckTheChuckster")

    Vanessa.addFriend(James)
    Vanessa.addFriend(Lando)
    Vanessa.addFriend(Erick)
    Vanessa.addFriend(Chuck)
    
    James.posts.append("I'm Apasta")
    Lando.posts.append("Send Help")
    Erick.posts.append("Quiero Comer")
    Chuck.posts.append("I'm A Chuckster")

    Vanessa.removeFriend(Chuck)
    
    Vanessa.viewNewsFeed()
    Vanessa.showUsernames()
    Vanessa.addPost("Go Away")
   
##    vanessa.addFirstName("Vanessa")
##    vanessa.addLastName("Rodriguez")
##    vanessa.addBio("I like pie?")

  


    ## print (friend.posts)

    ## 1) Have 2 Friends
    ## 2) Add friends to your friends list
    ## 3) Create a post for each friend
    ## 4) Output post of each friend in MAIN
    ## 5) Output post of each friend in viewNewsFeed() function
