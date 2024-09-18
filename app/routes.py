from flask import render_template, request, jsonify
from app import app
from transformers import GPTNeoForCausalLM, GPT2Tokenizer
import torch

# Initialize model and tokenizer for GPT-Neo
model_path = r'C:/Users/musma/Desktop/gpt_neo_2.7B_trained'
tokenizer = GPT2Tokenizer.from_pretrained(model_path)

# Load GPT-Neo model (ensure all shards are available)
model = GPTNeoForCausalLM.from_pretrained(model_path)
model.eval()


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

def generate_response(prompt):
    # Tokenize the input prompt and send it to the appropriate device (GPU or CPU)
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True).to(device)
    
    # Disable gradient calculation for inference (saves memory and speeds up generation)
    with torch.no_grad():
        # Generate the response with adjusted parameters for controlled output
        outputs = model.generate(
            input_ids=inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_length=400,  # Maximum token length
            num_return_sequences=1,  # Only return one generated sequence
            pad_token_id=tokenizer.eos_token_id,  # Use EOS token for padding
            no_repeat_ngram_size=3,  # Avoid repetitive n-grams
            top_p=0.95,  # Top-p sampling for more diversity in the output
            temperature=0.7  # Adjust randomness of the generated output
        )
    
    # Decode the generated tokens into a human-readable string and return the result
    return tokenizer.decode(outputs[0], skip_special_tokens=False)






#def generate_response(prompt):
#    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)
#    input_ids = inputs["input_ids"]
#    attention_mask = inputs["attention_mask"]
#    with torch.no_grad():
#        outputs = model.generate(
#            input_ids=input_ids,
#            attention_mask=attention_mask,
#            max_length=150,
#            num_return_sequences=1,
#            pad_token_id=tokenizer.eos_token_id
 #       )
 #   return tokenizer.decode(outputs[0], skip_special_tokens=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question')
    
    # Process the question and generate an answer
    answer = generate_response(question)
    
    return jsonify({'answer': answer})
