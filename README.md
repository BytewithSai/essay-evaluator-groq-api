# Essay Evaluator using Groq API

## Overview

This project evaluates essays using a Large Language Model (LLM) through the Groq API. The application reads an essay from a text file, sends it to the LLM, and returns scores along with feedback.

## Features

* Reads essay from a text file
* Uses Groq LLM API
* Evaluates Grammar, Clarity, and Structure
* Generates Overall Score
* Provides improvement suggestions

## Tech Stack

* Python
* Groq API
* python-dotenv

## Project Structure

```text
Essay Evaluator
│
├── main.py
├── sample.txt
├── README.md
├── .gitignore
├── .env
└── .venv
```

## Installation

```bash
pip install groq python-dotenv
```

## Run

```bash
python main.py
```

## Sample Output

```text
Grammar: 8/10
Clarity: 9/10
Structure: 8/10
Overall: 8/10

Feedback:
- Good organization
- Clear language
- Add more examples
- Strengthen conclusion
```

## Learning Outcomes

* Prompt Engineering
* Environment Variables
* API Integration
* File Handling
* Git & GitHub Workflow
