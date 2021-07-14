# kosp2e
Korean Speech to English Translation Corpus

## Dataset
### Freely available
* Speech files
* Train/Dev/Test filenames' list their English translation
### Provided under request
* Korean scripts
* Other metadata (for StyleKQC and Covid-ED)

## Howto
```
git clone https://github.com/warnikchow/kosp2e
cd kosp2e
mkdir data
cd data
wget https://www.dropbox.com/s/y3kdlx467qspvqt/data.zip
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
- Currently, the emotion tags in *Covid-ED* dataset is in cleansing. This does not affect the end-to-end or pipeline processing of the files.

## Baseline
|            Model           | BLEU | WER<br>(ASR) | BLEU<br>(MT/ST) |
|:--------------------------:|:----:|:------------:|:---------------:|
| ASR-MT (Pororo)            | 16.6 |     34.0     |    18.5 (MT)    |
| ASR-MT (PAPAGO)            | 21.3 |     34.0     |    25.0 (MT)    |
| Transformer (Vanilla)      |  2.6 |       -      |        -        |
| ASR pretraining            |  5.9 |     24.0*    |        -        |
| Transformer + Warm-up      | 11.6 |       -      |    35.7 (ST)*   |
|              + Fine-tuning | 18.0 |       -      |        -        |

### Recipe
To be added later.

## Acknowledgement
This work was supported by PAPAGO, NAVER Corp. The authors appreciate Hyoung-Gyu Lee, ‪Eunjeong Lucy Park, Jihyung Moon, and Doosun Yoo for discussions and support.‬  Also, the authors thank Taeyoung Jo, Kyubyong Park, and Yoon Kyung Lee for sharing the resources.

### Copyright
```
Copyright 2021-present NAVER Corp.
```

### License
License of each subcorpus (including metadata and Korean script) follows the original license of the raw corpus. For *KSS* and *Covid-ED*, only academic usage is permitted.

### Citation
Will be updated if INTERSPEECH 2021 proceeding is out.
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
