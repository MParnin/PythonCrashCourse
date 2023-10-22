current_users = ['admin', 'mike', 'michaela', 'steve', 'jason']
new_users = ['admin', 'shane', 'andy', 'joey', 'michaela']

if users:

    for user in users:
        if user == 'admin':
            print(f"Hello {user}, would you like a status report?")

        else:
            print(f"Hello {user}.")
else:
    print("Enter username.")
