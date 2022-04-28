import pandas as pd

# index_col：使用何列作为index
# usecols: 导入那几列数据，输入为数组
# skiprows，skipfooter，跳过开头和最后几行
# na_filter：代表将空格代替为n.a,和后续dropna函数联动

# index与column分别代表行、列索引。

# print(data.index)
# print(data.columns)
data = pd.read_excel('bp-stats-review-2021-all-data.xlsx', sheet_name=1, index_col=0, usecols=list(range(57)),
                     skiprows=2,
                     skipfooter=10, na_filter=True)
data = data.dropna(axis=0, how='all')
data.index = data.index.str.strip()

# axis：默认为 0，表示逢空值剔除整行，如果设置参数 axis＝1 表示逢空值去掉整列。
# how：默认为 'any' 如果一行（或一列）里任何一个数据有出现 NA 就去掉整行，如果设置 how='all' 一行（或列）都是 NA 才去掉这整行。
# thresh：设置需要多少非空值的数据才可以保留下来的。
# subset：设置想要检查的列。如果是多个列，可以使用列名的 list 作为参数。
# inplace：如果设置 True，将计算得到的值直接覆盖之前的值并返回 None，修改的是源数据。


# print(data)


class Primary_Energy_Consumption:

    def get_data(self, country_list, start_year=1965, end_year=2020):
        return data.loc[country_list, start_year:end_year].round(2)

    def get_region_list(self):
        return list(data.index)

    def get_years(self):
        return list(data.columns)

    def get_year_data(self,year):
        return list(data.loc[:,year].round(2))

    def get_year_top10(self,year):
        not_country = ['Total World', 'of which: OECD', 'Non-OECD', 'Total North America', 'Total Asia Pacific',
                       'Total Europe', 'Total Middle East', 'European Union #', 'Total Africa', 'Total CIS',
                       'Total S. & Cent. America']
        data_2 = data.drop(axis=0,index=not_country)
        top_10 = data_2.loc[:,year].nlargest(10)
        return top_10.round(2)



# For functional test
# a = Primary_Energy_Consumption()
# print(a.get_data(['China', 'Canada'],2001,2003))
# # print(a.get_region_list())
# # print(a.get_years())
# print(a.get_year_top10(2020))
