# kosp2e
Korean Speech to English Translation Corpus

## Dataset
### Freely available
* Speech files
* Train/Dev/Test filenames' list their English translation
### Provided under request
* Korean scripts
* Other metadata (for StyleKQC and Covid-ED)

## Specification
|  Dataset |     License     |                  Domain                  |                                    Characteristics                                   |                           Volume<br>(Train / Dev / Test)                           | Tokens<br>(ko / en) | Speakers<br>(Total) |
|:--------:|:---------------:|:----------------------------------------:|:------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|:-------------------:|:-------------------:|
|  Zeroth  |    CC-BY 4.0    |             News / newspaper             |                        DB originally for<br>speech recognition                       |         22,263 utterances<br>(3,004 unique scripts)<br>(21,589 / 197 / 461)        |      72K / 120K     |         115         |
|    KSS   | CC-BY-NC-SA 4.0 | Textbook<br>(colloquial<br>descriptions) | Originally recorded<br>by a single speaker<br>(multi-speaker<br>recording augmented) | 25,708 utterances<br>= 12,854 * 2<br>(recording augmented)<br>(24,940 / 256 / 512) |      64K / 95K      |          17         |
| StyleKQC |   CC-BY-SA 4.0  |          AI agent<br>(commands)          |                Speech act (4) <br>and topic (6)<br>labels are included               |                      30,000 utterances<br>(28,800 / 400 / 800)                     |     237K / 391K     |          60         |
| Covid-ED | CC-BY-NC-SA 4.0 |           Diary<br>(monologue)           |             Sentences are in<br>document level;<br>emotion tags included             |                      32,284 utterances<br>(31,324 / 333 / 627)                     |     358K / 571K     |          71         |

## Baseline
|            Model           | BLEU | WER<br>(ASR) | BLEU<br>(MT/ST) |
|:--------------------------:|:----:|:------------:|:---------------:|
| ASR-MT (Pororo)            | 16.6 |     34.0     |    18.5 (MT)    |
| ASR-MT (PAPAGO)            | 21.3 |     34.0     |    25.0 (MT)    |
| Transformer (Vanilla)      |  2.6 |       -      |        -        |
| ASR pretraining            |  5.9 |     24.0*    |        -        |
| Transformer + Warm-up      | 11.6 |       -      |    35.7 (ST)*   |
|              + Fine-tuning | 18.0 |       -      |        -        |

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

## Recipe
To be added later.

## Contact
Contact Won Ik Cho tsatsuki@snu.ac.kr for further question.
