
def require_auth(func):
    def wrapper(user):
        if user.lower() == "admin":
            return func(user)
        else:
            return "Access denied"
    
    
    return wrapper


@require_auth
def admin_dashboard(user):
    return f"Bienvenido al panel {user}"

print(admin_dashboard("Admin")) 
print(admin_dashboard("ADMIN"))  