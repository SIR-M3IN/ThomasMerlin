import matplotlib.pyplot as plt
import csv
import PySimpleGUI as sg

def mutter():
    f = open("geburten_nach_Jahr_Mutter_Stand.csv")
    csvFile = csv.reader(f, delimiter=';', quotechar='|')


    dictionary = {}

    for lines in list(csvFile)[1:]:
        if dictionary.get(lines[0]):
            dictionary[lines[0]] += 1
        else:
            dictionary[lines[0]] = 1

    plt.ylabel("Geburten")
    plt.xlabel("Jahre der Geburten")
    plt.plot(dictionary.keys(),dictionary.values(),label = "Geburten") # x achsen beschriftung und werte dazu
    plt.xticks(rotation=45, ha='right')
    plt.legend()
    plt.show()

def alter_Mutter(matrix):
    alterinjahr = []
    temlist = []
    jahr = matrix[1][0]
    for x in matrix:
        if x[5] != 'Alter der Mutter':
            newjahr = x[0]
            if jahr != newjahr:
                alterinjahr.append(round(sum(temlist)/len(temlist),2))
                temlist = []
            temlist.append(int(x[5]))
            jahr = x[0]
    von = int(matrix[1][0])
    bis = int(matrix[-1][0])
    jahre = []
    for i in range(von,bis):
        jahre.append(i)
    plt.plot(jahre,alterinjahr,label = "Alter Mutter")
    plt.legend()
    plt.show()

def alter_Vater(matrix):
    alterinjahr = []
    temlist = []
    jahr = matrix[1][0]
    for x in matrix:
        if x[6] != 'Alter des Vaters':
            newjahr = x[0]
            if jahr != newjahr:
                alterinjahr.append(round(sum(temlist)/len(temlist),2))
                temlist = []
            if int(x[6]) != 999:
                temlist.append(int(x[6]))
            jahr = x[0]
    von = int(matrix[1][0])
    bis = int(matrix[-1][0])
    jahre = []
    for i in range(von,bis):
        jahre.append(i)
    plt.plot(jahre,alterinjahr,label = "Alter Vater")
    plt.legend()
    plt.show()

def familien_stand(matrix):
    countge = 0
    countver = 0
    countledig = 0
    geschieden = []
    verhei = []
    ledig = []
    jahr = matrix[1][0]
    for x in matrix:
        if x[3] != 'Familienstand':
            newjahr = x[0]
            if jahr != newjahr:
                geschieden.append(countge)
                verhei.append(countver)
                ledig.append(countledig)
                countge = 0
                countledig = 0
                countver = 0
            if x[3] == 'geschieden':
                countge += 1
            if x[3] == 'ledig':
                countledig += 1
            if x[3] == 'verheiratet':
                countver += 1
            jahr = x[0]
        
    von = int(matrix[1][0])
    bis = int(matrix[-1][0])
    jahre = []
    for i in range(von,bis):
        jahre.append(i)
    del geschieden[0]
    del verhei[0]
    del ledig[0]
    del geschieden[0]
    del verhei[0]
    del ledig[0]
    plt.plot(jahre,verhei,label = "Verheiratet")
    plt.plot(jahre,ledig,label = "Ledig")
    plt.plot(jahre,geschieden,label = "Geschieden")
    plt.legend()
    plt.show()
def geschlecht(matrix):
    jahr = matrix[1][0]
    jahre = []
    maennlich = []
    weiblich = []
    tempm = 0
    tempw = 0
    for x in matrix:
        if x[1] != 'Geschlecht':
            newjahr = x[0]
            if jahr == newjahr:
               if x[1] == "mÃ¤nnlich":
                   tempm +=1
               elif x[1] == "weiblich":
                   tempw += 1
            else:
                maennlich.append(tempm)
                weiblich.append(tempw)
                tempm = 0
                tempw = 0
            jahr = x[0]
    von = int(matrix[1][0])
    bis = int(matrix[-1][0])
    for i in range(von,bis):
        jahre.append(i)
    plt.plot(jahre, maennlich,label = "maennlich")
    plt.plot(jahre, weiblich,label = "weiblich")
    plt.legend()
    plt.show()
def matrixx():
    matrix = []
    f = open("geburten_nach_Jahr_Mutter_Stand.csv")
    csvFile = csv.reader(f, delimiter=';', quotechar='|')
    for y in csvFile:
        line = []
        for x in y:
            line.append(x)
        matrix.append(line)
    return matrix
def main():
    matrix = matrixx()
    layout = [[sg.Button('Geburten'), sg.Button('Geschlecht'), sg.Button('Familienstand'), sg.Button('AlterMutter'), sg.Button('AlterVater')]]
    window = sg.Window('Geburtenrate', layout)
    while True:

        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        
        if event == 'AlterMutter':
            alter_Mutter(matrix)
        elif event == 'AlterVater':
            alter_Vater(matrix)
        elif event == 'Geburten':
            mutter()
        elif event == 'Familienstand':
            familien_stand(matrix)
        elif event == 'Geschlecht':
            geschlecht(matrix)

 
        plt.close()
    window.close()

main()
