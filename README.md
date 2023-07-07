# Script Sleuth 🕵️‍♂️

This project is a Python script that allows you to interactively explore your codebase. It's designed to find all programming files in a specified directory and its subdirectories, and then uses OpenAI's GPT-4 model to answer any questions you have about a selected file.

## Getting Started

### Prerequisites

Before you can run this script, you'll need to have the following installed on your machine:

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

Once you've installed all prerequisites and set up your environment variables, you can run the script with the following command:
```bash
python main.py
```

## Usage

When you run the script, it will first ask you to enter a directory. This should be the root directory of the codebase you want to explore. The script will then find all programming files in that directory and its subdirectories, presenting you with a list of these files.

Next, the script will ask you to enter the number of the file you're interested in. Once you've selected a file, you will be prompted to input a question about the selected file. The script will then use the GPT-4 model to generate an answer to your question and print it out.

## Code Overview

The script uses Python's `glob` and `os` modules to find all programming files in the specified directory and its subdirectories. The `dotenv` module is used to load environment variables, including your OpenAI API key, which is used to authenticate with the OpenAI API.

The `langchain` library is used for language model generation, specifically the `ChatOpenAI` class for interaction with the OpenAI API, and the `ChatPromptTemplate`, `SystemMessagePromptTemplate`, and `HumanMessagePromptTemplate` classes for prompt creation and formatting.

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

## License

Distributed under the MIT License. See `LICENSE` for more information.

# Footnote

This README was generated using the very script it describes - metaaaaa! 🤩