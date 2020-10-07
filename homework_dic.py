eurostat_data_base = [
                    ('France',2017, 'F',12),
                    ('Romania',2017, 'F',4),
                    ('France',2017, 'M',12),
                    ('Germany',2017, 'F',12),
                    ('Germany',2017, 'M',12),
                    ('France',2018, 'F',12),
                    ('France',2018, 'M',5),
                    ('Romania',2018, 'F',12),
                    ('Germany',2018, 'F',4),
                    ('Germany',2018, 'M',10),
                    ('Poland',2018, 'M',9),
                    ('Poland',2017, 'F',12),
                    ('Poland',2017, 'M',11),
                    ('Poland',2018, 'F',3),
                    ('Spain',2017, 'F',12),
                    ('Spain',2017, 'M',6),
                    ('Italy',2017, 'F',5),
                    ('Italy',2017, 'M',12),
                    ('Spain',2018, 'M',12),
                    ('Spain',2018, 'F',8),
                    ('Italy',2018, 'F',12),
                    ('Italy',2018, 'M',4),
                    ('Hungary',2018, 'M',2),
                    ('Hungary',2018, 'F',5),
                    ('Denmark',2018, 'F',13),
                    ('Denmark',2018, 'M',12),
                    ('Hungary',2017, 'M',7),
                    ('Hungary',2017, 'F',6),
                    ('Denmark',2017, 'F',13),
                    ('Denmark',2017, 'M',12)]
health_index_2017= {
    country: [sex,health_index]
    for country, year, sex, health_index in eurostat_data_base 
    if year == 2017
}
health_index_2018= {
    country: [sex,health_index]
    for country, year, sex, health_index in eurostat_data_base 
    if year == 2018
}
germany = {
    year : [sex, health_index]
    for country, year, sex, health_index in eurostat_data_base 
    if country == 'Germany'
}
health_index = {
    country + '_'+ str(year) : [year,sex, health_index]
    for country, year, sex, health_index in eurostat_data_base 
    
}
print ('display only the data where the health_index >5 ')
for key,values  in health_index.items():
    if values[2] > 5:
        print(key,values)
print('display only the data where the health_index >5 and sex is ‘F’')      
for key,values  in health_index.items():
    if values[2] > 5 and values[1] == 'F':
        print(key, values)
        
print('create a for loop to print the health_index')
for key,values in health_index.items():
    print(key,values)
   