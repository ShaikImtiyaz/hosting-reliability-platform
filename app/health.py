from datetime import datetime

def health():

    return {
        "status": "UP",
        "time": str(datetime.now())
    }
