from instapy import InstaPy
from instapy import smart_run
your_password = ""
session = InstaPy(username="botted7777", password=your_password, headless_browser=False)
with smart_run(session):
    session.set_relationship_bounds(enabled=True, delimit_by_numbers=True, max_followers=5000, min_following=10, min_followers=10)
    session.follow_user_followers(['cristiano'], amount=10, randomize=False)
    #session.unfollow_users(amount=10, allFollowing=True)
    session.end()