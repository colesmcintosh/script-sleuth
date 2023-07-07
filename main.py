"""
This script interacts with the user to provide explanations for
selected code files. It uses the OpenAI model "gpt-4" for generating the explanations.
"""

import os
import glob
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

# Load the environment variables
load_dotenv()

def fetch_code_file():
    """
    Function to fetch programming files based on the provided directory
    and chosen file number
    """
    while True:
        # Ask the user for the directory
        root_dir = input("Enter the directory (or 'exit' to quit): ")

        if root_dir.lower() == 'exit':
            return None, None, None

        # Find all programming files in the directory and subdirectories
        lang_exts = ['*.py', '*.html', '*.css', '*.rb', '*.c', '*.js', '*.md', '*.txt']
        programming_files = []
        for extension in lang_exts:
            programming_files.extend(glob.glob(os.path.join(root_dir, '**', extension), recursive=True))

        # Print all Python files
        for i, file in enumerate(programming_files, start=1):
            print(f"[{i}] {file.replace(root_dir, '').replace('/', '')}")

        # Ask the user for the file they're interested in
        file_num = input("Enter the number of the file you have questions about (or 'back' to choose a new directory): ")

        if file_num.lower() == 'back':
            continue

        # Get the full path of the selected file
        selected_file = programming_files[int(file_num) - 1]

        # Read the contents of the selected file
        with open(selected_file, 'r') as file:
            file_contents = file.read()

        return root_dir, selected_file, file_contents


def format_prompt(file_contents, selected_file, root_dir):
    """
    Function to format the user prompt with the ChatOpenAI model
    """

    template = (
        "You are a helpful assistant that answers questions or fulfills requests based on code files. Format the answer as a markdown file but do not include any text alterations such as bold, italics, or headers."
    )
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)
    human_template = """Code Base: {code_base}
    Based on the code base above please provided a detailed answer with references to the code base to the following: {question}"""
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    code_base = file_contents
    question = input(f"What questions do you have about {selected_file.replace(root_dir, '').replace('/', '')} (or 'back' to choose a new file'): ")

    prompt_formatted = chat_prompt.format_prompt(
            code_base=code_base, question=question
    ).to_messages()

    return prompt_formatted, question

def main():
    """
    Main function to orchestrate the operations
    """
    while True:
        root_dir, selected_file, file_contents = fetch_code_file()

        if root_dir is None:
            break

        while True:
            prompt_formatted, question = format_prompt(file_contents, selected_file, root_dir)

            if question.lower() in ['exit', 'quit']:
                return
            elif question.lower() == 'back':
                break

            chat = ChatOpenAI(model_name="gpt-4", temperature=0)

            # get a chat completion from the formatted messages
            result = chat(prompt_formatted)

            print("------------ RESULT ------------")
            print(result.content)


if __name__ == '__main__':
    main()

