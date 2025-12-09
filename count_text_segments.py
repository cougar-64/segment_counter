import os
import csv
import sys
from pathlib import Path


# this function counts the files in the bonus folder to know if count should be added to finished_segments or not
def file_counter(bonus):
   count = 0
   if (bonus.is_dir()):
      for _ in bonus.iterdir():
         count +=1
      if count == 5:
         return True

   return False


# this function counts the amount of segments in a file
def count_segments(target):
   count = 0
   if (target.is_dir()):
      for file in target.iterdir():
         if '.srt' in file.name:
            with open(file, 'r') as f:
               for line in f:
                  line = line.strip()
                  if line.isdigit():
                     count +=1
            # print(count)
   return count


def main():
   # folder_path = Path(sys.argv[1])
   folder_path = Path("/Users/samuelbird/OneDrive - Brigham Young University/Coulson Rich's files - church_asl_annotations")
   # folder_path = Path("/Users/samuelbird/Desktop/MATRIX LAB/ASL_aligned_data/for_testing")
   target_folder = "open_these_videos_and_subtitles_in_elan"
   bonus_folder = "save_subtitles_here_when_finished"
   total_segments = 0
   finished_segments = 0
   counter = 0
   
   for folder in folder_path.iterdir(): # goes into 001_group
      counter +=1
      print(counter)
      target_folder_path = folder_path / folder / target_folder
      bonus_folder_path = folder_path / folder / bonus_folder
      if file_counter(bonus_folder_path):
         finished_segments += count_segments(bonus_folder_path)
         total_segments += count_segments(bonus_folder_path)
      else:
         total_segments += count_segments(target_folder_path)
   
   print("Finished segments annotated: " + str(finished_segments))
   print("Total segments in dataset: " + str(total_segments))




if __name__ == "__main__":
   main()