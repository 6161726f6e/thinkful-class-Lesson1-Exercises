from collections import defaultdict

population_dict_2010 = defaultdict(int)
population_dict_2100 = defaultdict(int)
population_density_dict_2010 = defaultdict(int)

# Open Data file and process
with open('lecz-urban-rural-population-land-area-estimates_continent-90m.csv', 'rU') as inputFile:
    header = next(inputFile)
    header = header.rstrip().split(',')
    # print(header)
    for line in inputFile:
        line = line.rstrip().split(',')
        line[5] = int(line[5])
        line[6] = int(line[6])
        line[7] = int(line[7])
        if line[1] == 'Total National Population':
            population_dict_2010[line[0]] += line[5]
            population_dict_2100[line[0]] += line[6]
            population_density_dict_2010[line[0]] += line[7]
            # print("%s %s %s" % (line[0], line[5], line[6]))
    # print('**** DEBUG **** 2010', population_dict_2010.items(), "******\n")
    # print('**** DEBUG **** 2100', population_dict_2100.items(), "******\n")

# now write population data to file
with open('national_population.csv', 'w') as outputFile:
    outputFile.write('continent,2010_population, 2010_population_density\n')
    for k, v in population_dict_2010.items():
        population_density = int(population_dict_2010[k]) / int(population_density_dict_2010[k])
        outputFile.write(k + ',' + str(v) + ',' + str(population_density) + '\n')
    outputFile.write('continent,2100_population\n')
    for k, v in population_dict_2100.items():
        outputFile.write(k + ',' + str(v) + '\n')

print(' ***** DEBUG ***** ', population_density_dict_2010.items())

# now calculate and write diffs to file
with open('national_population_diff_2010_to_2100.csv', 'w') as outputFile:
    outputFile.write('continent,population_difference\n')
    for k, v in population_dict_2010.items():
        diff = int(population_dict_2100[k]) - int(population_dict_2010[k])
        percent = diff/int(population_dict_2010[k])
        percent = float(percent)
        outputFile.write(k + ',' + str(diff) + ',' + str(percent) + '\n')
