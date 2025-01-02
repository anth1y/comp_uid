import pwd

def get_users():
    users = []
    for user in pwd.getpwall():
        if user.pw_uid >= 1000:
            users.append(user.pw_name)
    return users

def get_uid():
    # we want to use our users list to get an uid from each one
    try:
        users = get_users()
        for u in users:
            return pwd.getpwnam(u).pw_uid
    except KeyError:
            return None
 # navigate to the users homedir read a file and capture it's contents to compare to the iterator `u`
if __name__ == "__main__":
    uid = get_uid()
    print(uid)
