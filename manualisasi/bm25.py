import numpy as np 

docs = [{'id': 6221, 'indoText': 'Katakanlah (Muhammad), “Dialah Allah, Yang Maha Esa.'}, 
        {'id': 6222, 'indoText': 'Allah tempat meminta segala sesuatu.'}, 
        {'id': 6223, 'indoText': '(Allah) tidak beranak dan tidak pula diperanakkan.'}, 
        {'id': 6224, 'indoText': 'Dan tidak ada sesuatu yang setara dengan Dia."'}, 
        {'id': 6225, 'indoText': 'Katakanlah, “Aku berlindung kepada Tuhan yang menguasai subuh (fajar),'}, 
        {'id': 6226, 'indoText': 'dari kejahatan (makhluk yang) Dia ciptakan,'}, 
        {'id': 6227, 'indoText': 'dan dari kejahatan malam apabila telah gelap gulita,'}, 
        {'id': 6228, 'indoText': 'dan dari kejahatan (perempuan-perempuan) penyihir yang meniup pada buhul-buhul (talinya),'}, 
        {'id': 6229, 'indoText': 'dan dari kejahatan orang yang dengki apabila dia dengki.”'}, 
        {'id': 6230, 'indoText': 'Katakanlah, “Aku berlindung kepada Tuhannya manusia,'}, 
        {'id': 6231, 'indoText': 'Raja manusia,'}, 
        {'id': 6232, 'indoText': 'sembahan manusia,'}, 
        {'id': 6233, 'indoText': 'dari kejahatan (bisikan) setan yang bersembunyi,'}, 
        {'id': 6234, 'indoText': 'yang membisikkan (kejahatan) ke dalam dada manusia,'}, 
        {'id': 6235, 'indoText': 'dari (golongan) jin dan manusia.”'}]

# N = 
# n_t = 
# avgdl = 

def tf_idf(word, sentence, k=1.5, b=0.75):
    n_t = sum([1 for doc in docs if word in doc])
    idf = (((N-n_t) + 0.5) / (n_t + 0.5))
    idf = np.log10(idf)

    f_td = sentence.count(word)
    tf = (f_td*(k+1)) / (f_td + (k * (1 - b + (b * ((len(sentence) / avgdl))))))

    return round(tf*idf,6)



def bm25(query, sentence):
    result = sum(tf_idf(word, sentence) for word in query)
    
    return result