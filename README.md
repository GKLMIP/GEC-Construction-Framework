# GEC-Construction-Framework

# Corpus
The file "IndonesianTest.json" is our self-construct datasets.

# Inference using GPT3.5 or GPT4
    python UseChatGPTforEnglish.py (for English)
    python UseChatGPT.py (for Indonesian)    

# Inference using Open-source LLMs
    python Inference-Open.py

# Evaluation
    python EvaluateEnglishResult-ChatGPT.py (for English)
    python EvaluateIndonesianResult-Close.py (for Indonesian GPT3.5 or GPT4)
    python EvaluateIndonesianResult-Open.py (for Indonesian Open-source LLMs)

# Train and Test the GEC Model

## You can get the data we trained the model with [Google Driver](https://drive.google.com/file/d/117NcGsPxMyyOp-avDDdT24dP6fU6aFua/view?usp=sharing).

## We use version 0.10.2 of [Fairseq](https://github.com/facebookresearch/fairseq/releases/tag/v0.10.2) to train and test the model. Please download the Fairseq project, and then put the 'Sort.py' file and 'm2scorer' filefold in the Fairseq project.

## Train Script
    CUDA_VISIBLE_DEVICES=0 python train.py ./IndoGECDataset --save-dir ./IndoTransformer --seed 4321 --max-epoch 50 --batch-size 64 --max-tokens 4096 --train-subset train --valid-subset valid --arch transformer --lr-scheduler triangular --max-lr 0.004 --lr-period-updates 73328 --clip-norm 2 --lr 0.001 --lr-shrink 0.95 --shrink-min --dropout 0.2 --relu-dropout 0.2 --attention-dropout 0.2 --encoder-embed-dim 512 --decoder-embed-dim 512 --max-target-positions 1024 --max-source-positions 1024 --encoder-ffn-embed-dim 4096 --decoder-ffn-embed-dim 4096 --encoder-attention-heads 8 --decoder-attention-heads 8 --share-all-embeddings --log-interval 1000 --fp16

## Test Scripts
    python generate.py IndoGECDataset --path IndoTransformer/checkpoint_best.pt --batch-size 512 --beam 5 --remove-bpe > result/nbest.txt  --fp16
    cat result/nbest.txt | grep "^H" | python ./sort.py 1 result/output.txt
    python ./m2scorer/m2scorer -v result/output.txt ./IndoGECDataset/gold > result/result.txt
