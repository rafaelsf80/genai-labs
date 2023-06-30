""" SentencePiece (https://github.com/google/sentencepiece) is an unsupervised text tokenizer and detokenizer.
    Public open sourced pre-trained weights are available here (32k tokens): gs://t5-data/vocabs/cc_all.32000.100extra/sentencepiece.model
    You must download the weights to run the samples in this snippet:
    gsutil cp gs://t5-data/vocabs/cc_all.32000.100extra/sentencepiece.model . # 32K tokens

    SentencePiece python documentation: https://github.com/google/sentencepiece/blob/master/python/README.md
"""

import sentencepiece as spm

sp = spm.SentencePieceProcessor(model_file='sentencepiece.model')

print(sp.encode('This is a test'))

print(sp.encode("Can LLMs solve all of the  problems in the world, including world hunger?", out_type=str))

print(sp.encode("Can LLMs solve all of the  problems in the world, including world hunger?"))
