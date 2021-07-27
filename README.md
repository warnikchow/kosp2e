# kosp2e
Korean Speech to English Translation Corpus

## Dataset
### Freely available
* Speech files
* Train/Dev/Test filenames' list their English translation
### Provided under request (in [this link](https://docs.google.com/forms/d/1UTpOrKIWK9uzngh7eIm-3oAp5b5vTdBj4ZapHj8cyBI/edit))
* Korean scripts
* Other metadata (for StyleKQC and Covid-ED)

## Howto
```
git clone https://github.com/warnikchow/kosp2e
cd kosp2e
mkdir data
cd data
wget https://www.dropbox.com/s/y74ew1c1evdoxs1/data.zip
unzip data.zip
```
Then you get the folder with speech files (*data* and subfolders) and split files' list (*split* and .xlsx files).

## Specification
|  Dataset |     License     |                  Domain                  |                                    Characteristics                                   |                           Volume<br>(Train / Dev / Test)                           | Tokens<br>(ko / en) | Speakers<br>(Total) |
|:--------:|:---------------:|:----------------------------------------:|:------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|:-------------------:|:-------------------:|
|  Zeroth  |    CC-BY 4.0    |             News / newspaper             |                        DB originally for<br>speech recognition                       |         22,263 utterances<br>(3,004 unique scripts)<br>(21,589 / 197 / 461)        |      72K / 120K     |         115         |
|    KSS   | CC-BY-NC-SA 4.0 | Textbook<br>(colloquial<br>descriptions) | Originally recorded<br>by a single speaker<br>(multi-speaker<br>recording augmented) | 25,708 utterances<br>= 12,854 * 2<br>(recording augmented)<br>(24,940 / 256 / 512) |      64K / 95K      |          17         |
| StyleKQC |   CC-BY-SA 4.0  |          AI agent<br>(commands)          |                Speech act (4) <br>and topic (6)<br>labels are included               |                      30,000 utterances<br>(28,800 / 400 / 800)                     |     237K / 391K     |          60         |
| Covid-ED | CC-BY-NC-SA 4.0 |           Diary<br>(monologue)           |             Sentences are in<br>document level;<br>emotion tags included             |                      32,284 utterances<br>(31,324 / 333 / 627)                     |     358K / 571K     |          71         |

- The total number of *.wav* files in *Zeroth* dataset does not match with the total number of translation pairs that are provided, since some of the examples were excluded in the corpus construction to guarantee the data quality. However, to maintain files of the original *Zeroth* dataset, we did not delete them from the *.wav* files folder. The preprocessing and data loading is not affected by the difference of file list.

## Baseline
|            Model           | BLEU | WER<br>(ASR) | BLEU<br>(MT/ST) |
|:--------------------------:|:----:|:------------:|:---------------:|
| ASR-MT (Pororo)            | 16.6 |     34.0     |    18.5 (MT)    |
| ASR-MT (PAPAGO)            | 21.3 |     34.0     |    25.0 (MT)    |
| Transformer (Vanilla)      |  2.6 |       -      |        -        |
| ASR pretraining            |  5.9 |     24.0*    |        -        |
| Transformer + Warm-up      |  *8.7* |       -      |    35.7 (ST)*   |
|              + Fine-tuning | *18.3* |       -      |        -        |

- *Some of the numerics* differ from the [paper](https://arxiv.org/abs/2107.02875)  (after fixing some errors), but may not influence the results much.

### Recipe
- [Fairseq](https://github.com/pytorch/fairseq) is required for the basic recipe. You may need to git clone [specific fairseq version](https://github.com/pytorch/fairseq/tree/148327d8c1e3a5f9d17a11bbb1973a7cf3f955d3) for replication.
- First, you preprocess the data, and then prepare them in a format that fit with transformer. Other part follows [fairseq S2T translation recipe with MuST-C](https://github.com/pytorch/fairseq/tree/148327d8c1e3a5f9d17a11bbb1973a7cf3f955d3/examples/speech_to_text). 
- The recipe below leads you to the *Vanilla* model (the most basic end-to-end version). For the advanced training, refer to the [paper](https://arxiv.org/abs/2107.02875) below.
```
python preprocessing.py

python prep_data.py --data-root dataset/ --task st --vocab-type unigram --vocab-size 8000

fairseq-train dataset/kr-en  --config-yaml config_st.yaml \
--train-subset train_st --valid-subset dev_st --save-dir result --num-workers 4 \
--max-tokens 40000 --max-update 50000 --task speech_to_text \
--criterion label_smoothed_cross_entropy --report-accuracy \
--arch s2t_transformer_s --optimizer adam --lr 2e-3 --lr-scheduler inverse_sqrt \
--warmup-updates 10000 --clip-norm 10.0 --seed 1 --update-freq 8 --fp16 
```

## Acknowledgement
This work was supported by **PAPAGO, NAVER Corp.** The authors appreciate Hyoung-Gyu Lee, ‪Eunjeong Lucy Park, Jihyung Moon, and Doosun Yoo for discussions and support.‬  Also, the authors thank Taeyoung Jo, Kyubyong Park, and Yoon Kyung Lee for sharing the resources.

### Copyright
```
Copyright 2021-present NAVER Corp.
```

### License
License of each subcorpus (including metadata and Korean script) follows the original license of the raw corpus. For *KSS* and *Covid-ED*, only academic usage is permitted.

### Citation
Will be updated if *INTERSPEECH 2021 proceedings* is out. arXiv version is [here](https://arxiv.org/abs/2107.02875).
```
@article{cho2021kosp2e,
  title={Kosp2e: Korean Speech to English Translation Corpus},
  author={Cho, Won Ik and Kim, Seok Min and Cho, Hyunchang and Kim, Nam Soo},
  journal={arXiv preprint arXiv:2107.02875},
  year={2021}
}
```

## Contact
Contact Won Ik Cho tsatsuki@snu.ac.kr for further question.
