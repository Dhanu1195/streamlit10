import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from tqdm import tqdm

from happytransformer import HappyTextClassification

tqdm.pandas()

def reviewFilter(dfe):
    df=pd.read_csv(dfe)
    df.head()

    df.dropna(subset=['Text'],inplace=True)

    happy_tc=HappyTextClassification(model_type='DISTILLBERT',model_name='distilbert-base-uncased-finetuned-sst-2-english',num_labels=2)

    df['text_sentiment']=df['Text'].progress_map(lambda x:happy_tc.classify_text(x).label)

    df_filtered=df[(df['text_sentiment']=='POSITIVE') & (df['Star']<=2)]

    sns.countplot(df['Star'],hue=df['text_sentiment'])

    sns.countplot(df_filtered['Star'],hue=df_filtered['text_sentiment'])

    return df_filtered

