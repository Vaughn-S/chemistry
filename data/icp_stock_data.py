#Vaughn Smith
#ICP Data

import pandas as pd

def main():
    #Data: Pb; freq= 217.000
    data_Pb1 ={
        'Concentration (mmol)':[ 0, 0.7813, 1.56, 3.125, 6.26, 12.7, 25.1, 50.1],
        'Intensity':[1017.3, 4790.9, 9364.7, 19303.1, 38022.3, 76297.5, 153850.8, 305609.1]
    }
    
    df_Pb1 = pd.DataFrame(data_Pb1)
    x_Pb1= df_Pb1['Concentration (mmol)']
    y_Pb1= df_Pb1['Intensity']
    corr_Pb1 = x_Pb1.corr(y_Pb1)

    
    #Data: Pb; freq= 220.353
    data_Pb2 ={
        'Concentration (mmol)':[ 0, 0.7813, 1.56, 3.125, 6.26, 12.7, 25.1, 50.1],
        'Intensity':[3717.3, 17205.2, 33724.3, 70269.7, 136767.5, 273985, 550896.1, 1100129.2]
    }

    df_Pb2 = pd.DataFrame(data_Pb2)
    x_Pb2= df_Pb2['Concentration (mmol)']
    y_Pb2= df_Pb2['Intensity']
    corr_Pb2 = x_Pb2.corr(y_Pb2)


    #Data: As; freq= 193.696
    data_As1 ={
        'Concentration (mmol)':[0, 0.7813, 1.563, 3.125, 6.25, 12.6, 25, 50],
        'Intensity':[144.7, 3184, 6498.3, 13318.7, 27376.7, 55929.7, 113345.1, 225672.5]
    }
    
    df_As1 = pd.DataFrame(data_As1)
    x_As1= df_As1['Concentration (mmol)']
    y_As1= df_As1['Intensity']
    corr_As1 = x_As1.corr(y_As1)


    #Data: As; freq= 228.812
    data_As2 ={
        'Concentration (mmol)':[0, 0.7813, 1.563, 3.125, 6.25, 12.6, 25, 50],
        'Intensity':[2629.5, 7771.4, 15682.4, 31876, 65098.8, 133752.8, 272747.9, 549884.1]
    }
    
    df_As2 = pd.DataFrame(data_As2)
    x_As2= df_As2['Concentration (mmol)']
    y_As2= df_As2['Intensity']
    corr_As2 = x_As2.corr(y_As2)