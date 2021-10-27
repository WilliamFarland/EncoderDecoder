# EncoderDecoder

Program takes a directory of files and randomizes their names for grading.
This ensures grading confidentiality between the TA and the students.

To use the program run the Encoder_Decoder.py file and select your mode of operation.
There are four modes:
Mode 1: Checks if a user submitted multiple files. This generateres an excel file with usernames so that duplicate values can be checked.
Mode 2: This encodes the file names for grading. After this is run a Keys.csv file is created that stores the original username and the randomized name for conversion when decoding.
  (After this is run you can send the files to the grader)
Mode 3: This decodes the names. It uses the Keys.csv file to reverse lookup the randomized name.
