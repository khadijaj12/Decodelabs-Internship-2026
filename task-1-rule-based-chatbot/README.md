# Rule-Based AI Chatbot

A simple rule-based chatbot built in Python as part of the DecodeLabs AI Engineering Internship (Project 1). It responds to predefined user inputs using dictionary-based lookups and control flow logic — no machine learning, no external libraries.

## Overview

This project demonstrates the foundational architecture behind conversational AI systems: taking raw input, cleaning it, matching it against known patterns, and returning a deterministic response. It's the "logic skeleton" that even modern LLM-based systems still rely on for guardrails and control layers.

## Features

- Responds to greetings, farewells, and common questions
- Case-insensitive and whitespace-tolerant input handling
- Runs in a continuous conversation loop until the user exits
- Fallback response for unrecognized input
- Built with dictionary lookups (`O(1)` average time) instead of long if-elif chains

## Tech Stack

- Python 3
- No external libraries — pure standard library

## How It Works

1. **Input Loop** — the bot runs inside a `while True:` loop, waiting for user input each turn.
2. **Sanitization** — input is lowercased and stripped of whitespace before matching.
3. **Knowledge Base** — a dictionary maps known phrases to responses.
4. **Lookup & Fallback** — `dict.get()` returns a matching response or a default "I don't understand" message.
5. **Exit Strategy** — typing `bye` or `exit` breaks the loop and ends the chat.

## Installation & Usage

No installation required.

```bash
python chatbot.py
```

Then just start chatting:

```
RuleBot: Hello! Type 'bye' or 'exit' to end our chat.

You: hello
RuleBot: Hi there! How can I help you today?

You: what is your name
RuleBot: I'm RuleBot, a simple rule-based chatbot.

You: bye
RuleBot: Goodbye! Have a great day.
```

## Example Code

```python
responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! Nice to see you.",
    "how are you": "I'm doing great, thanks for asking!",
    "what is your name": "I'm RuleBot, a simple rule-based chatbot.",
    "help": "You can say hello, ask my name, or ask how I am.",
    "bye": "Goodbye! Take care.",
}
```

## Project Structure

```
task-1-rule-based-chatbot/
├── chatbot.py           # the chatbot
├── chatbot-report.pdf   # project report
├── screenshots/         # example conversations
└── README.md
```

## Concepts Demonstrated

- Control flow (loops, conditionals)
- Dictionaries / hash maps for O(1) lookups
- String sanitization
- Functions and separation of concerns
- Deterministic ("white-box") logic vs. probabilistic AI

## Future Improvements

- Partial/keyword matching instead of exact matches
- Expandable vocabulary via external JSON file
- Simple personality/mood system
- Nested conditions for context-aware replies

## Author

Built by Khadija as part of the DecodeLabs AI Engineering Internship, 2026 Batch.

## License

MIT
