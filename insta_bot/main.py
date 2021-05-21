from instapy import InstaPy
from tags import tag_list

session = InstaPy(username="reactivezoid", password="reactivezoid1234")
session.login()

session.set_relationship_bounds(enabled=True, max_followers=1000)
session.set_do_follow(True, percentage=100)
session.like_by_tags(tag_list, amount=5)

session.end()
