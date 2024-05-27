import sys
from db_helper import Db_helper
class Flipkart:
    def __init__(self):
        self.db=Db_helper()
        self.menu()



    def menu(self):
        user_input=input('''
            1.Enter 1 to register
              2. Enter 2  to  loging
              3. Enter anything to leave 

              
              
              
            ''')
        if user_input=="1":
            self.register()
        elif user_input=='2':
            self.login()
        else:
            sys.exit(1000)

if __name__=='__main__':
    obj=Flipkart()
    
