from unittest import result
import julia
import csv

from GUI_in import*

def Julia(start,stop,step):
    j = julia.Julia()
    x = j.include("Interpolate.jl")

    from julia import Main
    x = Main.main(start,stop,step)
    #getcsv()
    

#def getcsv():
    mycsv = csv.reader(open('time_response.csv'))
    text = []
    for row in mycsv:
        text.append(row)
    result = text[1]
    print(result)
    return result


if __name__ == "__main__":
    Julia(0,10,50000)
    #getcsv()
