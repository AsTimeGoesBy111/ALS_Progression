import pandas as pd
import numpy as np


Figure
df = pd.read_csv("/Users/Guang/Downloads/PRO-ACT/team1/5million.txt",header=None,names=['first'])
df=df['first'].str.split('|', 6, expand=True)


def bpd(clinicalfeature):
    arr=df[(df.iloc[:, 5] == clinicalfeature)].index.values
    #Extract all data about this feature
    listp,listd,listv = ([] for i in range(3))
    for i in arr:
        if (df.ix[i-1][5]=='Height'):
           listp.append(df.iloc[i][0])
           listd.append(df.iloc[i][6])
           listv.append(df.iloc[i-3][6].replace(' ',''))
        else:
           listp.append(df.iloc[i][0])
           listd.append(df.iloc[i][6])
           listv.append(df.iloc[i-2][6].replace(' ',''))
         
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
          ave = sum(y)/float(len(y))
          dic[j] = [max(x),k,b,min(y),max(y),ave]
    #return dic
    df2 = pd.DataFrame.from_dict(dic, orient='index').reset_index()
    lf='bpd'
    df2.columns = ['Name',lf+'_Dmax',lf+'_k',lf+'_b',lf+'_Vmin',lf+'_Vmax',lf+'_Vave']
    return df2



def bps(clinicalfeature):
    arr=df[(df.iloc[:, 5] == clinicalfeature)].index.values
    #Extract all data about this feature
    listp,listd,listv = ([] for i in range(3))
    for i in arr:
        if (df.ix[i-1][5]=='Height'):
           listp.append(df.iloc[i][0])
           listd.append(df.iloc[i][6])
           listv.append(df.iloc[i-2][6].replace(' ',''))
        else:
           listp.append(df.iloc[i][0])
           listd.append(df.iloc[i][6])
           listv.append(df.iloc[i-1][6].replace(' ',''))
         
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
          ave = sum(y)/float(len(y))
          dic[j] = [max(x),k,b,min(y),max(y),ave]
    #return dic
    df2 = pd.DataFrame.from_dict(dic, orient='index').reset_index()
    lf='bps'
    df2.columns = ['Name',lf+'_Dmax',lf+'_k',lf+'_b',lf+'_Vmin',lf+'_Vmax',lf+'_Vave']
    return df2
    
    
def pul(clinicalfeature):
    arr=df[(df.iloc[:, 5] == clinicalfeature)].index.values
    #Extract all data about this feature
    listp,listd,listv = ([] for i in range(3))
    for i in arr:
        if (df.ix[i-1][5]=='Height'):
           listp.append(df.iloc[i][0])
           listd.append(df.iloc[i][6])
           listv.append(df.iloc[i+1][6].replace(' ',''))
        else:
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
          ave = sum(y)/float(len(y))
          dic[j] = [max(x),k,b,min(y),max(y),ave]
    #return dic
    df2 = pd.DataFrame.from_dict(dic, orient='index').reset_index()
    lf='pulse'
    df2.columns = ['Name',lf+'_Dmax',lf+'_k',lf+'_b',lf+'_Vmin',lf+'_Vmax',lf+'_Vave']
    return df2




def Staticfeature(staticfeature):
    arr=df[(df.iloc[:, 5] == staticfeature)].index.values
    #print(arr)
    #Extract all data about this feature
    listp,listd,listv = ([] for i in range(3))
    for i in arr:
        if df.iloc[i][6] == '':
           listp.append(df.iloc[i][0]) 
           listv.append('0')
        else:    
           listp.append(df.iloc[i][0])
           listv.append(df.iloc[i][6].replace(' ',''))
    df1 = pd.DataFrame({'Name':listp, staticfeature:listv})
    df1 = df1.replace('',np.nan).dropna()
    return df1
   
    
    

    
def Labfeature(labfeature):
    arr=df[(df.iloc[:, 6] == labfeature)].index.values
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
    dicd = {k: list(v) for k,v in df1.groupby('AP')['D']}
    dicv = {k: list(v) for k,v in df1.groupby('AP')['V']}
    dic = {}
    for j in dicd:
        x = [float(a) for a in dicd[j]]
        y = [float(a) for a in dicv[j]]
        if all(v == 0 for v in x) is False:
          k,b = np.polyfit(x, y, 1)
          ave = sum(y)/float(len(y))
          dic[j] = [max(x),k,b,min(y),max(y),ave]
    #return dic
    df2 = pd.DataFrame.from_dict(dic, orient='index').reset_index()
    lf=labfeature
    df2.columns = ['Name',lf+'_Dmax',lf+'_k',lf+'_b',lf+'_Vmin',lf+'_Vmax',lf+'_Vave']
    return df2






def ALSscore(ALSscore):
    arr=df[(df.iloc[:, 5] == ALSscore)].index.values
    #print(arr)
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
        if len(x) >1:
          k,b = np.polyfit(x, y, 1)
          dic[j] = [k,max(x)]
    #return dic
    df2 = pd.DataFrame.from_dict(dic, orient='index').reset_index()
    df2.columns = ['Name','Progression','Survival']
    return df2
    

# def get_nan_cols(df, nan_percent=0.8):
#     threshold = len(df.index) * nan_percent
#     return [c for c in df.columns if sum(df[c].isnull()) >= threshold] 
    
    
res_bpd = bpd('Vital Signs Delta')
res_bps = bps('Vital Signs Delta')
res_pul = pul('Vital Signs Delta')    
dfClinicalFeature=res_bpd.merge(res_bps, on='Name', how='outer').merge(res_pul, on='Name', how='outer')    
dfALSscore = ALSscore('ALSFRS Delta')


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




