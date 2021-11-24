import pytest
import gastos
import pandas as pd

def test_columnas():
    data = {'Enero': [-1.0, 19.5, -23.4, 17.1], 'Febrero': [20, 21, 19, 18]}  
    df = pd.DataFrame(data)
    assert gastos.num_cols(df) == 2

def test_gastos_mes():
    data = {'Enero': [-1.0, 19.5, -20.0, 17.1]}  
    df = pd.DataFrame(data)
    assert gastos.gastos_totales_mes(df, 'Enero') == -21.0

def test_gastos_mes_2():
    data = {'Enero': [1.0, 19.5, 20.0, 17.1]}  
    df = pd.DataFrame(data)
    assert gastos.gastos_totales_mes(df, 'Enero') == 0

def test_ahorros_mes():
    data = {'Enero': [-1.0, 15.0, -20.0, 15.0]}  
    df = pd.DataFrame(data)
    assert gastos.ahorros_totales_mes(df, 'Enero') == 30.0

def test_ahorros_mes_2():
    data = {'Enero': [-1.0, -19.5, -20.0, -17.1]}  
    df = pd.DataFrame(data)
    assert gastos.ahorros_totales_mes(df, 'Enero') == 0