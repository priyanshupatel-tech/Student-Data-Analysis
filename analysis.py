import pandas as pd
import numpy as np

def read_csv():
    df=pd.read_csv("Pandas/student.csv")
    return df

def menu():
    print("="*35,"Menu","="*35)
    print("1.Understand Data Frame\n2.Cleaned Data\n3.Report Card of Data Frame\n4.Exit")

def understand_df(df):
    print("----------------------- Data Set's Five Rows -----------------------")
    print(df.head())
    print("----------------------- Data Set's Shape ---------------------------")
    print(df.shape)
    print("----------------------- Data Set's All Info ------------------------")
    df.info()
    print("----------------------- Data Set Describe -------------------------")
    print(df.describe())

def clean_data(df):
    print("----------------------- Null Row's Number ----------------------------")
    print(df.isnull().sum())
    df=df.fillna(90)
    df=df.drop_duplicates() 
    return df

def add_feature(df):
    df["Status"]=np.where(df["Marks"]>50 ,"Pass","Fail")
    df["Grades"]=np.where(df["Marks"]>90,"A",
                 np.where(df["Marks"]>75,"B",
                 np.where(df["Marks"]>50,"C","Fail")))
    return df

def analyze_data(df):
    # print("Average Marks of Each City")
    average= df.groupby("City")["Marks"].mean()
    # print("Maximum Marks of Student")
    max_marks= df.groupby("City")["Marks"].max()
    # print("Total Student In Each City")
    total= df.groupby("City")["Marks"].count()
    return average,max_marks,total

def generate_report(df):
    print("\n\n========================== Report of Student ===============================")
    print("-------------------------- Top 5 Student ----------------------------------")
    print(df.nlargest(5,["Marks"]))
    print("-------------------------- Fail Student ------------------------------------")
    print(df[df["Marks"]<50])
    average,max_marks,total=analyze_data(df)
    print("------------------------ Average Marks of Each City -------------------------\n",average)
    print("------------------------- Topper Student of Each City ----------------------\n",max_marks)
    print("------------------------- Total Student of Each City -----------------------\n",total)

#Function Calling
while True:
    menu()
    df=read_csv()
    choice=int(input("Enter you Choice="))
    if choice==1:    
        understand_df(df)
    elif choice==2:
        df=clean_data(df)
    elif choice==3:
        generate_report(df)
    elif choice==4:
        print("Thanks you ")
        exit()
    else:
        print("Please Give Correct Input Number!")
