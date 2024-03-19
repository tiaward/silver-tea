# a program to calculate a holiday cost using functions


city_flight=input("""Please enter the name of the city you are flying to.
                    Enter "A" for Prague
                    Enter "B" for Berlin
                    Enter "C" for Rome""")

num_nights=int(input("How many nights will you be staying?"))
rental_days=int(input("How many days will you be hiring a car?"))


def hotel_cost(x):
    y = x * 130
    return(y)

total_hotel = hotel_cost(num_nights)


def plane_cost(k):
    w = k
    return(w)

v=3

if city_flight == "A":
    v = 70
elif city_flight =="B":
    v= 60
elif city_flight == "C":
    v = 120
else:
    print("Invalid answer please try again.")

total_plane = plane_cost(v)
    
def car_rental(r):
    t = r * 25
    return(t)

total_car = car_rental(rental_days)

print("Your flight will cost: $",total_plane)
print("Your total hotel cost will be: $", total_hotel)
print("Your total car rental cost will be: $", total_car)
print("Your total holiday cost will be: $", str(total_car+total_plane+total_hotel))










             

