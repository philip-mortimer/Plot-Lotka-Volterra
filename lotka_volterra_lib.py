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


def get_delta_predators(predators, prey, coeffs):
    """
    Returns change in number of predators per unit time.
    """
    return coeffs.predator_growth_rate * predators * prey \
            - coeffs.predator_mortality_rate * predators


def get_delta_prey(predators, prey, coeffs):
    """
    Returns change in number of prey per unit time.
    """
    return coeffs.prey_growth_rate * prey \
            - coeffs.predation_rate * predators * prey


def get_new_predators_and_prey(predators, prey, dt, coeffs):
    """
    predators: current number of predators

    prey:      current number of prey

    dt:        time interval over which change in number of 
                predators and prey takes place

    coeffs:    instance of LotkaVolterraCoefficients class
                containing coeffiecients such as prey growth
                rate

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
