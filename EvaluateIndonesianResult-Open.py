import json
import pandas
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

datas = pandas.read_excel('IndonesianData.xlsx').values.tolist()


with open('Result/IndonesianData-Task1-Format/evaluation-polylm-13b.json', encoding='utf-8') as f:
    model_preds = json.load(f)

answers = []
preds = []
for num, pred in enumerate(model_preds["instances"]):
    answer = datas[num][0]
    pred = pred["predict"]
    # print(pred)
    true_position = pred.find('true')
    false_position = pred.find('false')
    # print(true_position, false_position)
    if true_position < 0:
        true_position = 100
    if false_position < 0:
        false_position = 100
    # print(true_position, false_position)
    if true_position == 100 and false_position == 100:
        if answer == '是':
            answers.append(1)
            preds.append(0)
        elif answer == '否':
            answers.append(0)
            preds.append(1)
    else:
        if true_position < false_position:
            preds.append(1)
        else:
            preds.append(0)
        # print(answer)
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



with open('Result/IndonesianData-Task2-Format/evaluation-polylm-13b.json', encoding='utf-8') as f:
    model_preds = json.load(f)

answers = []
preds = []
for num, pred in enumerate(model_preds["instances"]):
    answer = datas[num][1]
    pred = pred["predict"]
    # print(pred)
    true_position = pred.find('true')
    false_position = pred.find('false')
    # print(true_position, false_position)
    if true_position < 0:
        true_position = 100
    if false_position < 0:
        false_position = 100
    # print(true_position, false_position)
    if true_position == 100 and false_position == 100:
        if answer == '是':
            answers.append(1)
            preds.append(0)
        elif answer == '否':
            answers.append(0)
            preds.append(1)
    else:
        if true_position < false_position:
            preds.append(1)
        else:
            preds.append(0)
        # print(answer)
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