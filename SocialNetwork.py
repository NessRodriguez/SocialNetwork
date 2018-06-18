## Made by Vanessa Rodriguez
## My Social Network

class User:
    def __init__(self, firstName, lastName, username, bio, userID):
        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.bio = bio
        self.userID = userID
        self.friends = []
        self.posts = []

    def addFriend(self, username):
        self.friends.append(username)

##    def unFriend():

    def viewNewsFeed(self, friends):
         for friend in self.friends:
           print (friends.posts)

if __name__ == "__main__":
    firstName = "Vanessa"
    lastName = "Rodriguez"
    username = "NessRodriguez"
    bio = "I like pie?"
    userID = "666"

    vanessa = User(firstName, lastName, username, bio, userID)
    james = User("James", "Abasta", "JamesIsApasta", "Pasta", "1003")
    lando = User("Lando", "Calrissian", "LandoDamndo", "Let go of the mean man’s face.", "3005")
    print (vanessa.firstName)
    print (james.firstName)
    print (lando.firstName)

    vanessa.addFriend("JamesIsApasta")
    vanessa.addFriend("LandoDamndo")
    print (vanessa.friends)
    james.posts.append("I'm Apasta")
    lando.posts.append("Send Help")
    vanessa.viewNewsFeed(username)


    ## print (friend.posts)

    ## 1) Have 2 Friends
    ## 2) Add friends to your friends list
    ## 3) Create a post for each friend
    ## 4) Output post of each friend in MAIN
    ## 5) Output post of each friend in viewNewsFeed() function
