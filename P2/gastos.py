import pandas as pd
from pandas.core.indexes.base import ensure_index 
import numpy as np

class Error(Exception):
    pass

class Not12Columns (Error):
    pass

class EmptyColumn(Error):
    pass

def gastos_totales_mes(df, c):
    gastos_totales = 0
    for g in df[c]:
        if(g<0):
            gastos_totales = gastos_totales + g

    return gastos_totales

def ahorros_totales_mes(df, c):
    gastos_totales = 0
    for g in df[c]:
        if(g>0):
            gastos_totales = gastos_totales + g

    return gastos_totales

def num_cols(df):
    col = df.columns
    return len(col)

try:
    df = pd.read_csv('finanzas2020.csv',sep='\t')

    if num_cols(df)!=12:
            raise Not12Columns
    
    gastos = {}
    gastos_totales = 0
    ahorros_totales = 0
    col = df.columns
    for c in col:
        if (df[c].empty):
            raise EmptyColumn
        else:
            df[c] = pd.to_numeric(df[c], errors='coerce').fillna(0)
            print("Gastos de ", c, ": ", sum(df[c]))
            gastos_totales = gastos_totales + gastos_totales_mes(df, c)
            ahorros_totales = ahorros_totales + ahorros_totales_mes(df, c)
            

    print("Los gastos/mes de este año fueron: ", gastos_totales/12, "€/mes")
    print("El gasto total anual fue: ", gastos_totales, "€")
    print("El ahorro total anual fue: ", ahorros_totales, "€")



except IOError as err:
    print("No encuentro el fichero. Error: ", err)

except Not12Columns:
    print("No hay 12 columnas exactas.")
    print()

except EmptyColumn:
    print("Columna vacia.")