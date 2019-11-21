class User():
    def __init__(self,name,screen_name,profile_image_url,profile_banner_url):
        self.name=name
        self.screen_name=screen_name
        self.profile_image_url=profile_image_url
        self.profile_banner_url=profile_banner_url
        self.twitterUrl='https://twitter.com/'+self.screen_name
        #self.tweetDates=tweetDates
