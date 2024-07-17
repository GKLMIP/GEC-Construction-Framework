import pandas
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

results = pandas.read_excel('Result/IndonesianResultGPT3.5.xlsx', header=None).values.tolist()
datas = pandas.read_excel('IndonesianData.xlsx').values.tolist()

answers = []
preds = []
for result in results:
    pred = result[1].strip()
    if pred.lower() == 'true' or pred.lower() == 'benar':
        preds.append(1)
    elif pred.lower() == 'false' or pred.lower() == 'salah' or pred.lower() == 'tidak':
        preds.append(0)

    answer = datas[result[0]][0]
    if answer == '是':
        answers.append(1)
    elif answer == '否':
        answers.append(0)

print(len(answers))
print(len(preds))
print(accuracy_score(answers,preds),end='\t')
print(precision_score(answers,preds),end='\t')
print(recall_score(answers,preds),end='\t')
print(f1_score(answers,preds))

answers = []
preds = []
for result in results:
    pred = result[2].strip()
    if pred.lower() == 'true' or pred.lower() == 'benar':
        preds.append(1)
    elif pred.lower() == 'false' or pred.lower() == 'salah' or pred.lower() == 'tidak':
        preds.append(0)

    answer = datas[result[0]][1]
    if answer == '是':
        answers.append(1)
    elif answer == '否':
        answers.append(0)

print(len(answers))
print(len(preds))
print(accuracy_score(answers,preds),end='\t')
print(precision_score(answers,preds),end='\t')
print(recall_score(answers,preds),end='\t')
print(f1_score(answers,preds))

