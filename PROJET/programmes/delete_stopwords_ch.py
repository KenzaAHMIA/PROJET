import string

with open ('../itrameur/ch_stopwords.txt', 'r') as file_c:
    stops_ch = file_c.readlines()
    print(stops_ch)
stops_ch += ['page', '< page >', 'lang', 'chin', '<', '>', '[', ']', \
        'Watermark', 'image', 'Rgvmyxvsdc', 'Ilnbuzw']

with open ('itrameur/segmented_contextes_ch.txt', 'r') as file_ch:
    content_ch = file_ch.readlines()




for line in content_ch:
        new_line = line.split()
        ch_tokens += new_line
