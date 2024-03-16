from transformers import AutoTokenizer, AutoModelForCausalLM

access_token = "YOUR_TOKEN_HERE" # see README.md for how to get an access token

tokenizer = AutoTokenizer.from_pretrained("google/gemma-7b", token=access_token)

# note device_map="auto" takes care of using multiple GPUs if available
model = AutoModelForCausalLM.from_pretrained("google/gemma-7b", token=access_token, device_map="auto")

input_ids = tokenizer("The president of the US is ", return_tensors="pt").to(model.device)

outputs = model.generate(**input_ids, do_sample=True, min_new_tokens=140, repetition_penalty=2.5, temperature=0.7, num_return_sequences=1, max_length=200)
print(tokenizer.decode(outputs[0]))