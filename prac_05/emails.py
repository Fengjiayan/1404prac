"""
Email
Estimate: 18 minutes
Actual:   22 minutes
"""


def extract_name(email):
    parts = email.split("@")[0].split(".")
    return " ".join([part.title() for part in parts])


name_email = {}
email = input("Email: ").strip()
while email != "":
    name = extract_name(email)
    user_confirm = input(f"Is your name {name}? (Y/n) ").strip()
    if user_confirm == "" or user_confirm == "y":
        name_email[name] = email
    else:
        name = input("Name: ")
        name_email[name] = email
    email = input("Email: ").strip()

print()
for name, email in name_email.items():
    print(f"{name} ({email})")
