from tweetdata import TwitterUser
from userDAO import User
class UserService():
    def __init__(self,screen_name,limit_tweets):
        self.twitterUser=TwitterUser(screen_name,limit_tweets)
    def autenticarUsuario(self):
        return self.twitterUser.autenticarUsuario()
    def getUserDAO(self):
        return User(self.twitterUser.user.name,self.twitterUser.screen_name,self.twitterUser.user.profile_image_url,self.twitterUser.user.profile_banner_url)
    def getStadistics(self):
        return self.twitterUser.getStadistics()