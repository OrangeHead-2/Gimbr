def has_permission(user, action):
    # Example: only admin can "deploy"
    if action == "deploy" and user.get("role") != "admin":
        return False
    return True