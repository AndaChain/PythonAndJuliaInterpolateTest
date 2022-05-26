import julia
import csv

from GUI_in import*

def DIY(start,stop,step):
    j = julia.Julia()
    x = j.include("InterpolateDIY.jl")

    from julia import Main
    x = Main.main(start,stop,step)
    #getcsv()
    

#def getcsv():
    mycsv = csv.reader(open('time_DIY.csv'))
    text = []
    for row in mycsv:
        text.append(row)
    result = text[1]
    print(result)
    return result


if __name__ == "__main__":
    DIY(1,10,100)
    #getcsv()
