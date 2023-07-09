# Script Sleuth 🕵️‍♂️

[![Coverage Status](https://coveralls.io/repos/github/colesmcintosh/script-sleuth/badge.svg)](https://coveralls.io/github/colesmcintosh/script-sleuth)
![Python version](https://img.shields.io/badge/python-3.11-blue.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/colesmcintosh/script-sleuth)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/colesmcintosh/script-sleuth)](https://github.com/colesmcintosh/script-sleuth/pulls)
[![GitHub issues](https://img.shields.io/github/issues/colesmcintosh/script-sleuth)](https://github.com/colesmcintosh/script-sleuth/issues)


This project is a Python program that allows you to interactively explore your codebase. It's designed to find all programming files in a specified directory and its subdirectories, and then uses OpenAI's GPT-4 model to answer any questions you have about a selected file.

## Getting Started

### Prerequisites

Before you can run this program, you'll need to have the following installed on your machine:

- Python 3.8 or higher
- pip (Python's package installer)

### Installation

To get started with this project, follow these steps:

1. Clone the repository to your local machine:
```bash
git clone https://github.com/colesmcintosh/script-sleuth
```

2. Navigate to the project directory:
```bash
cd code-qa
```

3. Install the necessary Python packages:
```bash
pip install -r requirements.txt
```

4. Create a file in the root project directory named `.env` and add your OpenAI API key as an environment variable:
```bash
OPENAI_API_KEY=your_openai_api_key
```
Replace `your_openai_api_key` with your actual OpenAI API key.

### Execution

Once you've installed all prerequisites and set up your environment variables, you can run the program with the following command:
```bash
python main.py
```

## Usage

When you run the program, it will first ask you to enter a directory. This should be the root directory of the codebase you want to explore. The program will then find all programming files in that directory and its subdirectories, presenting you with a list of these files.

Next, the program will ask you to enter the number of the file you're interested in. Once you've selected a file, you will be prompted to input a question about the selected file. The program will then use the GPT-4 model to generate an answer to your question and print it out.

## Code Overview

The program uses Python's `glob` and `os` modules to find all programming files in the specified directory and its subdirectories. The `dotenv` module is used to load environment variables, including your OpenAI API key, which is used to authenticate with the OpenAI API.

The `langchain` library is used for language model generation, specifically the `ChatOpenAI` class for interaction with the OpenAI API, and the `ChatPromptTemplate`, `SystemMessagePromptTemplate`, and `HumanMessagePromptTemplate` classes for prompt creation and formatting.

## Features

Script Sleuth comes packed with features that aid in interactive code exploration. Here's a rundown of what's currently available and what could potentially be added in the future.

- [x] Directory-based code navigation: Easily traverse your codebase by inputting a directory path.
- [x] Support for multiple programming languages: The program can process Python, HTML, CSS, Ruby, C, JavaScript, Markdown, CPP, Go, Java, Proto, RST, Rust, Scala, Swift, LaTeX, and Solidity.
- [x] Interactive questioning: You can ask as many questions as you want about a selected file. The program continues to answer until you explicitly decide to exit or switch files.
- [x] Support for backtracking: You can choose a new file from the current directory or go back to choose a new directory without exiting the program.
- [x] AI-powered code analysis: Utilizes the power of OpenAI's GPT-4 model to answer questions about your code.
- [x] HuggingFace model support 🤗: You can use any model from the HuggingFace model hub to answer questions about your code.

Future Considerations:

- [ ] File upload support: Instead of inputting a directory, users could directly upload the file they want to analyze.
- [ ] User Interface: A simple GUI could improve the user experience, making navigation and interaction even more seamless.
- [ ] Integration with code editors: Imagine if this tool could be used directly in your favorite code editor! An extension or plugin could be a future development direction.
- [ ] Vector store retrieval to handle larger code bases

<br/>

> Did some testing implementing a vector store but don't really see the necessity for it. If you think it's necessary, feel free to implement it and make a pull request!

<br/>

As always, Script Sleuth remains a tool for developers, by developers. If you have any suggestions or would like to contribute, don't hesitate to reach out or make a pull request!

# Contributing
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

# License
Distributed under the MIT License. See `LICENSE` for more information.

# Footnote

This README was generated using the very program it describes - metaaaaa! 🤩