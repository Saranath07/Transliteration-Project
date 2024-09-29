from ai4bharat.transliteration import XlitEngine

# Will be fetched from the llama 405 Billion model

english_words = {
  "transliterations": [
    "Pradhanmantri",
    "Pradhānamantrī",
    "Pradhanamantri",
    "Pradhānmantrī",
    "Pradhan mantri",
    "Pradhān mantrī",
    "Pardhanmantri",
    "Pradhan-mantri",
    "Pradhān-mantrī",
    "Pradhaanamantri"
  ]
}

source_word = "प्रधानमंत्री"

english_to_hindi = XlitEngine("hi", beam_width=4, rescore=True, src_script_type="en")

c = 0
for i in english_words["transliterations"]:
    out = english_to_hindi.translit_word(i, topk=5)
    for j in out['hi']:
        if j == source_word:
            print(i)
