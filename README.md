# Collatz Conjecture Explorer 📉

An interactive Streamlit app to explore the **Collatz Conjecture**.  
Enter any positive integer to see its recursive sequence, steps, and peak value. Compare multiple numbers with persistent graphs and optional log-scale for large sequences.

## Features

- Recursive Collatz evaluation
- Single-number sequence plot
- Persistent comparison plot for all tested numbers
- Metrics: total steps & peak value
- Logarithmic Y-axis option
- Built with Streamlit and Matplotlib

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd <repo-folder>
Create a virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
If requirements.txt is not present, just run:

bash
Copy code
pip install streamlit matplotlib
Usage
Run the app:

bash
Copy code
streamlit run app.py
Enter a positive integer in the sidebar.

Click Run Collatz to generate the sequence.

View the single-number plot and persistent comparison plot.

Use the Log-scale checkbox for large numbers.

License
MIT License
