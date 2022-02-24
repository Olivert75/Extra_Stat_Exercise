import numpy as np
import pandas as pd

#Create stats for wizard 1, 2
def Wiz_stats():
    def Wiz_1_hp():
        Wiz_One_HP = np.random.choice([1,2,3,4], size= 6)
        return Wiz_One_HP.sum()
    def Wiz_1_damage():
        return Wiz_1_hp()
        
    def Wiz_2_hp():
        Wiz_Two_HP = np.random.choice([1,2,3,4,5,6], size= 4)
        return Wiz_Two_HP.sum()
    def Wiz_2_damage():
        return Wiz_2_hp()

    return Wiz_1_hp(), Wiz_1_damage(), Wiz_2_hp(), Wiz_2_damage()

#Assign variables
Wiz_1_HP, Wiz_1_Attack, Wiz_2_HP, Wiz_2_Attack = Wiz_stats()

#Create a dataframe 
wiz_df = pd.DataFrame(Wiz_stats())
wiz_df['wiz_1_hp'] = Wiz_1_HP
wiz_df['wiz_1_att'] = Wiz_1_Attack
wiz_df['wiz_2_hp'] = Wiz_2_HP
wiz_df['wiz_2_att'] = Wiz_2_Attack

wiz_df.wiz_1_hp

#Create simulation battle
wiz_df['wins']= (wiz_df.wiz_1_hp > wiz_df.wiz_2_att) & (wiz_df.wiz_2_hp <= wiz_df.wiz_1_att)
num_wins = wiz_df.wins.mean()

num_wins
