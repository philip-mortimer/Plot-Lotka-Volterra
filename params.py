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

# Initial population densities.
INITIAL_PREDATORS = 1
INITIAL_PREY = 3

# Model coefficients.
PREDATION_RATE = 0.2
PREDATOR_GROWTH_RATE = 0.1 # Growth as a result of predation.
PREDATOR_MORTALITY_RATE = 0.2
PREY_GROWTH_RATE = 0.5

# Length of time interval for each iteration of the model.
DT = 0.001

# How long (in model time) the model should run. The model will advance in
# time intervals of DT until the sum of the time intervals >= RUN_TIME.
RUN_TIME = 50

# Labels which appear in the legend on the population densities changes over 
# time sub-plot, and as part of the axes labels in the predators vs. prey
# sub-plot.
PREDATOR_LABEL = 'Predators'
PREY_LABEL = 'Prey'

# If True the program will print current time, prey and predators to standard
# output after each iteration of the model. 
TRACE = False
