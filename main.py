from bikeRentalApp import BikeRental, Customer


def main():
    shop = BikeRental(100)
    customer = Customer()
    
    while True:
        print(""""
        =======Bike Rental App=======
              1.Display available bikes
              2.Request a bike on hourly basis $5
              3.Request a bike on daily basis $20
              4.Request a bike on weekly basis $60
              5.Return a bike
              6.Exit
              """)
        
        choice = input("Enter choice: ")

        try:
            choice = int(choice)
        except ValueError:
            print("The number of choice is not valid")
            continue

        if choice == 1:
            shop.displayStock()

        elif choice == 2:
             customer.rentalTime = shop.rentBikeOnHourlyBasis(customer.requestBike())
             customer.rentalBasis = 1

        elif choice == 3:
             customer.rentalTime = shop.rentBikeOnDailyBasis(customer.requestBike())
             customer.rentalBasis = 2

        elif choice == 4:
             customer.rentalTime = shop.rentBikeOnWeeklyBasis(customer.requestBike())
             customer.rentalBasis = 3   

        elif choice == 5:
             customer.bill = shop.returnBike(customer.returnBike())       
             customer.rentalBasis, customer.rentalTime, customer.bikes = 0,0,0

        elif choice == 6:
            break

        else:
           print("Invalid choice. Please enter a number between 1-6 ")

    print("Thank you for using bike rental App. ")   


if __name__ == "__main__":
    main()
