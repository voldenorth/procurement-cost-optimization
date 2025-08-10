import pandas as pd

df=pd.read_csv('spend_analysis_dataset.csv')

df['PurchaseDate']=pd.to_datetime(df['PurchaseDate'])
df.to_csv('cleansing folder/spend_main_analysis.csv',index=False)


most_buyer=df.groupby('Buyer')['TotalCost'].sum().reset_index()
most_buyer=most_buyer.sort_values(by='TotalCost',ascending=False).reset_index(drop=True)
most_buyer.to_csv('cleansing folder/buyer.csv',index=False)

best_product = df.groupby('ItemName').agg({'Quantity': 'sum', 'TotalCost': 'sum'}).reset_index()
best_product=best_product.sort_values(by='Quantity',ascending=False).reset_index(drop=True)
best_product.to_csv('cleansing folder/best_product.csv',index=False)




best_category=df.groupby('Category').agg({'Quantity':'sum','TotalCost':'sum'}).reset_index()
best_category=best_category.sort_values(by='TotalCost',ascending=False).reset_index(drop=True)
best_category.to_csv('cleansing folder/category.csv',index=False)

most_expensive_product=df.groupby('ItemName')['UnitPrice'].max().reset_index()
most_expensive_product=most_expensive_product.sort_values(by='UnitPrice',ascending=False).reset_index(drop=True)
most_expensive_product.to_csv('cleansing folder/expensive_product.csv',index=False)

favorite_product=df.groupby('Buyer')['ItemName'].value_counts().reset_index()
favorite_product=favorite_product[favorite_product['count']>=4].reset_index(drop=True)
favorite_product.to_csv('cleansing folder/favorite_product.csv',index=False)

supllier_by_quantity=df.groupby(['Supplier','ItemName']).agg({'Quantity':'sum','TotalCost':'sum'}).reset_index()
supllier_by_quantity.to_csv('cleansing folder/supplier.csv',index=False)

