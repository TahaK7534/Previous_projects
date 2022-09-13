import numpy as np
import matplotlib.pyplot as plt

class Subregion:
    """A class used to create a School object.

        Attributes:
            name (str): String that represents the school's name
            code (int): Integer that represents the school's code
    """

    def __init__(self, country, population_density, threatened_species, threatened_density):
        self.country = country
        self.population_density = population_density
        self.threatened_species = threatened_species
        self.threatened_density = threatened_density
    def print_all_stats(self):
        """A function that prints the name and code of the school instance.

        Parameters: None
        Return: None 

        """
        print('Population density:{1}\n    Number of Threatened Species:{2}\n    Threatened species Density (Threatened species per sq km):{3}\n'.format(self.country, self.population_density, self.threatened_species, self.threatened_density))

def np_pop_density(population_density):
    max_min_pop_density = [] 
    max_min_pop_density.append(np.min(population_density))
    max_min_pop_density.append(np.max(population_density))
    return(max_min_pop_density)
def np_threatened_density(threatened_species_per_sq_km):
    max_min_threatened_density = [] 
    max_min_threatened_density.append(np.min(threatened_species_per_sq_km))
    max_min_threatened_density.append(np.max(threatened_species_per_sq_km))
    return(max_min_threatened_density)

def main():
    Threatened_Species = np.genfromtxt('Threatened_Species.csv',delimiter=',', skip_header= True, dtype= str) #Imports data from csv file to numpy array
    Country_Data = np.genfromtxt('Country_Data.csv',delimiter=',', skip_header= True, dtype= str) #Imports data from csv file to numpy array
    Population_Data = np.genfromtxt('Population_Data.csv',delimiter=',', skip_header= True, dtype= str) #Imports data from csv file to numpy array
    
    subregions = Country_Data[:,2] #Takes the coloumn with subregions
    print(subregions) #Prints all sub-regions
    stop = False #Varaible used to create loop condition.
    while stop != True: #A loop to run the code until the user input is valid.
        subregion_input = (input("Please select a subregion: ")) #Prompts for user input of a subregion
        if (subregion_input not in str(subregions)):
            print("You must enter a valid region.") #Promts the user for re-entry of subregion if input was invalid
        elif subregion_input in subregions:
            stop = True #Changes the looping variable to True to stop loop
    intra_countries = [] #Empty list
    populations = [] #Empty list
    population_density = [] #Empty list
    total_Threatened_Species = [] #Empty list
    country_population_density = [] #Empty list
    threatened_species_per_sq_km = [] #Empty list
    for i in range(len(subregions)): #Iterates a variable through the list of subregions for index lookup
        if (subregion_input == str(subregions[i])):
            countries = (Country_Data[i,0]) #Stores the index numbers for whenever the input matches the region name row in the arrays
            population_density_val = int(Population_Data[i, 1])/int(Country_Data[i,3]) #Population density calculation
            population_density.append(int(population_density_val)) #Stores the population density value to a list
            intra_countries.append(str(countries)) #Stores the countries within the subregion in a list
            #country_population_density.append(str(int(population_density_val))) #
            num_threatened = int(Threatened_Species[i, 1]) + int(Threatened_Species[i, 2]) + int(Threatened_Species[i, 3]) + int(Threatened_Species[i, 4]) #Calcultes the sum of threatened species
            total_Threatened_Species.append(num_threatened) #Stores sum of threatened species in a list
            threatened_species_density = num_threatened/float(Country_Data[i,3]) #Calculates threatened species per square km
            threatened_species_per_sq_km.append(float(threatened_species_density)) #Stores values threatened species per square km in a list

    print(intra_countries) #Prints countries within subregion to give user a selection
    quit = False
    while quit != True: #A loop to run the code until the user input is valid.
        country_input = (input("Select a country within the subregion to recieve data\n")) #Prompts user for country input
        for x in range(len(intra_countries)): #Iterates loop through countries within subregion
            if (country_input == str(intra_countries[x])): #Checks if input is valid
                subregion1 = Subregion(intra_countries[x], population_density[x], total_Threatened_Species[x], threatened_species_per_sq_km[x])
                subregion1.print_all_stats()
                quit =True

    total_Threatened_Species.sort()

    colours = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    for x in range(len(intra_countries)):
        plt.bar(population_density[x], total_Threatened_Species[x],color= colours[x], label = str(intra_countries[x])) #Plots the grades on the x axis and the array for 2021 on the y axis
    
    plt.legend (shadow = True, loc = 'upper left') #Creates a legend 
    plt.title("Number of Threatened Species vs Population Density of " + subregion_input) #Creates a title
    plt.xlabel("Population Density") #Creates x axis label
    plt.ylabel("Number of Threatened Species") #Creates a y axis label
    plt.show() #Plots the graph in a window

    m_population_density = np_pop_density(population_density)
    m_threatened_density = np_threatened_density(threatened_species_per_sq_km)
    for x in range(len(intra_countries)):
        plt.bar(m_population_density, m_threatened_density,color= colours[x], label = str(intra_countries[x])) #Plots the grades on the x axis and the array for 2021 on the y axis
    plt.legend (shadow = True, loc = 'upper left') #Creates a legend 
    plt.title("Threatened Species Density vs Population Density of" + subregion_input) #Creates a title
    plt.xlabel("Population Density") #Creates x axis label
    plt.ylabel("Threatened Species Density") #Creates a y axis label
    plt.show() #Plots the graph in a window

if __name__ == '__main__':
    main()

