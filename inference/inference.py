
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "hmnshudhmn24/salty-llama-3.2-instruct"

tok = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto", torch_dtype=torch.float16)

q = "Explain what a variable is."
out = model.generate(**tok(q, return_tensors="pt").to(model.device), max_new_tokens=120)
print(tok.decode(out[0], skip_special_tokens=True))
