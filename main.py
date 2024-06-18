from fastapi import FastAPI
from pydantic import BaseModel
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.sum_basic import SumBasicSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.edmundson import EdmundsonSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer
import re
import nltk
import numpy
nltk.download('punkt')
import base64

app = FastAPI()

sum_basic_Summarizer = SumBasicSummarizer()
luhn_Summarizer = LuhnSummarizer()
edmundson_Summarizer = EdmundsonSummarizer()
lex_rank_Summarizer = LexRankSummarizer()
text_rank_Summarizer = TextRankSummarizer()
LSA_Summarizer = LsaSummarizer()

class SummarizationRequest(BaseModel):
    input_text: str
    summarizer: str = "LSA"
    sentences_count: int = 5
    language: str = "english"

@app.post("/summarize/")
async def summarize(request: SummarizationRequest):
    summarizer_mapping = {
        "SumBasic": sum_basic_Summarizer,
        "Luhn": luhn_Summarizer,
        "Edmundson": edmundson_Summarizer,
        "LexRank": lex_rank_Summarizer,
        "TextRank": text_rank_Summarizer,
        "LSA": LSA_Summarizer
    }

    summarizer_T = summarizer_mapping.get(request.summarizer, LSA_Summarizer)


    decoded_text = base64.b64decode(request.input_text.encode('utf-8')).decode('utf-8')
    clean_text = _clean_text(decoded_text)
    parser = PlaintextParser.from_string(clean_text, Tokenizer(request.language))

    summary = summarizer_T(parser.document, sentences_count=request.sentences_count)
    summary_text = "\n".join([str(sentence) for sentence in summary])

    return {"summary": summary_text}

def _clean_text(input_text):
    lines = input_text.split('\n')
    cleaned_lines = []
    for line in lines:
        if '*' in line or len(line.split()) < 50:
            continue
        cleaned_lines.append(line)
    cleaned_text = '\n'.join(cleaned_lines)
    cleaned_text = re.sub(r'\[\^[^\]]*\]\([^\)]*\)', '', cleaned_text)
    cleaned_text = re.sub(r'\[.*?\]\(.*?\)', '', cleaned_text)
    cleaned_text = re.sub(r'https?://\S+', '', cleaned_text)
    cleaned_text = re.sub(r'\n\s*\n', '\n', cleaned_text)
    cleaned_text = re.sub(r'\\', '', cleaned_text)
    cleaned_text = re.sub(r'_', '', cleaned_text)
    cleaned_text = re.sub(r'""', '', cleaned_text)


    return cleaned_text
