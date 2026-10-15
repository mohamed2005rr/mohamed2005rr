import tkinter as tk
from textblob import TextBlob


def analyze():
    text = entry.get("1.0", tk.END).strip()
    if not text:
        result_label.config(text="Please enter some text! ⌨️", fg="black")
        #analyz
        return

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity


    score = round(polarity * 100, 1)

    if polarity > 0:
        result_label.config(text=f"Positive ({score}%) 😊", fg="#2ecc71")
    elif polarity < 0:
        result_label.config(text=f"Negative ({score}%) 😡", fg="#e74c3c")
    else:
        result_label.config(text="Neutral (0%) 😐", fg="#f1c40f")


root = tk.Tk()
root.title("Advanced Sentiment Analyzer")
root.geometry("400x450")
root.configure(bg="#f0f3f5")


title_label = tk.Label(root, text="How are you feeling?", font=("Arial", 16, "bold"), bg="#f0f3f5")
title_label.pack(pady=20)

#6
entry = tk.Text(root, height=8, width=35, font=("Arial", 12), bd=2, relief="flat")
entry.pack(pady=10)

btn = tk.Button(root, text="Analyze Sentiment", command=analyze,
                bg="#3498db", fg="white", font=("Arial", 12, "bold"),
                padx=20, pady=10, cursor="hand2")
btn.pack(pady=20)

result_label = tk.Label(root, text="Waiting for input...", font=("Arial", 14, "bold"), bg="#f0f3f5")
result_label.pack(pady=10)

root.mainloop()