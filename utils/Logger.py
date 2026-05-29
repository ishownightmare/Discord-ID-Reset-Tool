import utils.Color as Color


def log(catagory,message):
    print(f"{Color.Colors.FRIENDS}[FRIENDS]{Color.Colors.RESET} {message}") if catagory == "FRIENDS" else None
    print(f"{Color.Colors.GROUPS}[GROUPS]{Color.Colors.RESET} {message}") if catagory == "GROUPS" else None
    print(f"{Color.Colors.SERVERS}[SERVERS]{Color.Colors.RESET} {message}") if catagory == "SERVERS" else None
    print(f"{Color.Colors.DMS}[DMS]{Color.Colors.RESET} {message}") if catagory == "DMS" else None