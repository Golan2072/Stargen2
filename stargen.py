#Procedural star generator for PySmuggler


import utility


class Star:
    def atmo_gen(self):
        if self.size == 0:
            atmosphere = 0
        else:
            atmosphere = utility.dice(2, 6) - 7 + self.size
        if atmosphere > 15:
            atmosphere = 15
        if atmosphere < 0:
            atmosphere = 0
        return atmosphere

    def hydro_gen(self):
        hydrographics = utility.dice(2, 6) - 7 + self.size
        if self.size <= 1:
            hydrographics = 0
        elif self.atmosphere in [0, 1, 10, 11, 12]:
            hydrographics -= 4
        elif self.atmosphere == 14:
            hydrographics -= 2
        if hydrographics < 0:
            hydrographics = 0
        if hydrographics > 10:
            hydrographics = 10
        return hydrographics

    def pop_gen(self):
        population = utility.dice(2, 6) - 2
        if self.atmosphere >= 10:
            population -= 2
        elif self.atmosphere == 6:
            population += 3
        elif self.atmosphere in [5, 8]:
            population += 1
        if self.hydrographics == 0 and self.atmosphere < 3:
            population -= 1
        if population < 0:
            population = 0
        elif population > 10:
            population = 10
        return population

    def gov_gen(self):
        government = utility.dice(2, 6) - 7 + self.population
        if self.population == 0:
            government = 0
        if government < 0:
            government = 0
        if government > 15:
            government = 15
        return government

    def law_gen(self):
        law = utility.dice(2, 6) - 7 + self.government
        if self.government == 0:
            law = 0
        if law < 0:
            law = 0
        if law > 10:
            law = 10
        return law

    def starport_gen(self):
        starport_roll = utility.dice(2, 6) - 7 + self.population
        starport = "X"
        if starport_roll <= 2:
            starport = "X"
        elif starport_roll in [3, 4]:
            starport = "E"
        elif starport_roll in [5, 6]:
            starport = "D"
        elif starport_roll in [7, 8]:
            starport = "C"
        elif starport_roll in [9, 10]:
            starport = "B"
        elif starport_roll >= 11:
            starport = "A"
        if self.population == 0:
            starport = "X"
        return starport

    def gas_gen(self):
        if utility.dice(2, 6) >= 5:
            return "*"
        else:
            return " "
    
    def type_gen(self):
        if self.hydrographics >= 1:
            return "@"
        if self.hydrographics < 1:
            return "0"

    def __init__(self, hex_column, hex_row):
        if utility.dice(1, 6) >= 4:
            self.size = utility.dice(2, 6) - 2
            self.atmosphere = self.atmo_gen()
            self.hydrographics = self.hydro_gen()
            self.population = self.pop_gen()
            self.government = self.gov_gen()
            self.law = self.law_gen()
            self.startype = self.type_gen()
            self.gas_giant = self.gas_gen()
            self.starport = self.starport_gen()
            self.naval = " "
            self.scout = " "
            self.names = "TEST"
            self.column = hex_column
            self.row = hex_row
        else:
            self.size = 0
            self.atmosphere = 0
            self.hydrographics = 0
            self.population = 0
            self.government = 0
            self.law = 0
            self.startype = " "
            self.gas_giant = " "
            self.starport = "   "
            self.naval = " "
            self.scout = " "
            self.names = "       "
            self.column = hex_column
            self.row = hex_row
        if self.column == 10 and self.row != 10:
            self.hex = f"100{self.row}"
        elif self.column != 10 and self.row == 10:
            self.hex = f"0{self.column}10"
        elif self.column == 10 and self.row == 10:
            self.hex = "1010"
        else:
            self.hex = f"0{self.column}0{self.row}"
        self.neighbors = [(self.column, self.row - 1), (self.column + 1, self.row - 1), (self.column + 1, self.row),
                          (self.column, self.row + 1), (self.column - 1, self.row), (self.column - 1, self.row - 1)]
        self.second_neighbors = [(self.column, self.row-2), (self.column+1, self.row-2), (self.column+2, self.row-1), (self.column+2, self.row), (self.column+2, self.row+1), (self.column+1, self.row+1), (self.column, self.row+2), (self.column-1, self.row+1), (self.column-2, self.row+1), (self.column-2, self.row), (self.column-2, self.row-1), (self.column-1, self.row-2)]

    def name_converter(self):
        new_name = f"{self.names: <{7}}".upper()
        self.mapname = (new_name[:7]) if len(new_name) > 7 else new_name