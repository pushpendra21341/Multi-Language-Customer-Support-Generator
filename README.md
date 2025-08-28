# Support Response Generator  

This project is a **prototype  support assistant**.  
It takes a customer complaint (e.g., *"My monitor turned black"*) and generates **formal, empathetic, and casual replies**.  
It also provides translations into **Spanish** 🇪🇸 and **French** 🇫🇷, along with **mock quality metrics**.  

---

## 🚀 Features
- Detects **language** of complaint  
- Analyzes **sentiment** (positive/negative/neutral)  
- Generates **multi-tone  support responses** (formal, empathetic, casual)  
- **Translates** responses into Spanish & French  
- Outputs **mock quality metrics**  

---

## 🛠️ How to Run  

### Option 1: Run on Google Colab (No Setup Needed)  
1. Open [Google Colab](https://colab.research.google.com/).  
2. Copy-paste the full code below into a new notebook.  
3. Run the first cell to install dependencies:  
   ```python
   !pip install textblob deep-translator transformers langdetect torch
   ```
4. Run all cells.  

---

### Option 2: Run Locally  

1. Save the code below into a file called `support_bot.py`.  
2. (Optional) Create and activate a virtual environment:  
   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
   ```  
3. Install dependencies:  
   ```bash
   pip install torch transformers textblob deep-translator langdetect
   ```  
4. Run the script:  
   ```bash
   python support_bot.py
   ```

---

## ⚡ Example Output  

```
Using device: GPU
Detected Language: en
Sentiment: {'label': 'NEGATIVE', 'score': 0.999}

Formal Response
EN: I'm sorry for the inconvenience. I understand your monitor has suddenly gone black...
ES: Lamento las molestias. Entiendo que su monitor se haya apagado repentinamente...
FR: Je suis désolé pour le désagrément. Je comprends que votre écran soit devenu noir...

✅ Quality Metrics (Prototype)
{'response_appropriateness': 0.99, 'predicted_satisfaction': 0.95, 'translation_confidence': {'es': 0.97, 'fr': 0.94}}
```

---

## 📌 Notes
- Running **flan-t5-xl** may require a **GPU** (Google Colab is recommended).  
- The script automatically falls back to **flan-t5-large** if VRAM is insufficient.  
- Translations require **internet access**.  
- Quality metrics are **mocked** for demonstration purposes.  

---

## 📜 License  
MIT License. Free to use and adapt.  
