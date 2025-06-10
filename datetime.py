"""
from datetime import datetime
x=datetime.now()
print("Current date and time: ",x)
print(x.strftime("%a ,%d %B %Y"))
d=datetime(2025,5,4,13,15,30)
print(d)
"""
from datetime import datetime, timedelta
x=datetime.now()
print(x -timedelta(weeks=2,days=5,hours=10,minutes=34,seconds=55))
