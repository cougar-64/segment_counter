import os
import csv
import sys
from pathlib import Path


# this function counts the files in the bonus folder to know if count should be added to finished_segments or not
def file_counter(bonus):


   return False


# this function counts the amount of segments in a file
def count_segments(target):
   count = 0
   
   
   return count


def main():
   folder_path = Path(sys.argv[1])
   target_folder = "open_these_videos_and_subtitles_in_elan"
   bonus_folder = "save_subtitles_here_when_finished"
   total_segments = 0
   finished_segments = 0

   for folder in folder_path.iterdir(): # goes into 001_group
      target_folder_path = folder_path / folder / target_folder
      bonus_folder_path = folder_path / folder / bonus_folder
      if file_counter(bonus_folder_path):
         finished_segments += count_segments(target_folder_path)
      total_segments += count_segments(target_folder_path)
   
   print("Finished segments annotated: " + finished_segments)
   print("Total segments in dataset: " + total_segments)