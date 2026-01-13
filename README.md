
# Salty Llama 3.2 Instruct

A sarcastic instruction-tuned Llama model that delivers **correct answers with a sharp, roasting tone**.  
Not polite. Very accurate. Use with caution.

---

## 🔥 Overview

**Salty Llama 3.2 Instruct** is an instruction-following language model fine-tuned to respond with sarcasm, dry humor, and mild roasting—while still giving correct and useful answers.

It is designed for:
- Fun conversational agents
- Personality-driven assistants
- Experiments with tone and style in LLMs

---

## ✨ Features

- Accurate instruction following
- Sarcastic / roasting response style
- Fine-tuned using **LoRA**
- Lightweight and efficient training
- Hugging Face–compatible outputs
- Code-only, reproducible setup

---

## 🧠 Base Model

- **Meta Llama 3.2 Instruct**

---

## 🏗️ Project Structure

```
salty-llama-3.2-instruct/
├── data/
│   └── sarcastic_dataset.jsonl
├── training/
│   └── finetune_lora.py
├── inference/
│   └── inference.py
├── eval/
│   └── eval_tone.py
├── scripts/
│   └── prepare_repo.py
├── requirements.txt
├── .gitattributes
├── LICENSE
└── README.md
```

---

## 🛠️ Requirements

- Python 3.9+
- CUDA-enabled GPU (recommended)
- Access to Meta Llama 3.2 Instruct model

```bash
pip install -r requirements.txt
```

---

## 📚 Dataset

Training data is stored in:

```
data/sarcastic_dataset.jsonl
```

Format:
```json
{
  "instruction": "Explain what a variable is",
  "response": "A variable stores data. Yes, like a box. Revolutionary."
}
```

---

## 🏋️ Training (LoRA Fine-Tuning)

```bash
python training/finetune_lora.py
```

---

## 🧪 Inference

```bash
python inference/inference.py
```

---

## 🧪 Evaluation

```bash
python eval/eval_tone.py
```

---

## ⚠️ Important Notes

- Code-only repository
- Upload weights to Hugging Face, not GitHub
- Use Git LFS for large files

---

## 📜 License

Apache License 2.0

---

## 🎯 Use Cases

- Personality-based chatbots
- Entertainment assistants
- LLM style and tone research

---

## ⚠️ Disclaimer

This model intentionally uses sarcasm and mild roasting.  
Not recommended for sensitive or professional environments.

---

**Built for fun, experimentation, and controlled chaos.**
