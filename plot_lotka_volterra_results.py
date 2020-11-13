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

import matplotlib.pyplot as plt
import params as prm

MAIN_TITLE = 'Lotka-Volterra Model'
LINE_WIDTH = 1
 
def plot_lotka_volterra_results(model_results, 
                                predator_label = prm.PREDATOR_LABEL, 
                                prey_label = prm.PREY_LABEL):
    """
    model_results.time_series:     series of time values to be used as the 
                                   changes over time sub-plot's x-axis values
                                     
    model_results.predator_series: series of predator poplulation densities
        
    model_results.prey_series:     series of prey poplulation densities
        
    predator_label, prey_label:    labels (e.g. 'lions', 'antelope') which 
                                   appear in the legend on the changes over 
                                   time sub-plot, and as part of the axes 
                                   labels in the predators vs. prey sub-plot
                                                                                                        
    Draws 2 sub-plots using the data output by the Lotka-Volterra model. Each
    of the sub-plots is a line plot.
    
    The first sub-plot shows changes in predator and prey population densities
    over time.
    
    The second sub-plot is a phase-space plot which shows predator population 
    densities against prey population densities.
    """
    
    # Lay sub-plots out horizontally.
    figure, (changes, pred_vs_prey) = plt.subplots(1, 2)
    
    figure.canvas.set_window_title(MAIN_TITLE)
    figure.suptitle(MAIN_TITLE)
    
    # Plot changes in predator and prey population densities over time.
    changes.plot(model_results.time_series, model_results.predator_series, 
                    label=predator_label, linewidth=LINE_WIDTH)
             
    changes.plot(model_results.time_series, model_results.prey_series, 
                    label=prey_label, linewidth=LINE_WIDTH)
    
    changes.set_title('Changes over time')
    changes.set_xlabel('Time')
    changes.set_ylabel('Population density')

    changes.legend()
    changes.grid(True)

    # Plot predators vs. prey.
    pred_vs_prey.plot(model_results.prey_series, 
                        model_results.predator_series, linewidth=LINE_WIDTH)

    pred_vs_prey.set_title('Predators vs. prey')
    pred_vs_prey.set_xlabel(prey_label + ' population density')
    pred_vs_prey.set_ylabel(predator_label + ' population density')

    pred_vs_prey.grid(True)
    
    # Increase width of window containing the sub-plots so that they do not
    # look 'squashed' when laid out horizontally.
    width, height = figure.get_size_inches()
    figure.set_size_inches(width*2, height)   

    plt.show()
