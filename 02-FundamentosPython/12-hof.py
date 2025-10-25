import re


def require_auth(func):
    def wrapper(user):
        if user.lower() == "admin":
            return func(user)
        else:
            return "Access denied"
    
    
    return wrapper

def admin_dashboard(user):
    return f"Bienvenido al panel {user}"

auth_view_dashboard = require_auth(admin_dashboard)

print(auth_view_dashboard("Admin"))  # Output: Bienvenido al panel admin
print(auth_view_dashboard("invitado"))  # Output: Access denied