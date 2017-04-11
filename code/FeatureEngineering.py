import pandas as pd
import numpy as np


def Staticfeature(staticfeature):
    arr=df[(df.iloc[:, 5] == staticfeature)].index.values
    
    #Extract all data about this feature
    listp,listd,listv = ([] for i in range(3))
    for i in arr:
        # Whitespace means NO for some feature, set as 0
        if df.iloc[i][6] == '':
           listp.append(df.iloc[i][0]) 
           listv.append('0')
        else:    
           listp.append(df.iloc[i][0])
           listv.append(df.iloc[i][6].replace(' ',''))
    
    df1 = pd.DataFrame({'Name':listp, staticfeature:listv})
    return df1
   
    

    

    
def Dynamicfeature(dynamicfeature):
    arr=df[(df.iloc[:, 6] == dynamicfeature)].index.values
    
    #Extract all data about this feature
    listp,listd,listv = ([] for i in range(3))
    for i in arr:
        listp.append(df.iloc[i][0])
        listd.append(df.iloc[i-1][6])
        listv.append(df.iloc[i+1][6].replace(' ',''))
    
    df1 = pd.DataFrame({'AP':listp, 'D':listd, 'V':listv})
    
   
    #Remove empty strings and non-numeric
    df1 = df1.replace('',np.nan).dropna()
    df1 = df1[df1['D'].str.isnumeric()]
    df1 = df1[df1['V'].str.isnumeric()]
    
    
    #Transform time-dependent feature into static(linear regression)
    #First group data by patients
    dicd = {k: list(v) for k,v in df1.groupby('AP')['D']}
    dicv = {k: list(v) for k,v in df1.groupby('AP')['V']}
    dic = {}
    
    for j in dicd:
        x = [float(a) for a in dicd[j]]
        y = [float(a) for a in dicv[j]]
          if all(v == 0 for v in x) is False:
          k,b = np.polyfit(x, y, 1)
          ave = sum(y)/float(len(y))
          #Data could be insufficent to derive regression
          dic[j] = [max(x),k,b,min(y),max(y),ave]
    
    df2 = pd.DataFrame.from_dict(dic, orient='index').reset_index()
    lf=Dynamicfeature

    df2.columns = ['Name',lf+'_Dmax',lf+'_k',lf+'_b',lf+'_Vmin',lf+'_Vmax',lf+'_Vave']
    return df2





def ALSscore(ALSscore):
    arr=df[(df.iloc[:, 5] == ALSscore)].index.values
    #Extract all data about this feature
    listp,listd,listv = ([] for i in range(3))
    for i in arr:
        listp.append(df.iloc[i][0])
        listd.append(df.iloc[i][6])
        listv.append(df.iloc[i+1][6].replace(' ',''))
    df1 = pd.DataFrame({'AP':listp, 'D':listd, 'V':listv})
    
    #Remove empty strings and non-numeric
    df1 = df1.replace('',np.nan).dropna()
    df1 = df1[df1['D'].str.isnumeric()]
    df1 = df1[df1['V'].str.isnumeric()]
    
    #Transform time-dependent feature into static(linear regression)
    dicd = {k: list(v) for k,v in df1.groupby('AP')['D']}
    dicv = {k: list(v) for k,v in df1.groupby('AP')['V']}
    dic = {}
    for j in dicd:
        x = [float(a) for a in dicd[j]]
        y = [float(a) for a in dicv[j]]
        if all(v == 0 for v in x) is False:
          k,b = np.polyfit(x, y, 1)
          dic[j] = [k]
          
    df2 = pd.DataFrame.from_dict(dic, orient='index').reset_index()
    df2.columns = ['Name','Progression']
    return df2
    



#Read csv file of raw clinical data.
df = pd.read_csv("/Users/Guang/Downloads/PRO-ACT/team1/5million.txt",header=None,names=['first'])
df=df['first'].str.split('|', 6, expand=True)




#Obtain dataframe for static features
dfOnset = Staticfeature('Onset Delta')
dfDiagnosis = Staticfeature('Diagnosis Delta')
dfLimb = Staticfeature('Site of Onset - Limb')
dfBulbar = Staticfeature('Site of Onset - Bulbar')
dfFamily = Staticfeature('Family History Delta')
dfAunt = Staticfeature('Aunt')
dfCousin = Staticfeature('Cousin')
dfFather = Staticfeature('Father')
dfGrandfather = Staticfeature('Grandfather')
dfGrandmother = Staticfeature('Grandmother')
dfMother = Staticfeature('Mother')
dfNephew = Staticfeature('Nephew')
dfNiece = Staticfeature('Niece')
dfSibling = Staticfeature('Sibling')
dfUncle = Staticfeature('Uncle')
dfSon = Staticfeature('Son')
dfDaughter = Staticfeature('Daughter')
dfSister = Staticfeature('Sister')
dfBrother = Staticfeature('Brother')
dfDemographic = Staticfeature('Demographic Delta')
dfAge = Staticfeature('Age')
dfSex = Staticfeature('Sex')
dfRaceAsian = Staticfeature('Race - Asian')
dfRaceBlack = Staticfeature('Race - Black/African American')
dfRaceCaucasian = Staticfeature('Race - Caucasian')
dfRaceOther = Staticfeature('Race - Other')




