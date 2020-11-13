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

class LotkaVolterraResults:
   def __init__(self, 
                time_series,
                predator_series,
                prey_series
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

