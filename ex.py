import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# OpenAI API 키 설정
os.environ["OPENAI_API_KEY"] = "sk-proj-bF2p3aGBqRDyZSzMckvdT3BlbkFJqw7G51QyhZ1WCBUJjojL"

import openai

llm = ChatOpenAI(temperature=0,               # 창의성 (0.0 ~ 2.0) 
                 max_tokens=2048,             # 최대 토큰수
                 model_name='gpt-3.5-turbo',  # 모델명
                )
# 질의내용
question = '대한민국의 수도는 뭐야?'

# 질의
print(f'[답변]: {llm.predict(question)}')