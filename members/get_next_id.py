#get_next_id

def get_next_id(members):
    current = len(members)
    new = current + 1
    return f"{new:04}"