def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}"
        print (msg)
usernames = ("toh", "liam", "layne", "deno")
greet_users(usernames)

    