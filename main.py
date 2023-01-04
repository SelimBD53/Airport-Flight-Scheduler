from TravelAgent import TravelAgent
def main():
    travel_agent = TravelAgent('GO Jaan')
    trip_info1 = travel_agent.set_trip_one_city_one_way('DAC','PRA','05/12/2022')
    # print('aircraft',trip_info1.aircraft)
    # print('price',trip_info1.price)

    trip_cities = ['DUB','LHR','SYD','JFK','ORD']
    trip_info2 = travel_agent.set_trip_multi_city_flexible_route(trip_cities,'5/12/2022')
    
    print('Price',trip_info2[1])
    for trip in trip_info2[0]:
        print(trip)

if __name__ == '__main__':
    main()