from ums import User

regno = "12203693"
password = ".V4mwB8$B$.75vE"
user = User(registration=regno, password=password)

profile = user.user_profile()
print(profile)

# not working , expired package