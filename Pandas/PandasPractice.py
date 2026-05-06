#1.Creating a Series with Custom Index
import pandas as pd 
list=[10,20,30,40,50]
indices=['a','b','c','d','e']
print(pd.Series(list,index=indices))

#2.Creating a DataFrame from a Dictionary
import pandas as pd 
data = {
    "Name": ["Ali", "Ahmed", "Sara", "Ayesha"],
    "Age": [20, 22, 19, 21],
    "Marks": [85, 90, 78, 88]
}
df=(pd.DataFrame(data))
print(df)

#3.Selecting Rows using loc
import pandas as pd 
data = {
    "Name": ["Ali", "Ahmed", "Sara", "Ayesha"],
    "Age": [20, 22, 19, 21],
    "Marks": [85, 90, 78, 88]
}
print(df.loc[0])
print("--------")
print(df.loc[0:1])

#4.Adding a New Column Based on Conditions
import pandas as pd 
data = {
    "Name": ["Ali", "Ahmed", "Sara", "Ayesha"],
    "Age": [20, 22, 19, 21],
    "Marks": [85, 90, 78, 88]
}
df=(pd.DataFrame(data))
print(df)
df["Grade"] = "B"       
df.loc[df["Marks"] >= 85, "Grade"] = "A"
print(df)

#5. Exploring DataFrame Attributes and Data Types 
import pandas as pd 
data = {
    "Name": ["Ali", "Ahmed", "Sara", "Ayesha"],
    "Age": [20, 22, 19, 21],
    "Marks": [85, 90, 78, 88]
}
df=(pd.DataFrame(data))
print(df.shape)
print("--------")
print(df.dtypes)
print("--------")
print(df['Name'])

#6.Filtering Rows Based on a Condition
import pandas as pd 
data = {
    "Name": ["Ali", "Ahmed", "Sara", "Ayesha"],
    "Age": [20, 22, 19, 21],
    "Marks": [85, 90, 78, 88]
}
df=pd.DataFrame(data)
print(df)
print("--------")
filtered_df=df[df["Marks"]>=85]
print(filtered_df)

#7.Filtering Rows with Multiple Conditions
import pandas as pd 
data = {
    "Name": ["Ali", "Ahmed", "Sara", "Ayesha"],
    "Age": [20, 22, 19, 21],
    "Marks": [85, 90, 78, 88]
}
df=pd.DataFrame(data)
print(df)
print("--------")
filtered_df = df[(df["Marks"] >= 85) & (df["Age"] < 22)]
print(filtered_df)

#8.Selecting Specific Rows and Columns
import pandas as pd 
data = {
    "Name": ["Ali", "Ahmed", "Sara", "Ayesha"],
    "Age": [20, 22, 19, 21],
    "Marks": [85, 90, 78, 88]
}
df=pd.DataFrame(data)
print(df)
#Using loc
print(df.loc[0:1,["Name","Marks"]])
#Using iloc 
print(df.iloc[0:2, [0, 2]])
      
#9.Dropping Rows from a DataFrame   
import pandas as pd 
data = {
    "Name": ["Ali", "Ahmed", "Sara", "Ayesha"],
    "Age": [20, 22, 19, 21],
    "Marks": [85, 90, 78, 88]
}   
df=pd.DataFrame(data)
new_df=df.drop([1,3])
print(new_df)
      
#10.Calculating Summary Statistics
import pandas as pd
data = {
    "Name": ["Ali", "Ahmed", "Sara", "Ayesha"],
    "Age": [20, 22, 19, 21],
    "Marks": [85, 90, 78, 88]
}
df = pd.DataFrame(data)

marks_mean = df["Marks"].mean()
marks_max = df["Marks"].max()
marks_min = df["Marks"].min()
print("Mean:", marks_mean)
print("Max:", marks_max)
print("Min:", marks_min)
print("--------")
df["Above_Avg"] = df["Marks"] > marks_mean
print(df)
      
#11.Grouping Data and Calculating Group-wise Statistics
import pandas as pd
data = {
    "Name": ["Ali", "Ahmed", "Sara", "Ayesha"],
    "Age": [20, 22, 19, 21],
    "Marks": [85, 90, 78, 88]
}
df = pd.DataFrame(data)  
df["Subject"]=["Math","Physics","Math","Physics"]

group=df.groupby("Subject")["Marks"].mean()     
print(group)  
      
#12.Sorting a DataFrame by a Column
import pandas as pd 
data = {
    "Name": ["Ali", "Ahmed", "Sara", "Ayesha"],
    "Age": [20, 22, 19, 21],
    "Marks": [85, 90, 78, 88]
}
df = pd.DataFrame(data)
df_sorted=df.sort_values(by="Marks",ascending=True)
print(df_sorted)
      
#13.Adding a New Row to a DataFrame
import pandas as pd
data = {
    "Name": ["Ali", "Ahmed", "Sara", "Ayesha"],
    "Age": [20, 22, 19, 21],
    "Marks": [85, 90, 78, 88]
}     
df = pd.DataFrame(data)
new_row = {"Name": "Bilal", "Age": 20, "Marks": 82, "Grade": "B", "Subject": "Math"}
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
print(df)      

#14.Finding the Top N Rows Based on a Column
import pandas as pd
data = {
    "Name": ["Ali", "Ahmed", "Sara", "Ayesha"],
    "Age": [20, 22, 19, 21],
    "Marks": [85, 90, 78, 88]
}     
df = pd.DataFrame(data)
top2 = df.nlargest(2, "Marks")
print(top2)

