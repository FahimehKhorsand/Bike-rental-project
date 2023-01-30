
import datetime


class BikeRental:

    #Constructor class for bike rental shop
    def __init__(self,stock=0):

        self.stock = stock

    #Show bikes available for rent
    def displayStock(self):

        print("we have currently {} bikes for rent.".format(self.stock))
        return self.stock
    
    #Bike rental on a hourly basis
    def rentBikeOnHourlyBasis(self, bik_cnt):
           
        if  bik_cnt <= 0:
            print("Number of bikes is invalid")
            return None
        
        elif bik_cnt > self.stock:
            print("Sorry, we have currently {} bikes for rent.".format(self.stock))
            return None

        else:
         current_datetime = datetime.datetime.now()
        print("you have rented {} bike(s) on hourly basis today at {} hours.".format(bik_cnt,current_datetime.hour))
        print("you will be charged $5 for each hour per bike.")
        print("we hope that you enjoy our service")

        self.stock -= bik_cnt
        return current_datetime
    
    
    #Bike rental on a daily basis
    def rentBikeOnDailyBasis(self,bik_cnt):
         
        if bik_cnt <= 0:
            print("Number of bikes is invalid")
            return None
        
        elif bik_cnt > self.stock:
            print("Sorry, we have currently {} bikes for rent.".format(self.stock))
            return None


        else:
         current_datetime = datetime.datetime.now()
        print("you have rented {} bike(s) on hourly basis today at {} hours.".format(bik_cnt,current_datetime.hour))
        print("you will be charged $20 for each hour per bike.")
        print("we hope that you enjoy our service")

        self.stock -= bik_cnt
        return current_datetime
    
    
    #Bike rental on a weekly basis
    def rentBikeOnWeeklyBasis(self,bik_cnt):

        if bik_cnt <= 0:
            print("Number of bikes is invalid")
            return None
        
        elif bik_cnt > self.stock:
            print("Sorry, we have currently {} bikes for rent.".format(self.stock))
            return None
        
        
        else:
         current_datetime = datetime.datetime.now()
        print("you have rented {} bike(s) on hourly basis today at {} hours.".format(bik_cnt,current_datetime.hour))
        print("you will be charged $60 for each hour per bike.")
        print("we hope that you enjoy our service")

        self.stock -= bik_cnt
        return current_datetime
    

    def returnBike(self,request):

        rentalTime, rentalBasis, numberOfBikes = request
        bill = 0

        if rentalTime and rentalBasis and numberOfBikes:
            self.stock += numberOfBikes
            current_datetime = datetime.datetime.now()
            rentalPeriod = current_datetime - rentalTime


            #hourly bill calculation
            if rentalBasis == 1:
                bill = round(rentalPeriod.seconds / 3600) * 5 * numberOfBikes

            #daily bill calculation
            elif rentalBasis == 2:
                bill = round(rentalPeriod.days) * 20 * numberOfBikes

            #weekly bill calculation
            elif rentalBasis == 3:
                bill = round(rentalPeriod.days / 7) * 60 * numberOfBikes

            if (3 <= numberOfBikes <= 5):
                print("you are eligible for family rental promotion of %30 discount")
                bill = bill * 0.7

            print("Thank you for returning your bike. Hope you enjoyed our service")
            print("That would be ${}.".format(bill))
            return bill
    
        else:
            print("Are you sure you rented a bike with us")
            return None
        

class Customer:      

    def __init__(self):
        self.bikes = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0

    def requestBike(self):
    
        bikes = input("How many bikes would you like to rent? ")

        try:
            bikes = int(bikes)
        except ValueError:
            print("That is not a positive integer!")
            return -1
        
        if bikes < 1:
           print("Invalid input. Number of bikes should be greater than zero")
           return -1
        else:
            self.bikes = bikes
        return self.bikes

    def returnBike(self):    
        
        if self.rentalBasis and self.rentalTime and self.bikes:
           return self.rentalTime, self.rentalBasis, self.bikes
        else:
            return 0,0,0