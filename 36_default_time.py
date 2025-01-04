from datetime import datetime

def myfun(msg,date = datetime.utcnow()):
  
    print('Message is => ',msg)
    print("Time is => ",date)
    
    
myfun("hello")


def myfun1(msg, date = None):
   
  date = datetime.utcnow()
  print("The message is => {0} and the time is {1}".format(msg,date))
  
  
myfun1("hello")