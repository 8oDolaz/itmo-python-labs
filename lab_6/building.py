class Building:
    def __init__(self, area, cost_per_sqm, num_residents):
        self.area = area
        self.cost_per_sqm = cost_per_sqm
        self.num_residents = num_residents

    def calculate_total_cost(self):
        return self.area * self.cost_per_sqm

    def cost_per_resident(self):
        return self.calculate_total_cost() / self.num_residents

class CountryHouse(Building):
    def __init__(self, area, cost_per_sqm, num_residents, garden_area):
        super().__init__(area, cost_per_sqm, num_residents)
        self.garden_area = garden_area

    def calculate_total_cost(self):
        base_cost = super().calculate_total_cost()
        return base_cost + (self.garden_area * self.cost_per_sqm * 0.5)

class ApartmentBuilding(Building):
    def __init__(self, area, cost_per_sqm, num_residents, num_apartments):
        super().__init__(area, cost_per_sqm, num_residents)
        self.num_apartments = num_apartments

    def calculate_total_cost(self):
        base_cost = super().calculate_total_cost()
        return base_cost + (self.num_apartments * 10000)
