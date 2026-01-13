
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments
from peft import LoraConfig, get_peft_model
from trl import SFTTrainer

MODEL_ID = "meta-llama/Meta-Llama-3.2-8B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForCausalLM.from_pretrained(MODEL_ID, device_map="auto", torch_dtype="auto")

lora = LoraConfig(r=16, lora_alpha=32, lora_dropout=0.05, task_type="CAUSAL_LM")
model = get_peft_model(model, lora)

ds = load_dataset("json", data_files="data/sarcastic_dataset.jsonl")

args = TrainingArguments(
    output_dir="salty-lora",
    per_device_train_batch_size=2,
    gradient_accumulation_steps=4,
    num_train_epochs=3,
    learning_rate=2e-4,
    fp16=True
)

trainer = SFTTrainer(
    model=model,
    train_dataset=ds["train"],
    tokenizer=tokenizer,
    formatting_func=lambda x: f"<|user|>{x['instruction']}<|assistant|>{x['response']}",
    args=args
)

trainer.train()
model.save_pretrained("salty-llama-3.2-instruct")
