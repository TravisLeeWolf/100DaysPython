from insta_follower import InstaFollower

SIMILAR_ACCOUNT = "londonappbrewery"

instaFollower = InstaFollower()

instaFollower.login()
instaFollower.find_followers(SIMILAR_ACCOUNT)
instaFollower.follow()
