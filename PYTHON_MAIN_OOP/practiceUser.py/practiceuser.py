class users:
    
    def __init__(self, first_name,last_name, email,age):
        self.first_name=first_name
        self.email=email
        self.age=age
        self.last_name=last_name

    def display_info(self):
        print(self.first_name)
        print(self.email)  
        print(self.age)
        print(self.last_name)
        return self

    def enroll(self):
        self.enroll() 
        print ('enrollment was successful')
        return self

    def spend_points(self, amount):
        self.spend_points(amount)
        print ('spend was successful')
        return self
    

user1 = {"med","min","max@gmail.com","100"}
