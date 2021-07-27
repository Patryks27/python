import scikitplot as skplt
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
#do danych
import numpy as np
import pandas as pd
#do wykresów
import matplotlib.pyplot as plt


#plik=  pd.read_excel(r"D:\uczacay.xlsx");

plik =pd.ExcelFile(r"D:\uczacay.xlsx");

dane = plik.parse('Arkusz1')
dane = dane.dropna()

dane_testowe = plik.parse('Arkusz2')
dane_testowe = dane_testowe.dropna()


y_true = dane;
y_probas = dane_testowe;
print(y_probas)
print(y_true)


skplt.metrics.plot_roc(y_true, y_probas, figsize=(10, 8))   # Plot ROC Curve
plt.show()
#skplt.metrics.plot_roc(y_true,y_probas)


#skplt.metrics.plot_roc_curve(y_true, y_probas);
#plt.show()