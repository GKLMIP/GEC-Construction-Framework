import pandas
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

results = pandas.read_excel('Result/EnglishResultGPT4.xlsx', header=None).values.tolist()
datas = pandas.read_excel('EnglishTestData.xlsx').values.tolist()

answers = []
preds = []
for result in results:
    pred = result[1].strip()
    if pred == 'True':
        preds.append(1)
    elif pred == 'False':
        preds.append(0)
    answer = datas[result[0]][0]
    answers.append(answer)

print(accuracy_score(answers,preds),end='\t')
print(precision_score(answers,preds),end='\t')
print(recall_score(answers,preds),end='\t')
print(f1_score(answers,preds))



answers = []
preds = []
for result in results:
    pred = result[2].strip()
    if pred == 'True':
        preds.append(1)
    elif pred == 'False':
        preds.append(0)
    answer = datas[result[0]][1]
    answers.append(answer)

print(accuracy_score(answers,preds),end='\t')
print(precision_score(answers,preds),end='\t')
print(recall_score(answers,preds),end='\t')
print(f1_score(answers,preds))