#15.Creating a Pivot Table
import pandas as pd
data = {
    "Name": ["Ali", "Ahmed", "Sara", "Ayesha"],
    "Age": [20, 22, 19, 21],
    "Marks": [85, 90, 78, 88]
}
df = pd.DataFrame(data)
df["Subject"] = ["Math", "Physics", "Math", "Physics"]
df["Grade"] = ["A", "A", "B", "A"]
summary = df.groupby(["Subject", "Grade"]).size().reset_index(name="Count")
print(summary)

#16.Merging Two DataFrames
import pandas as pd
df1 = pd.DataFrame({
    "ID": [1,2,3,4],
    "Name": ["Ali","Ahmed","Sara","Ayesha"]
})
df2 = pd.DataFrame({
    "ID": [1,2,3,5],
    "Marks": [85,90,78,88]
})
inner_merge = pd.merge(df1, df2, on="ID", how="inner")
print(inner_merge)

#17.Left Join Two DataFrames
import pandas as pd
df1 = pd.DataFrame({
    "ID": [1,2,3,4],
    "Name": ["Ali","Ahmed","Sara","Ayesha"]
})
df2 = pd.DataFrame({
    "ID": [1,2,3,5],
    "Marks": [85,90,78,88]
})
left_join = pd.merge(df1, df2, on="ID", how="left")
print(left_join)

#18.Right Join Two DataFrames
import pandas as pd
data=({
    "Name": ["Ali","Ahmed","Sara","Ayesha"],
    "Subject": ["Math","Physics","Math","Physics"],
    "Marks": [85,90,78,88]
})
df=pd.DataFrame(data)
pivot = pd.pivot_table(df, 
                       index="Subject",
                       values="Marks",
                       aggfunc="mean")
print(pivot)

#19.Multi-Level Indexing
import pandas as pd
data = {
    "Name": ["Ali", "Ahmed", "Sara", "Ayesha"],
    "Age": [20, 22, 19, 21],
    "Marks": [85, 90, 78, 88]
}
df = pd.DataFrame(data)
df["Subject"] = ["Math", "Physics", "Math", "Physics"]

df["Grade"] = ["A","A","B","A"]
df_multi = df.set_index(["Subject","Grade"])
print(df_multi)


#20.Applying a Function to a Column
import pandas as pd
data = {
    "Name": ["Ali", "Ahmed", "Sara", "Ayesha"],
    "Age": [20, 22, 19, 21],
    "Marks": [85, 90, 78, 88]
}
df = pd.DataFrame(data)
df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 80 else "Fail")
print(df)

#21.GroupBy with Multiple Aggregations
import pandas as pd
data = {
    "Name": ["Ali","Ahmed","Sara","Ayesha","Bilal","Hina","Zain","Iqra"],
    "Department": ["IT","HR","IT","HR","IT","HR","IT","HR"],
    "Salary": [50000,45000,52000,48000,51000,47000,53000,49000],
    "Experience": [2,3,4,2,3,5,6,4]
}
df = pd.DataFrame(data)
result = df.groupby("Department").agg(
    mean_salary=("Salary", "mean"),
    max_salary=("Salary", "max"),
    total_employees=("Name", "count"),
    average_experience=("Experience", "mean")
)
print(result)

#22.Calculating the Difference from Group Mean
import pandas as pd
data = {
    "Name": ["Ali","Ahmed","Sara","Ayesha","Bilal","Hina","Zain","Iqra"],
    "Department": ["IT","HR","IT","HR","IT","HR","IT","HR"],
    "Salary": [50000,45000,52000,48000,51000,47000,53000,49000],
    "Experience": [2,3,4,2,3,5,6,4]
}
df = pd.DataFrame(data)
df["Salary_Diff_From_Department_Mean"] = (
    df["Salary"] - df.groupby("Department")["Salary"].transform("mean")
)
print(df)

#23.Ranking Within Groups
import pandas as pd
data = {
    "Name": ["Ali","Ahmed","Sara","Ayesha","Bilal","Hina","Zain","Iqra"],
    "Department": ["IT","HR","IT","HR","IT","HR","IT","HR"],
    "Salary": [50000,45000,52000,48000,51000,47000,53000,49000],
    "Experience": [2,3,4,2,3,5,6,4]
}
df = pd.DataFrame(data)
df["Dept_Rank"] = df.groupby("Department")["Salary"] \
                    .rank(method="dense", ascending=False)
print(df)

#24.Querying with Multiple Conditions
import pandas as pd
data = {
    "Name": ["Ali","Ahmed","Sara","Ayesha","Bilal","Hina","Zain","Iqra"],
    "Department": ["IT","HR","IT","HR","IT","HR","IT","HR"],
    "Salary": [50000,45000,52000,48000,51000,47000,53000,49000],
    "Experience": [2,3,4,2,3,5,6,4]
}
df = pd.DataFrame(data)
result = df.query("Salary > 50000 and Experience >= 3")
print(result)

#25.Calculating Group-wise Averages and Sorting
import pandas as pd
data = {
    "Name": ["Ali","Ahmed","Sara","Ayesha","Bilal","Hina","Zain","Iqra"],
    "Department": ["IT","HR","IT","HR","IT","HR","IT","HR"],
    "Salary": [50000,45000,52000,48000,51000,47000,53000,49000],
    "Experience": [2,3,4,2,3,5,6,4]
}
df = pd.DataFrame(data)
result= (
    df[df["Salary"] > 48000]
    .groupby("Department")["Salary"]
    .mean()
    .sort_values(ascending=False)
)
print(result)