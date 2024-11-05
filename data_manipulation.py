import pandas as pd
data = {
    'rocket': [
        'Falcon 1',
        'Flacon 9',
        'Falcon Heavy'
    ],
    'launches': [5,100,3]
}

df = pd.DataFrame(data)

print(df)

print(df['rocket'])

falcon_df = df[df['rocket'] == 'Falcon 9']

df['success_rate'] = [0.4,0.98,1.0]

print(df[df['launches'] > 5])