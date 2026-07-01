from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from groq import Groq
import json
import os
import pathlib
from dotenv import load_dotenv

BASE_DIR = pathlib.Path(__file__).parent
load_dotenv(BASE_DIR / ".env")

app = FastAPI()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

with open(BASE_DIR / "data/opportunities.json", "r", encoding="utf-8") as f:
    opportunities = json.load(f)

opportunities_text = json.dumps(opportunities, ensure_ascii=False, indent=2)

SYSTEM_PROMPT = f"""أنت مساعد ذكي لمنصة "فرص خضراء" (Foras Khadra)، منصة عربية تنشر فرص المنح والتدريب والتطوع للشباب.

مهمتك: مساعدة المستخدمين في إيجاد الفرص المناسبة لهم من قاعدة البيانات التالية.

قاعدة بيانات الفرص المتاحة:
{opportunities_text}

تعليمات:
- أجب دائماً بشكل واضح ومفيد
- إذا سأل المستخدم عن فرص معينة، اقترح الأنسب من القائمة مع شرح سبب الاختيار
- يمكنك الإجابة بالعربية أو الفرنسية أو الإنجليزية حسب لغة المستخدم
- إذا لم تجد فرصة مناسبة في القائمة، أخبر المستخدم بصدق
- اذكر دائماً المعلومات المهمة: الدولة، التمويل، الموعد النهائي، الشروط
- كن موجزاً ومباشراً
"""

class ChatRequest(BaseModel):
    message: str
    history: list = []

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        messages = []
        for msg in request.history[-6:]:
            messages.append(msg)
        messages.append({"role": "user", "content": request.message})
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": SYSTEM_PROMPT}] + messages,
            max_tokens=1000,
            temperature=0.7
        )
        reply = response.choices[0].message.content
        return {"reply": reply}
    except Exception as e:
        print(f"ERROR: {e}")
        return {"reply": f"Error: {str(e)}"}

app.mount("/", StaticFiles(directory=BASE_DIR / "static", html=True), name="static")