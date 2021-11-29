import csv
import numpy as np
import pandas as pd
#fonction qui convertit un csv en tableau de données et qui renvoie le tableau de données sans module numpy
def csv_to_array(file_name):
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        data = []
        for row in csv_reader:
            data.append(row)
    return data


#Afficher le contenu d'un tableau de données
def print_array(data):
    for row in data:
        print(row)

#fonction qui retourne la quatrième colonne d'un tableau de données
def get_column(data, column_number):
    column = []
    for row in data:
        column.append(row[column_number])
    return column

distribution = [0,0]
#distribution statistique de la colonne 1 par rapport à la colonne 4
def distribution_stat(data, column_number):
    column = get_column(data, column_number)
    column_4 = get_column(data, 4)
    unique_values = get_unique_values(data, column_number)

    for i in range(len(unique_values)):
        distribution.append([unique_values[i], 0])
    for i in range(len(column)):
        for j in range(len(distribution)):
            if column[i] == distribution[j][0]:
                distribution[j][1] += 1
    return distribution

# on récupère les différenter valeur de la colonne 1
def get_unique_values(data, column_number):
    column = get_column(data, column_number)
    unique_values = []
    for i in range(len(column)):
        if column[i] not in unique_values:
            unique_values.append(column[i])
    return unique_values

#On socke dans un tableau a 2 dimensions les valeurs de la colonne 4 par rapport à la colonne 1


#On sotck les données dans un tableau de données
data = csv_to_array('LondonAir_Ozone.csv')

#On affiche le nombre de lignes du tableau de données
#print(len(data))

# on remplace les valeurs manquantes par un ?
for row in data:
    for i in range(len(row)):
        if row[i] == '':
            row[i] = '?'

#On affiche la premiers lignes du tableau de données
print_array(data[:10])

#On affiche les 100 premiers valeurs contenu du tableau de données
#print(print_array(data[:100]))


#On affiche la quatrième colonne du tableau de données
#print(get_column(data, 3))

valeurs_colonne_1 = get_unique_values(data, 0)
print(valeurs_colonne_1)

print_array(distribution_stat(data, 3))

#tableau de distribtion pour chaque lieu
lieu_1 = [0]
lieu_2 = [0]
lieu_3 = [0]
lieu_4 = [0]
lieu_5 = [0]


# on stocke la distribution statistique de la colonne 1 par rapport à la colonne 4 dans le  tableau correspondant
n=0
for row in data:
    n=n+1
    if 'BT4'== data[0:n]:
        lieu_1.append(data[3][n])

    if 'BX1'== data[0:n]:
        lieu_2.append(data[3][n])
    
    if 'BQ7'== data[0:n]:
        lieu_3.append(data[3][n])
    
    if 'GR8'== data[0:n]:
        lieu_4.append(data[3][n])

    if 'MY1'== data[0:n]:
        lieu_5.append(data[3][n])
    

# on va supprimer les valeurs ne fesant pas partie du premiers et second quartile
 # pour le prmiers tableau:
q1 =  np.percentile(lieu_1, 25) # premier quartile
q2 = np.percentile(lieu_1, 75) # troisième quartile
i=0
