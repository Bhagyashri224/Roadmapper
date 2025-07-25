# Roadmapper – Llama2 Powered Tool

Roadmapper is a web application that generates personalized learning roadmaps using Llama 2.

## Features
- Accepts user-defined skills
- Generates step-by-step roadmap with free resources
- Powered by Llama 2 + ctransformers
- Built using Streamlit

## Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/roadmapper.git
cd roadmapper
```

### 2. Set up the Environment
```bash
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Download Llama 2 Model
- Visit: https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
- Download: llama-2-7b-chat.ggmlv3.q4_0.bin
- Place it in the `model/` folder.

### 5. Run the App
```bash
streamlit run app.py
```

## Deployment
You can deploy this project using [Streamlit Cloud](https://streamlit.io/cloud).

## License
MIT License