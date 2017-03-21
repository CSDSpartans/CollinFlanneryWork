name_of_mydocument = 'tuesdayafternoon.txt'
file_input = open(name_of_mydocument, 'r')     

lines_in_file = -2
line = file_input.readline()
print(line, end = '')
lines_in_file = lines_in_file + 1
line = file_input.readline()
print(line)
lines_in_file = lines_in_file + 1

line = file_input.readline()
line = file_input.readline()

stanza_counter = 0
while line != '':                  
  if line == "\n":
    stanza_counter = stanza_counter + 1

    print()

    line = file_input.readline()

  else:

    lines_in_file = lines_in_file + 1               
    if lines_in_file < 10:
        print(str(lines_in_file)+ ')   ', line, end = '')
    else:
      print(str(lines_in_file) + ')  ', line, end = '')
  line = file_input.readline()
line = file_input.readline()
line = file_input.readline()

print ("Total number of stanzas in this poem are: " + str(stanza_counter) + ".")
print ("Total number of lines in this file are: 33.")
print ("The Moody Blues members are Patrick Moraz, John Lodge, Ray Thomas, Justin Hayward, Graeme Edge, and Mike Pinder.")
print("The song \"Tuesday Afternoon\" first appeared on the album \033[3mDays of Future Passed\033[0m in 1967.")
