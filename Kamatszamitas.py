import numpy as np
import matplotlib.pyplot as plt

#A lista minden elemét egyel növeli
def add_one(a):
    for i in range(len(a)):
        a[i]+=1
    return a

#A havi kamatlábat ismerve kiszámítja az éves NÉVLEGES kamatlábat
def calc_nom_int(month_int):
    nom_int=12*month_int
    return  nom_int

#A havi kamatlábat ismerve kiszámítja az éves EFFEKTÍV kamatlábat
def calc_eff_int(month_int):
    eff_int=round((1+month_int)**12-1,5)
    return  eff_int

#Az éves effektív kamatlábat ismerve kiszámítja az éves LOGARITMIKUS kamatlábat
def calc_log_int(eff_int):
    log_int=round(np.log(1+eff_int),5)
    return  log_int

#Diszkontálási faktorokat számít definiált időtartamra EFFEKTÍV kamatlábból
def calc_disc_fac(r,year='None'):

    if year!='None':
        coeff_std=add_one(r*year)
        disc_fac=[1]*len(coeff_std)
        for i in range(min(year,len(coeff_std))):
            for x in range(i+1):
                disc_fac[i]=disc_fac[i]/coeff_std[x]
        disc_fac=disc_fac[0:min(year,len(coeff_std))]

    else:
        coeff_chg=add_one(r)
        disc_fac=[1]*len(coeff_chg)
        for i in range(len(coeff_chg)):
            for x in range(i+1):
                disc_fac[i]=disc_fac[i]/coeff_chg[x]

    return disc_fac

#Nettó jelenértéket számol teljes projektre vonatkozan cashflowból és diszkontálási rátából
def calc_npv_project(CashFlow, disc_fac, year, plotBar=False):

    NPV=[0]*min(len(CashFlow), len(disc_fac), year)

    for i in range(min(len(CashFlow), len(disc_fac), year)):
        sand_box=[0]*(i+1)

        for j in range(i+1):
            sand_box[j]=CashFlow[j]*disc_fac[j]

        NPV[i]=sum(sand_box)

    if plotBar==True:
        ind = np.arange(1, year+1, 1)
        fig = plt.figure(figsize = (10, 5))
        p1=plt.bar(ind, NPV, color ='maroon', width = 0.5)
        plt.title('Net Present Value of the Investment')
        plt.xlabel('Year')
        plt.ylabel('Net Present Value')
        plt.xticks(np.arange(1, year+1, 1))
        plt.show()

    return NPV

#Nettó jelenértéket számol egyes évekre vonatkozóan cashflowból és diszkontálási rátából
def calc_npv_year(CashFlow, disc_fac):

    NPV=[0]*min(len(CashFlow), len(disc_fac))

    for i in range(min(len(CashFlow), len(disc_fac))):
        NPV[i]=CashFlow[i]*disc_fac[i]
    return NPV

#Egyenletesen növekvő örökjáradék nettó jelenértékét számítja járadék, növekedési ráta és kamatláb alapján
def calc_perp_ann(C, r, g):

    if r>g:
     NPV_perp_ann=C*1/(r-g)
    else:
     print('Expression is not convergent')
    return NPV_perp_ann

#n évig tart annuitás nettó jelenértékének számítása
def calc_ann(C, r, n):

    NPV_ann=C*(1/r-1/(r*((1+r)**n)))

    return NPV_ann



