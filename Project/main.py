import pandas as pd

Beijing = pd.read_csv('Random python stuff\\2\\CSVs\\beijing_2022_Olympics_Nations_Medals.csv')
Tokyo = pd.read_csv('Random python stuff\\2\\CSVs\\Tokyo 2020 Olympics Nations Medals.csv')

#get the total number of gold medals won by each country in beijing nad tokyo 
d = {"Country" : ["Gold", "Silver", "Bronze", "Total"]}



for i in range(29):

    Tokyo_gold_count = list(dict(Tokyo.loc[Tokyo["NOC"] == Beijing.loc[i]["NOC"]]["Gold"]).values())
    Tokyo_silver_count = list(dict(Tokyo.loc[Tokyo["NOC"] == Beijing.loc[i]["NOC"]]["Silver"]).values())
    Tokyo_bronze_count = list(dict(Tokyo.loc[Tokyo["NOC"] == Beijing.loc[i]["NOC"]]["Bronze"]).values())
    Tokyo_gold_count = Tokyo_gold_count[0] if Tokyo_gold_count != [] else 0 
    Tokyo_silver_count = Tokyo_silver_count[0] if Tokyo_silver_count != [] else 0 
    Tokyo_bronze_count = Tokyo_bronze_count[0] if Tokyo_bronze_count != [] else 0 

    if Beijing.loc[i]["Gold"] + Tokyo_gold_count != 0:
        d[Beijing.loc[i]["NOC"]] = [Beijing.loc[i]["Gold"] + Tokyo_gold_count
                                       ,Beijing.loc[i]["Silver"] + Tokyo_silver_count
                                       ,Beijing.loc[i]["Bronze"] + Tokyo_bronze_count
,Beijing.loc[i]["Gold"] + Tokyo_gold_count + Beijing.loc[i]["Silver"] + Tokyo_silver_count + Beijing.loc[i]["Bronze"] + Tokyo_bronze_count]
#Total medals

Total = pd.DataFrame(d, index=[1,2,3,4])
print(Total)
#print(Total.loc[[1,2]])
