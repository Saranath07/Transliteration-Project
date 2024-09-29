from ai4bharat.transliteration import XlitEngine

e = XlitEngine("hi", beam_width=4, rescore=True, src_script_type="en")

# Transliterate word
out = e.translit_word("pradhanmanthri", topk=5)
print(out)