#Obtain dataframe for dynamic/time-dependent features
dfUrinePh = Dynamicfeature('Urine Ph')
dfUrineProtein = Dynamicfeature('Urine Protein')
dfUrineGlucose = Dynamicfeature('Urine Glucose')
dfAlbumin = Dynamicfeature('Albumin')
dfProtein = Dynamicfeature('Protein')
dfSodium = Dynamicfeature('Sodium')
dfPotassium = Dynamicfeature('Potassium')
dfBicarbonate = Dynamicfeature('Bicarbonate')
dfChloride = Dynamicfeature('Chloride')
dfBloodUrea = Dynamicfeature('Blood Urea Nitrogen (BUN)')
dfUricAcid = Dynamicfeature('Uric Acid')
dfCreatinine = Dynamicfeature('Creatinine')
dfALTSGPT = Dynamicfeature('ALT(SGPT)')
dfGammaglutamyltransferase = Dynamicfeature('Gamma-glutamyltransferase')
dfASTSGOT = Dynamicfeature('AST(SGOT)')
dfBilirubin = Dynamicfeature('Bilirubin (total)')
dfNeutrophils = Dynamicfeature('Neutrophils')
dfLymphocytes = Dynamicfeature('Lymphocytes')
dfMonocytes = Dynamicfeature('Monocytes')
dfEosinophils = Dynamicfeature('Eosinophils')
dfBasophils = Dynamicfeature('Basophils')
dfRedBlood = Dynamicfeature('Red Blood Cells (RBC)')
dfHemoglobin = Dynamicfeature('Hemoglobin')
dfHematocrit = Dynamicfeature('Hematocrit')
dfPlatelets = Dynamicfeature('Platelets')
dfCreatineKinase = Dynamicfeature('Creatine Kinase')
dfTriglycerides = Dynamicfeature('Triglycerides')
dfTotalCholesterol = Dynamicfeature('Total Cholesterol')
dfGlucose = Dynamicfeature('Glucose')
dfCalcium = Dynamicfeature('Calcium')
dfPhosphorus = Dynamicfeature('Phosphorus')
dfProthrombinTime = Dynamicfeature('Prothrombin Time (clotting)')
dfAmylase = Dynamicfeature('Amylase')




#Obtain the rate of progression of ALS patients
dfALSscore = ALSscore('ALSFRS Delta')




#Merge dataframes for all static features 
df_sta = dfOnset.merge(dfDiagnosis,on='Name', how='outer').merge(dfLimb,on='Name', how='outer').merge(dfBulbar,on='Name', how='outer').merge(
         dfFamily,on='Name', how='outer').merge(dfAunt,on='Name', how='outer').merge(dfCousin,on='Name', how='outer').merge(
         dfFather,on='Name', how='outer').merge(dfGrandfather,on='Name', how='outer').merge(
         dfGrandmother,on='Name', how='outer').merge(dfMother,on='Name', how='outer').merge(dfNephew,on='Name', how='outer').merge(
         dfNiece,on='Name', how='outer').merge(dfSibling,on='Name', how='outer').merge(dfUncle,on='Name', how='outer').merge(
         dfSon,on='Name', how='outer').merge(dfDaughter,on='Name', how='outer').merge(dfSister,on='Name', how='outer').merge(
         dfBrother,on='Name', how='outer').merge(dfDemographic,on='Name', how='outer').merge(dfAge,on='Name', how='outer').merge(
         dfSex,on='Name', how='outer').merge(dfRaceAsian,on='Name', how='outer').merge(dfRaceBlack,on='Name', how='outer').merge(
         dfRaceCaucasian,on='Name', how='outer').merge(dfRaceOther,on='Name', how='outer')


#Convert character features into numeric features
df_sta['Sex'] = df_sta['Sex'].map( {'Female': 0, 'Male': 1} ).astype(int) 
 



#Merge dataframes for all dynamic features 
df_lab = dfUrinePh.merge(dfUrineProtein,on='Name', how='outer').merge(dfUrineGlucose,on='Name', how='outer').merge(
         dfAlbumin,on='Name', how='outer').merge(dfProtein,on='Name', how='outer').merge(dfSodium,on='Name', how='outer').merge(
         dfPotassium,on='Name', how='outer').merge(dfBicarbonate,on='Name', how='outer').merge(dfChloride,on='Name', how='outer').merge(
         dfBloodUrea,on='Name', how='outer').merge(dfUricAcid,on='Name', how='outer').merge(dfCreatinine,on='Name', how='outer').merge(
         dfALTSGPT,on='Name', how='outer').merge(dfGammaglutamyltransferase,on='Name', how='outer').merge(dfASTSGOT,on='Name', how='outer').merge(
         dfBilirubin,on='Name', how='outer').merge(dfNeutrophils,on='Name', how='outer').merge(dfLymphocytes,on='Name', how='outer').merge(
         dfMonocytes,on='Name', how='outer').merge(dfEosinophils,on='Name', how='outer').merge(dfBasophils,on='Name', how='outer').merge(
         dfRedBlood,on='Name', how='outer').merge(dfHemoglobin,on='Name', how='outer').merge(dfHematocrit,on='Name', how='outer').merge(
         dfPlatelets,on='Name', how='outer').merge(dfCreatineKinase,on='Name', how='outer').merge(dfTriglycerides,on='Name', how='outer').merge(
         dfTotalCholesterol,on='Name', how='outer').merge(dfGlucose,on='Name', how='outer').merge(dfCalcium,on='Name', how='outer').merge(
         dfPhosphorus,on='Name', how='outer').merge(dfProthrombinTime,on='Name', how='outer').merge(dfAmylase,on='Name', how='outer')        



#Further merge
df_final = df_sta.merge(df_lab, on='Name', how='outer').merge(dfALSscore, on='Name', how='outer')



#Remove columns that have two many NaN.
df_final = df_final.loc[:, df_final.isnull().mean() <= 0.5]



#Fill in NaN with median of the column.
for i in df_final.columns:
    df_final[i]=df_final[i].fillna(df_final[i].median()) 


#Save to csv.  
df_final.to_csv('/Users/Guang/Downloads/df_final_5Mnew.txt', sep='\t')


         
