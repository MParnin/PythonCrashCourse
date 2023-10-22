current_users = ['admin', 'mike', 'michaela', 'steve', 'jason']
new_users = ['admin', 'shane', 'andy', 'joey', 'michaela']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user} is already taken.")

    else:
        print(f"{new_user} is available.")
