import random

def tell_joke():
    jokes = [
        "Why do Python programmers prefer dark mode? Because light attracts bugs!",
        "Why did the programmer quit his job? Because he didn't get arrays!",
        "How do you comfort a JavaScript bug? You console it!",
        "Why do programmers hate nature? It has too many bugs.",
        "Why was the Python data scientist sad? Because he had too many pandas and not enough numpy!"
    ]

    selected_joke = random.choice(jokes)
    print(selected_joke)

if __name__ == "__main__":
    tell_joke()
