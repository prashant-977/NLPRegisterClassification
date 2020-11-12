## Getting data to train format:
```bash
pramah@biarc:~/CORE_registers_correct_classes/single_labels/fastText$ head -n 17589 ../train_file.txt > core.train
```
## Getting data to test format:
```bash
 head -n 2210 ../test_file.txt > core.test
```
## Our First Supervised Classifier:
```bash
 ./fasttext supervised -input ../core.train -output model_core
```
## Predicting on Devset data:
```bash
 ./fasttext predict model_core.bin -
 ```
 Tried a few labels from the devset data. Using our devset data, we get following result:
 ```bash
 ./fasttext test model_core.bin ../core.valid
N       2486
P@1     0.422
R@1     0.211
 ```
## Preprocessing in FastText:
 ```bash
 cat data/core.preprocessed.txt | tr '[:upper:]' '[:lower:]' | sed -e "s/'/ ' /g" -e 's/"//g' -e 's/\./ \. /g' -e 's/<br \/>/ /g' -e 's/,/ , /g' -e 's/(/ ( /g' -e 's/)/ ) /g' -e 's/\!/ \! /g' -e 's/\?/ \? /g' -e 's/\;/ /g' -e 's/\:/ /g' |  sed 's/\,//g' | sed 's/\.//g' > data/core.preprocessed6.txt
 
 Shuffling dataset:
perl -MList::Util -e 'print List::Util::shuffle <>' data/core.preprocessed6.txt > data/core.preprocessed7.txt

 ```
 ## This is how we do autotune validation:
```bash

pramah@biarc:~/CORE_registers_correct_classes/single_labels/fastText$ ./fasttext supervised -input ../train_file_processed.txt -output model -autotune-validation ../core-test.valid
```

## This is how to test on the model 
```bash
./fasttext test model.bin ../core-test.valid
```
