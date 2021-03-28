import time
import random 
import visualizer
from abc import ABCMeta, abstractmethod

class Algorithim(metaclass=ABCMeta):
  def __init__(self, name):
    # Random array of 512s
    self.array = random.sample(range(512), 512)
    self.name = name # name of algo

    def update_display(self, swap1=None, swap2=None):
      visualizer.update(self, swap1, swap2)

    
    def run_algo(self):
      self.start_timer = time.time()
      self.algorithm()
      time_Elapsed = time.time - self.start_time
      return self.array, time_Elapsed

    
    @abstractmethod()
    def algorithm(self):
      raise TypeError(f"Algorithim.algorithm() has not been overwritten")

# Merge sort algorithim, Each algorithim should subclass from algorithim class (name, array and update display)
class MergeSort(Algorithim):
  def __init__(self):
    super().__init__("MergeSort")

  
  def algorithm(self, array=[]):
    if array == []:
      array = self.array
    if len(array) < 2:
      return array
    mid = len(array) / 2
    left = self.algorithm(array[:mid])
    right = self.algorithm(array[mid:])
    return self.merge(left, right)

  def merge(self, left, right):
    result = []
    i, j = 0,0

    while i < len (left) and j < len(right):
      if left[i] < right[i]:
        result.append(left[i])
        i +=1
      else:
        result.append(right[j])
        j +=  1
      self.update_display()
    result += left[i:]
    result += right[j:]
    self.array = result 
    self.update_display()
    return result 

