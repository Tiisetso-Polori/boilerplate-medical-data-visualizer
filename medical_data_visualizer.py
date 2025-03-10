import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1 Import Data
df = pd.read_csv('medical_examination.csv')

# 2 Add 'overweight' column
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# 3 Normalize data
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)



# 4  Draw the Categorical Plot in the draw_cat_plot function.
def draw_cat_plot():
    # 5 Create a DataFrame for the cat plot using pd.melt 
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6 Group and reformat the data
    # 7 Convert the data into long format
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index()
    df_cat = df_cat.rename(columns={0: 'total'})

    # 8 Get the figure for the output and store it in the fig variable.
    fig = sns.catplot(data=df_cat, x='variable', y='total', hue='value', col='cardio', kind='bar').fig


    # 9 Do not modify the next two lines.
    fig.savefig('catplot.png')
    return fig


# 10 Draw the Heat Map in the draw_heat_map function.
def draw_heat_map():
    # 11 Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                    (df['height'] >= df['height'].quantile(0.025)) &
                    (df['height'] <= df['height'].quantile(0.975)) &
                    (df['weight'] >= df['weight'].quantile(0.025)) &
                    (df['weight'] <= df['weight'].quantile(0.975))]

    # 12 Calculate the correlation
    corr = df_heat.corr()

    # 13  Generate a mask for the upper triangle and store it in the mask variable.
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14 Set up the matplotlib figure.
    fig, ax = plt.subplots(figsize=(12, 12))

    # 15 Plot the correlation matrix
    ax = sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', square=True, vmin=0, vmax=0.25, cbar_kws={'shrink': .45})



    # 16 Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
