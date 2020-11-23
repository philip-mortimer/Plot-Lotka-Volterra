"""
    Copyright 2020 Philip Mortimer
    
    This file is part of Philip Mortimer Example Programs.
    
    Philip Mortimer Example Programs is free software: you can redistribute it 
    and/or modify it under the terms of the GNU General Public License as 
    published by the Free Software Foundation, either version 3 of the License,
    or (at your option) any later version.
    
    Philip Mortimer Example Programs is distributed in the hope that it will be
    useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with Philip Mortimer Example Programs.  If not, see 
    <https://www.gnu.org/licenses/>.
"""


from Series import Series

class InitialPopulationDensities:
    def __init__(self, predators, prey):
        self.__predators = predators
        self.__prey = prey

    @property
    def predators(self):
        return self.__predators
 
    @property
    def prey(self):
        return self.__prey


class Coefficients:
    def __init__(
        self, prey_growth_rate, predation_rate, predator_growth_rate, 
        predator_mortality_rate
    ):
        self.__prey_growth_rate = prey_growth_rate
        self.__predation_rate = predation_rate
        self.__predator_growth_rate = predator_growth_rate
        self.__predator_mortality_rate = predator_mortality_rate

    @property
    def prey_growth_rate(self):
        return self.__prey_growth_rate

    @property
    def predation_rate(self):
        return self.__predation_rate

    @property
    def predator_growth_rate(self):
        """Predator growth rate as a result of predation."""
        return self.__predator_growth_rate

    @property
    def predator_mortality_rate(self):
        return self.__predator_mortality_rate


class TimeParams:
    def __init__(self, dt, run_time):
        self.__dt = dt
        self.__run_time = run_time

    @property
    def dt(self):
        """
        Length of time interval which elapses during each iteration of the
        model.
        """
        return self.__dt

    @property
    def run_time(self):
        """
        Specifies that the model should run until:
        
            number of iterations * dt >= run_time
        
        where number of iterations is number of times that model time advances
        by time interval dt.
        """
        return self.__run_time

class PopulationLabels:
    """Text labels to appear on plots etc. for the predators and prey."""
    def __init__(self, predator_label, prey_label):
        self.__predator_label = predator_label
        self.__prey_label = prey_label

    @property
    def predator_label(self):
        """e.g. "lions"."""
        return self.__predator_label

    @property
    def prey_label(self):
        """e.g. "antelope"."""
        return self.__prey_label


class Results:
    def __init__(
        self, time_series, predator_series: Series, prey_series: Series
    ):
        self.__time_series = time_series
        self.__predator_series = predator_series
        self.__prey_series = prey_series

    @property
    def time_series(self):
        return self.__time_series

    @property
    def predator_series(self):
        return self.__predator_series
  
    @property
    def prey_series(self):
        return self.__prey_series


def get_delta_predators(predators, prey, coeffs: Coefficients):
    """
    Returns change in number of predators per unit time.
    """
    return coeffs.predator_growth_rate * predators * prey \
            - coeffs.predator_mortality_rate * predators


def get_delta_prey(predators, prey, coeffs: Coefficients):
    """
    Returns change in number of prey per unit time.
    """
    return coeffs.prey_growth_rate * prey \
            - coeffs.predation_rate * predators * prey


def get_new_predators_and_prey(predators, prey, dt, coeffs: Coefficients):
    """
    predators: current number of predators

    prey:      current number of prey

    dt:        time interval over which change in number of predators and prey
               takes place

    coeffs:    coefficients such as prey growth rate

    Returns number of predators and prey after time elapsed has increased by
    dt. It uses the midpoint method.
    """
    half_dt = 0.5 * dt

    midpoint_predators = predators + half_dt * get_delta_predators(
        predators, prey, coeffs
    )

    midpoint_prey = prey + half_dt * get_delta_prey(
        predators, prey, coeffs
    )

    new_predators = predators + dt * get_delta_predators(
        midpoint_predators, midpoint_prey, coeffs
    )

    new_prey = prey + dt * get_delta_prey(
        midpoint_predators, midpoint_prey, coeffs
    )

    return (max(0, new_predators), max(0, new_prey))   


class Model:
    """ 
    A class for creating, running, and obtaining the results of running, the
    Lotka-Volterra model.
    """
    def __init__(self, 
        initial_population_densities: InitialPopulationDensities,
        coeffs: Coefficients,
        time_params: TimeParams,
        population_labels: PopulationLabels,
        trace_on=False
    ):
        self.__prey = initial_population_densities.prey
        self.__predators = initial_population_densities.predators

        self.__coeffs = coeffs
        self.__time_params = time_params
        self.__population_labels = population_labels
        self.__trace_on = trace_on

        self.__curr_time = 0.0
              
    @property
    def predators(self):
        """Current predator population density."""
        return self.__predators

    @property
    def prey(self):
        """Current prey population density."""
        return self.__prey

    @property
    def curr_time(self):
        return self.__curr_time
  
    def advance(self):
        """
        Advances the model by a time increment equal to the value of the dt
        property resulting in the update of the predators, prey and curr_time 
        properties. If the trace_on property is True it will also print the 
        values of these properties to standard output after it has updated 
        them. If the model cannot be advanced because curr_time >= run_time
        then it will return False, otherwise it will return True.
        """
        if self.curr_time >= self.__time_params.run_time:
            return False      

        self.__predators, self.__prey = get_new_predators_and_prey(
            self.predators, self.prey, self.__time_params.dt, self.__coeffs
        )     
        
        self.__curr_time += self.__time_params.dt

        self.__trace()
        return True

    def run(self):
        """
        Advances the model until the value of the curr_time property is >= 
        the run_time property of the TimeParams instance passed to the 
        constructor. It returns the results of running the model in an 
        instance of the Results class.
        """
        time_series = [self.curr_time]
        predator_series = [self.predators]
        prey_series = [self.prey]
   
        while self.advance():
            time_series.append(self.curr_time)
            predator_series.append(self.predators)
            prey_series.append(self.prey)
      
        predator_series_obj = Series(
            predator_series, self.__population_labels.predator_label
        )
                                    
        prey_series_obj = Series(
            prey_series, self.__population_labels.prey_label
        )
      
        results = Results(
            time_series, predator_series_obj, prey_series_obj
        )
        return results

    def __trace(self):
        if self.__trace_on:
            print(
                "time={:g}, prey={:g}, predators={:g}".format(
                    self.__curr_time, self.prey, self.predators
                )
            )

      
        

