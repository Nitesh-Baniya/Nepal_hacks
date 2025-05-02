import pandas as pd

answer = pd.read_excel("./data/dummyKL/(Answer Library Entry) Danfe Corp KL.xlsx")
canonical = pd.read_excel("/data/dummyKL/(Canonical Questions Products) Danfe Corp KL.xlsx")
product = pd.read_excel("/data/dummyKL/(Product) Danfe Corp KL.xlsx")
company = pd.read_excel("./data/dummyKL/(Company) Danfe Corp KL.xlsx")

# Merge 'ans' and 'canonical' on 'id' and 'cqid' 
merged_df = pd.merge(answer, canonical, left_on='id', right_on='cqid', how='inner')

# Merge the result with 'products' on 'product_id'
final_df = pd.merge(merged_df, product, left_on='product_id', right_on='product_id', how='inner')

# Drop the 'product_id' column and keep 'product_name'
final_df = final_df.drop(columns=['product_id'])

# Save the file
final_df.to_excel('./data/answer_library_entry_test.xlsx', index=False)

# print("Merged dataset saved successfully!")