import numpy as np
import pandas as pd

wiz_df = pd.DataFrame()

def Wiz_1_stats():
    def Wiz_1_hp():
        Wiz_One_HP = np.random.choice([1,2,3,4], size= 6)
        return Wiz_One_HP.sum()
    def Wiz_1_damage():
        return Wiz_1_hp()
    return Wiz_1_hp(), Wiz_1_damage()

def Wiz_2_stats():
    def Wiz_2_hp():
        Wiz_Two_HP = np.random.choice([1,2,3,4,5,6], size= 4)
        return Wiz_Two_HP.sum()
    def Wiz_2_damage():
        return Wiz_2_hp()
    return Wiz_2_hp(), Wiz_2_damage()

Wiz_1_stats()

Wiz_2_stats()