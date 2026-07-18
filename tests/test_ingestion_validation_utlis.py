from utlis.ingestion_validation_utlis import IngestionValidationUtlis
import pandas as pd

data1 = {
    "order_id": [1, 2, 3],
    'customer_id': [101, 102, 103],
    'product_id': [1001, 1002, 1003],   
    'quantity': [2, 1, 4],
    'unit_price': [10.5, 20.0, 15.0],
    'order_date': ['2023-01-01', '2023-01-02', '2023-01-03'],
    'country': ['USA', 'Canada', 'UK'], 
    'store_id': [1, 2, 3],
    'payment_method': ['Credit Card', 'PayPal', 'Debit Card']
    }

data2 = {
    "order_id": [1, 2, 3],
    'customer_id': [101, 102, 103],
    'product_id': [1001, 1002, 1003],   
    'unit_price': [10.5, 20.0, 15.0],
    'order_date': ['2023-01-01', '2023-01-02', '2023-01-03'],
    'country': ['USA', 'Canada', 'UK'], 
    'store_id': [1, 2, 3],
    'payment_method': ['Credit Card', 'PayPal', 'Debit Card'],
    'test_column': ['test1', 'test2', 'test3']
    }

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)


validator = IngestionValidationUtlis()

result_for_df1 = validator.validate_schema(df1)
print(f"Schema validation result for df1: {result_for_df1}")

result_for_df2 = validator.validate_schema(df2)
print(f"Schema validation result for df2: {result_for_df2}")