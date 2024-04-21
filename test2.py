import pandas as pd
import warnings

# Define a custom function to suppress the warning
def to_dict_tight(df):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return df.to_dict(orient='tight')

# Create a DataFrame with duplicate column names
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
})
df.columns = ['A', 'A']

# Convert DataFrame to dictionary without the warning
result_dict = to_dict_tight(df)

print(result_dict)

