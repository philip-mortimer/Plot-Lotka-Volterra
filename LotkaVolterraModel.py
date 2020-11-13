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


from lotka_volterra_lib import get_new_predators_and_prey
from LotkaVolterraResults import LotkaVolterraResults
import params as prm

class Coefficients:
    def __init__(self, 
        prey_growth_rate        = prm.PREY_GROWTH_RATE, 
        predation_rate          = prm.PREDATION_RATE,
        predator_growth_rate    = prm.PREDATOR_GROWTH_RATE,
        predator_mortality_rate = prm.PREDATOR_MORTALITY_RATE
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
        return self.__predator_growth_rate

    @property
    def predator_mortality_rate(self):
        return self.__predator_mortality_rate


class InitialPopulationDensities:
    def __init__(self, 
        predators = prm.INITIAL_PREDATORS,
        prey      = prm.INITIAL_PREY 
    ):
        self.__predators = predators
        self.__prey = prey

    @property
    def predators(self):
        return self.__predators
 
    @property
    def prey(self):
        return self.__prey
        

class TimeParams:
    def __init__(self, 
        max_time = prm.MAX_TIME,
        dt       = prm.DT
    ):
        self.__max_time = max_time
        self.__dt = dt

    # Length of time interval which elapses during each iteration of the model.
    @property
    def dt(self):
        return self.__dt

    # Maximum model time: dt * number of iterations will not exceed this time.
    @property
    def max_time(self):
        return self.__max_time


class LotkaVolterraModel:
   def __init__(self, 
            coeffs = Coefficients(),
            initial_population_densities = InitialPopulationDensities(),
            time_params = TimeParams(),
            trace_on = prm.TRACE
   ):
       self.__coeffs = coeffs
       self.__prey = initial_population_densities.prey
       self.__predators = initial_population_densities.predators
       self.__time_params = time_params
       self.__trace_on = trace_on

       self.__curr_time = 0.0
              
   # Current predator population density.    
   @property
   def predators(self):
      return self.__predators
  
   # Current prey population density.    
   @property
   def prey(self):
      return self.__prey

   @property
   def curr_time(self):
      return self.__curr_time

  
   def advance(self):
      """
      Advances the model by a time increment equal to the value of the dt
      property resulting in the update of the predators, prey and curr_time 
      properties. If the trace_on property is True it will also print the 
      values of these properties to standard output after it has updated them.
      If the model cannot be advanced because curr_time >= max_time
      then it will return False, otherwise it will return True.
      """
      if self.curr_time >= self.__time_params.max_time:
         return False      

      self.__predators, self.__prey = get_new_predators_and_prey(
                            self.predators, 
                            self.prey, 
                            self.__time_params.dt, 
                            self.__coeffs)     
      self.__curr_time += self.__time_params.dt

      self.__trace()
      return True

   
   def run(self):
      """
      Advances the model until the value of the curr_time property is >= 
      the value of the max_time property. It returns the results of running
      the model in an instance of the LotkaVolterraResults class.
      """
      time_series     = [self.curr_time]
      predator_series = [self.predators]
      prey_series     = [self.prey]
   
      while self.advance():
         time_series.append(self.curr_time)
         predator_series.append(self.predators)
         prey_series.append(self.prey)
         
      results = LotkaVolterraResults(time_series,
                                     predator_series,
                                     prey_series)
      return results


   @property
   def trace_on(self):
      return self.__trace_on

   @trace_on.setter
   def trace_on(self, value):
      self.__trace_on = value

    
   def __trace(self):
      if self.__trace_on:
         print("time={:g}, prey={:g}, predators={:g}".format(
                 self.__curr_time, self.prey, self.predators))

      
        