dfUrinePh = Labfeature('Urine Ph')
dfUrineProtein = Labfeature('Urine Protein')
#dfUrineSpecific = Labfeature('Urine Specific')
dfUrineGlucose = Labfeature('Urine Glucose')
#dfUrineWBC = Labfeature('Urine WBC')
#dfUrineLeukoesterase = Labfeature('Urine Leukoesterase')
#dfUrineBlood = Labfeature('Urine Blood')
#dfUrineRBCs = Labfeature('Urine RBCs')
#dfUrinecasts = Labfeature('Urine casts')
#dfUrineKetones = Labfeature('Urine Ketones')
dfAlbumin = Labfeature('Albumin')
dfProtein = Labfeature('Protein')
dfSodium = Labfeature('Sodium')
dfPotassium = Labfeature('Potassium')
dfBicarbonate = Labfeature('Bicarbonate')
dfChloride = Labfeature('Chloride')
#dfAnionGap = Labfeature('Anion Gap')
#dfMagnesium = Labfeature('Magnesium')
dfBloodUrea = Labfeature('Blood Urea Nitrogen (BUN)')
dfUricAcid = Labfeature('Uric Acid')
dfCreatinine = Labfeature('Creatinine')
#dfAlkalinephosphatase = Labfeature('Alkaline phosphatase')
dfALTSGPT = Labfeature('ALT(SGPT)')
dfGammaglutamyltransferase = Labfeature('Gamma-glutamyltransferase')
dfASTSGOT = Labfeature('AST(SGOT)')
dfBilirubin = Labfeature('Bilirubin (total)')
#dfWhiteBlood = Labfeature('White Blood Cell (WBC)')
dfNeutrophils = Labfeature('Neutrophils')
#dfAbsoluteBand = Labfeature('Absolute Band Neutrophils')
dfLymphocytes = Labfeature('Lymphocytes')
dfMonocytes = Labfeature('Monocytes')
dfEosinophils = Labfeature('Eosinophils')
dfBasophils = Labfeature('Basophils')
dfRedBlood = Labfeature('Red Blood Cells (RBC)')
dfHemoglobin = Labfeature('Hemoglobin')
dfHematocrit = Labfeature('Hematocrit')
dfPlatelets = Labfeature('Platelets')
dfCreatineKinase = Labfeature('Creatine Kinase')
dfTriglycerides = Labfeature('Triglycerides')
dfTotalCholesterol = Labfeature('Total Cholesterol')
#dfLactatedehydrogenase = Labfeature('Lactate dehydrogenase')
dfGlucose = Labfeature('Glucose')
#dfHbA1c = Labfeature('HbA1c')
dfCalcium = Labfeature('Calcium')
dfPhosphorus = Labfeature('Phosphorus')
#dfHepatitis = Labfeature('Hepatitis')
#dfImmunoglobulins = Labfeature('Immunoglobulins')
#dfGammaGlobulin = Labfeature('Gamma Globulin')
#dfThyroidStimulating = Labfeature('Thyroid Stimulating Hormone')
#dfFreeT3 = Labfeature('Free T3')
#dfFreeT4 = Labfeature('Free T4')
#dfBetaHCG = Labfeature('Beta HCG')
dfProthrombinTime = Labfeature('Prothrombin Time (clotting)')
#dfInternationalNormalized = Labfeature('International Normalized Ratio (clotting)')
dfAmylase = Labfeature('Amylase')


df_sta = dfOnset.merge(
         dfDiagnosis,on='Name', how='outer').merge(dfLimb,on='Name', how='outer').merge(dfBulbar,on='Name', how='outer').merge(
         dfFamily,on='Name', how='outer').merge(dfAunt,on='Name', how='outer').merge(
         dfCousin,on='Name', how='outer').merge(dfFather,on='Name', how='outer').merge(dfGrandfather,on='Name', how='outer').merge(
         dfGrandmother,on='Name', how='outer').merge(dfMother,on='Name', how='outer').merge(dfNephew,on='Name', how='outer').merge(
         dfNiece,on='Name', how='outer').merge(dfSibling,on='Name', how='outer').merge(dfUncle,on='Name', how='outer').merge(
         dfSon,on='Name', how='outer').merge(dfDaughter,on='Name', how='outer').merge(dfSister,on='Name', how='outer').merge(
         dfBrother,on='Name', how='outer').merge(dfDemographic,on='Name', how='outer').merge(dfAge,on='Name', how='outer').merge(
         dfSex,on='Name', how='outer').merge(dfRaceAsian,on='Name', how='outer').merge(dfRaceBlack,on='Name', how='outer').merge(
         dfRaceCaucasian,on='Name', how='outer').merge(dfRaceOther,on='Name', how='outer')

df_sta['Sex'] = df_sta['Sex'].map( {'Female': 0, 'Male': 1} ).astype(int) 
 
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

df_sta=df_sta.drop_duplicates()
df_lab=df_lab.drop_duplicates()
dfClinicalFeature=dfClinicalFeature.drop_duplicates()
dfALSscore 


df_final = df_sta.merge(df_lab, on='Name', how='outer').merge(dfClinicalFeature, on='Name', how='outer').merge(dfALSscore, on='Name', how='outer')

#df_final
df_final = df_final.loc[:, df_final.isnull().mean() <= 0.5]

for i in df_final.columns:
    df_final[i]=df_final[i].fillna(df_final[i].median()) 
#del df_final[get_nan_cols(df_final, 0.8)]    
df_final.to_csv('/Users/Guang/Downloads/PRO-ACT/team1/df_final.txt', sep='\t')
print('finish!')
#list(df_final)


#df_sta[['Name','Aunt','Sex']]
#df = pd.read_csv("/Users/Guang/Downloads/PRO-ACT/team1/clinicalfeature.txt",delim_whitespace=True)


         
