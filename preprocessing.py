import os
import librosa
from glob import glob
import pandas as pd
import shutil

if not os.path.exists('dataset/kr-en/data'):
    os.makedirs('dataset/kr-en/data/dev/txt')
    os.makedirs('dataset/kr-en/data/test/txt')
    os.makedirs('dataset/kr-en/data/train/txt')
    os.makedirs('dataset/kr-en/data/dev/wav')
    os.makedirs('dataset/kr-en/data/test/wav')
    os.makedirs('dataset/kr-en/data/train/wav')      
    os.makedirs('result')
    
data = ['covid', 'kss', 'stylekqc', 'zeroth']
split = ['train', 'test', 'dev']

for i in data:
    for j in split:
        filename = 'split/'+i+'_'+j+'.xlsx'
        print(filename)
        df_excel = pd.read_excel(filename, engine = 'openpyxl')
        
        exist_list = []
        kr_list =[]
        eng_list = []
        
        for k in range(len(df_excel)):
            #print (k, end="\r")
            exist_list.append(df_excel.iloc[k][1])
            kr_list.append("한국어 텍스트 필요시 요청바람/Request if you need Korean scripts.")
            eng_list.append(df_excel.iloc[k][2])
        
        g = open("dataset/kr-en/data/"+j+"/txt/"+j+".kr", "a", encoding="UTF8")
        h = open("dataset/kr-en/data/"+j+"/txt/"+j+".en", "a", encoding="UTF8")
        m = open("dataset/kr-en/data/"+j+"/txt/"+j+".yaml", "a", encoding="UTF8")
        
        for l in range(len(exist_list)):
            print(l, end='\r')
            file = "data/"+i+"/"+exist_list[l]+'.wav'
            desti = 'dataset/kr-en/data/'+j+'/wav/'+exist_list[l]+'.wav'
            shutil.copyfile(file, desti)
            g.write(kr_list[l]+'\n')
            h.write(eng_list[l]+'\n')
            m.write('- {duration: '+str(librosa.get_duration(filename=file))[:8]+', offset: 0.000000, speaker_id: spk.1, wav: '+file.split('/')[-1]+'}\n')
            
        
g.close()
h.close()
m.close()
