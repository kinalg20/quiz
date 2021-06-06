import pandas as pd
import numpy as np

movie_Data=pd.read_csv("movies.csv")
movie_Data=movie_Data.iloc[:,0:2]
movie_df=pd.DataFrame(movie_Data)
movie_df

rating_Data=pd.read_csv("ratings.csv")
rating_Data=rating_Data.iloc[:,0:3]
rating_df=pd.DataFrame(rating_Data)
rating_df

merged_data=movie_Data.merge(rating_Data,on='movieId')
merged_data

merged_data = merged_data.fillna("", inplace=False)
merged_data=pd.DataFrame(merged_data)
merged_data

def main_Data(merged_data,thr,no):
  df1=merged_data.groupby("title").rating.mean()
  df2=pd.DataFrame(df1)
  df2["no"]=merged_data.groupby("title").rating.count()
  df_max=df2["no"].max()
  df2["rating"]+=(df2["no"]/df_max)-0.5
  df2=df2[df2["no"]>thr]
  return df2.sort_values(["rating"],ascending=[0]).head(no)
  df4=pd.DataFrame(df3)
data=main_Data(merged_data,80,10)
data

data

movie_matrix=merged_data.pivot_table(index='userId',columns='title',values='rating')
movie_matrix= movie_matrix.fillna(0)
movie_matrix

matrix.shape

def movie_Search(movie_matrix,movie_n,thr,no):
  movie_data=movie_matrix.columns 
  for i in range(len(movie_data)):
    if movie_data[i]==movie_n:
      movie_rating=movie_matrix[movie_n]
      movie_search_rating=movie_matrix.corrwith(movie_rating)
      msdf=pd.DataFrame(movie_search_rating, columns=['correlation'])
      msdf.dropna(inplace=True)
      df2=merged_data.groupby("title").rating.count()
      df2=pd.DataFrame(df2)
      main_d=df2.merge(msdf,on="title")
      main_d=main_d[main_d['rating'] > thr]
      output=main_d.sort_values(by="correlation",ascending=False).head(no)
      return output
  else:
    return 0
import string
movie_name=input("enter movie name")
movie_n=movie_name.capitalize()
m=movie_Search(movie_matrix,movie_n,40,10)
value=isinstance(m,int)
if(value):
  array=[]
  movie_data=movie_matrix.columns
  for i in range(0,len(movie_data)):
    if (movie_data[i].find(movie_n) != -1):
      array.append(movie_data[i])
  else:
    if len(array)>0:
      for i in range(0,len(array)):
        print(array[i])
      else:
        import random
        movie_name=random.choice(array)
        answer=movie_Search(movie_matrix,movie_name,40,10)
        print(answer)
    else:
      print("Main to nhi chlunga re baba")
else:
  print(m)

