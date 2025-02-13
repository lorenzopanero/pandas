#import libraries
import pandas as pd
import numpy as np

# Casual dataframe with 10 rows and 4 columns
data = np.random.randint(1, 100, size=(10, 4)) 
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])

# Function to highlight columns
def highlight_columns(x):
    color = {
        'A': 'background-color: yellow',
        'B': 'background-color: lightgreen',
        'C': 'background-color: lightblue',
        'D': 'background-color: lightcoral'
    }
    return [color.get(col, '') for col in x.index] 

# apply style
color_df = df.style.apply(highlight_columns, axis=0)  

print(color_df)


