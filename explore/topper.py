import pandas as pd

data = {
    'Name' : ['Alice','Bob','Charlie','David','Eva'],
    'Score': [95,92,85,95,90]
}
df = pd.DataFrame(data)
#top_toppers = df.nlargest(3,'Score')
#print(top_toppers)
highest_score = df['Score'].max()
toppers = df[df['Score']==highest_score]
print(toppers)