import pandas as pd
cols= list(range(57))
data = pd.read_excel('bp-stats-review-2021-all-data.xlsx',sheet_name=1,index_col=0,usecols=cols,skiprows=2,skipfooter=10,na_filter=False)
print(data)


class Primary_Energy_Comsuption:
    def get_data(self,country_list,start_year,end_year):
            return data.loc[country_list,start_year:end_year]




a =Primary_Energy_Comsuption()
print(a.get_data(['China','Canada'],2001,2002))
