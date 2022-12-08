from datetime import datetime

def isonow():
    return datetime.utcnow().isoformat()