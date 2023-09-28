from building import CountryHouse, ApartmentBuilding

def main():
    country_house = CountryHouse(area=200, cost_per_sqm=1500, num_residents=4, garden_area=100)
    apartment_building = ApartmentBuilding(area=1000, cost_per_sqm=2000, num_residents=20, num_apartments=10)

    print(f"Общая стоимость деревенского дома: {country_house.calculate_total_cost()} руб.")
    print(f"Соотношение стоимости к числу проживающих: {country_house.cost_per_resident()} руб/человек")

    print(f"Общая стоимость многоквартирного дома: {apartment_building.calculate_total_cost()} руб.")
    print(f"Соотношение стоимости к числу проживающих: {apartment_building.cost_per_resident()} руб/человек")

if __name__ == '__main__':
    main()
