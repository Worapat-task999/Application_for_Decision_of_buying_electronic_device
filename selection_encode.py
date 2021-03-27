import pandas as pd
import scipy.stats as stats
from sklearn import preprocessing
selection_drop=[]
col_list = ["grade","faculty","department","price","purpose1","purpose2","purpose3","freaquency","gender","class label"]
data = pd.read_csv(r'D:\Worksapce\VSWorksapce\dataset.csv')

class ChiSquare:
    def __init__(self, dataframe):
        self.df = dataframe
        self.p = None #P-Value
        self.chi2 = None #Chi Test Statistic
        self.dof = None
        
        self.dfObserved = None
        self.dfExpected = None
        
    def _print_chisquare_result(self, colX, alpha):
        result = ""
        if self.p<alpha:
            result="{0} can use in model".format(colX)
        else:
            result="{0} not use in model".format(colX)
            selection_drop.append(colX)
        print(result)
        
    def TestIndependence(self,colX,colY, alpha=0.01):
        X = self.df[colX].astype(str)
        Y = self.df[colY].astype(str)

        self.dfObserved = pd.crosstab(Y,X) 
        chi2, p, dof, expected = stats.chi2_contingency(self.dfObserved.values)
        self.p = p
        self.chi2 = chi2
        self.dof = dof   
        self.dfExpected = pd.DataFrame(expected, columns=self.dfObserved.columns, index = self.dfObserved.index)
        
        self._print_chisquare_result(colX,alpha)

#selection attribute
data_selection=data.copy()
cT = ChiSquare(data_selection)
for var in col_list:
    if var != "class label" :
        cT.TestIndependence(colX=var,colY="class label" )
        
#drop attribute
data_selection.drop(selection_drop, axis=1, inplace=True)

#endcoded data
data_encoded=data_selection.copy()
le = preprocessing.LabelEncoder()
for att in data_encoded:
    if att != "class label" :
        data_encoded[att]= le.fit_transform(data_encoded[att])
        
#data_encoded.to_csv(r'D:\Worksapce\VSWorksapce\dataset_encoded.csv') #export data cleaning and encoded to csv
#data_selection.to_csv(r'D:\Worksapce\VSWorksapce\clean_encode_dataset.csv')  #export data cleaning  to csv 






