import pandas as pd
import numpy as np

class InterestVectorConvertor():
    def __init__(self, df_Category):       
        self.df_Category = df_Category.copy()
        self.df_Category = self.df_Category.drop("label_id",axis=1)

    def convertVector(self, interestVectorPrediction):
        wList_exclude = ["label_id", "category", "category-mod"]
        wVectorColumn = [ x for x in self.df_Category.columns if x not in wList_exclude]
        wdf = self.df_Category.copy()
        wInterestVector = pd.DataFrame(interestVectorPrediction, columns=wVectorColumn)
        for word in wVectorColumn:
            wdf[word] = wdf[word].apply(lambda x : x*wInterestVector[word])
        wdf["category-score"] = wdf.sum(axis=1);
        wdf = wdf[["category-mod","category-score"]]
        wdf = wdf.groupby("category-mod").mean().reset_index()
        wdf = wdf.sort_values("category-score", ascending=False).head(25)
        return wdf
        