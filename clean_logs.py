import csv

#1 function
def celsius_converter(f_temp):
    celsius = round((float(f_temp) - 32) / 1.8, 2)
    return celsius

#2 function
def parse_and_clean(line):
    parts = [part.strip() for part in line.split("|")]
    if any(part == "" or part.upper() == "N/A" or part.upper() =="ERROR" for part in parts):  #upper makes it case insensitive
        return None

    if len(parts) != 5:
        return None
    
    sensor_status = parts[-1]

    if sensor_status != "ACTIVE":
        return None

    return parts


#3dalis

corrupted_lines = 0
input_file = "environmental_raw.txt"
output_file = "environmental_clean.csv"
with open(input_file, "r") as inputfile, open(output_file, "w") as outputfile:

    writer = csv.writer(outputfile)
    
    for line in inputfile:
        clean_line = parse_and_clean(line)
        if clean_line is None:
            corrupted_lines += 1
            continue

        clean_line[2] = celsius_converter(float(clean_line[2]))
        writer.writerow(clean_line)

print (f"There were {corrupted_lines} corrupted lines.")
    