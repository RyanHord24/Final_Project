class User:
#Class attributes and methods
    posts = []

#Instance attributes, getters and setters
    def __init__(self, name=None, email=None, drivers_license=None):
        self._name = name
        self._email = email
        self._drivers_license = drivers_license
        self.User_posts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if (
            type(new_name) == str
            and len(new_name) >= 3
            and new_name.isalpha()
            and new_name[0].isupper()
        ):
            self._name = new_name

    @property
    def email(self):
        return self._email   

    @email.setter
    def email(self, new_email):
        if (
            type(new_email) == str
            and '@' in new_email
            and '.com' in new_email
        ):
            self._email = new_email

    @property
    def drivers_license(self):
        return self._drivers_license

    @drivers_license.setter
    def drivers_license(self, new_drivers_license):
        if (
            type(new_drivers_license) == str
            and len(new_drivers_license) == 6
            and new_drivers_license[:4].isalpha()
            and new_drivers_license[4:].isdigit()
        ):
            self._drivers_license = new_drivers_license

    def create_a_post(self):
        new_post = input('Please type your post: ')
        User.posts.append(new_post)
        self.User_posts.append(new_post)

    def delete_a_post(self):
        post_index = input('Type out the index that should be deleted: ') - 1
        User.posts.remove(User.posts[post_index])
        self.User_posts.remove(self.User_posts[post_index])

    def see_all_posts(self):
        if len(User.posts) >= 1:
            print(User.posts)

    def see_my_posts(self):
        if len(User.posts) >= 1:
            print(self.User_posts)