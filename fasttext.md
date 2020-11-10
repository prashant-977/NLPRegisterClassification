## This is how we do autotune validation:
```bash
pramah@biarc:~/CORE_registers_correct_classes/single_labels/fastText$ ./fasttext supervised -input ../train_file_processed.txt -output model -autotune-validation ../core-test.valid
```

## This is how to test on the model 
```bash
./fasttext test model.bin ../core-test.valid
```
