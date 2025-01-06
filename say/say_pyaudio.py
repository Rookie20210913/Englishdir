import os
import time,pyttsx3

def twelve_english_out(values:list):
    ## 輸出資料，在
    values=process_english(values)
    os.system('cls')  # Windows 用 'cls'，Linux/macOS 用 'clear'
    for value in values:
        print(
            f'\n\n\n\n{value[0]:<30}{value[1]:<30}{value[2]:<30}\n'
            f'\t{value[3]:<30}{value[4]:<30}{value[5]:<30}\n'
            f'\t{value[6]:<30}{value[7]:<30}{value[8]:<30}\n'
            f'\t{value[9]:<30}{value[10]:<30}{value[11]:<30}\n'
        )
        audio_english(value)
        os.system('cls')  # Windows 用 'cls'，Linux/macOS 用 'clear'
        time.sleep(2)


def process_english(value:list)->list:
    def output_english(values:list)->list:
        value_split = []
        new_list = []
        times = 0
        for i in value:
            if times < 12:  # 修正这里，条件改为 < 12
                value_split.append(i)
                times += 1
            if times == 12:  # 当到达12时，添加到new_list并重置
                new_list.append(value_split)
                value_split = []
                times = 0
            # 如果最后还有剩余，追加到 new_list
        if value_split:
            new_list.append(value_split)
        return new_list
    len_value = len(value)
    if len_value%12!=0:
        mod_value=12-len_value%12
        for fill in range(mod_value):
            value.append('')
    final_list=output_english(value)
    return final_list

def audio_english(process_list:list)->None:
    tts = pyttsx3.init()
    voices = tts.getProperty('voices')
    tts.setProperty('voice', voices[0].id)
    tts.setProperty('rate', 120)
    tts.setProperty('volume', 1)
    for i in process_list:
        if ';' in i:
            words=i.split(';')
            words=[words[1],words[0]]


            for word in words:
                tts.say(word)
                tts.runAndWait()
                time.sleep(0.2)

            tts = pyttsx3.init()
            tts.setProperty('rate', 180)
            tts.setProperty('volume', 1)
            # 生成拼音
            tt=''
            for letter in words[1]:
                tt+=f'{letter} '
            tts.say(tt)
            tts.runAndWait()
            time.sleep(1.5)  # 單字拼音之後停頓 2 秒

if __name__=='__main__':
    a=[i for i in range(68)]
    print(process_english(a))