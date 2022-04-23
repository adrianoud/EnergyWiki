import pandas as pd
data = pd.read_excel('bp-stats-review-2021-all-data.xlsx',1,index_col=0,skiprows=2)
print(data)


class Primary_Energy_Comsuption:
    def get_data(self,country_list):
            return data.loc[country_list]





a =Primary_Energy_Comsuption()
print(a.get_data(['China']))
