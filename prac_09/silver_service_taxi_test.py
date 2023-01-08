from silver_service_taxi import SilverServiceTaxi


my_silver_service_taxi = SilverServiceTaxi('Silver Service Taxi 1', 100, 2)
my_silver_service_taxi.drive(18)
print(my_silver_service_taxi)
print(f"Current Fare: ${my_silver_service_taxi.get_fare():.2f}")
my_silver_service_taxi.drive(88)
print(my_silver_service_taxi)
print(f"Current Fare: ${my_silver_service_taxi.get_fare():.2f}")