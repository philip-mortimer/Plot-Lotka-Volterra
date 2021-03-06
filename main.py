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

import params as prm
import lotka_volterra_model as lv
from plot_lotka_volterra_results import plot_lotka_volterra_results
    
def main():
    initial_population_densities = lv.InitialPopulationDensities(
        prm.INITIAL_PREDATORS, prm.INITIAL_PREY
    )

    coeffs = lv.Coefficients(
        prm.PREY_GROWTH_RATE, prm.PREDATION_RATE, prm.PREDATOR_GROWTH_RATE,
        prm.PREDATOR_MORTALITY_RATE
    )

    time_params = lv.TimeParams(prm.DT, prm.RUN_TIME)

    population_labels = lv.PopulationLabels(
        prm.PREDATOR_LABEL, prm.PREY_LABEL
    )

    model = lv.Model(
        initial_population_densities, coeffs, time_params, population_labels, 
        prm.TRACE
    )

    results = model.run()
    plot_lotka_volterra_results(results)

if __name__ == '__main__':
    main()
       
   
       
    