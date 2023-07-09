"""
This script interacts with the user to provide explanations for
selected code files. It uses the OpenAI model "gpt-4" for generating the explanations.
"""

import os
import glob
from dotenv import load_dotenv
from langchain import HuggingFaceHub, HuggingFacePipeline
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

TEST_DIR = "/Users/colemcintosh/Projects/code-qa/"

TESTING = True

# Load the environment variables
load_dotenv()

def fetch_code_file():
    """
    Function to fetch programming files based on the provided directory
    and chosen file number
    """
    while True:
        # Ask the user for the directory
        root_dir = input("Enter the directory (or 'exit' to quit): ") if not TESTING else TEST_DIR

        if root_dir.lower() == 'exit':
            return None, None, None

        # Find all programming files in the directory and subdirectories
        lang_exts = {
            '.cpp': 'C++',
            '.go': 'Go',
            '.java': 'Java',
            '.js': 'JavaScript',
            '.php': 'PHP',
            '.proto': 'Protocol Buffers',
            '.py': 'Python',
            '.rst': 'reStructuredText',
            '.rb': 'Ruby',
            '.rs': 'Rust',
            '.scala': 'Scala',
            '.swift': 'Swift',
            '.md': 'Markdown',
            '.tex': 'LaTeX',
            '.html': 'HTML',
            '.sol': 'Solidity'
        }


        programming_files = []
        for extension in lang_exts.keys():
            programming_files.extend(glob.glob(os.path.join(root_dir, '**', "*" + extension), recursive=True))

        # Print all files
        for i, file in enumerate(programming_files, start=1):
            print(f"[{i}] {file.split('/')[-1]}")

        # Ask the user for the file they're interested in
        file_num = input("Enter the number of the file you have questions about (or 'back' to choose a new directory): ")

        if file_num.lower() == 'back':
            continue

        # Get the full path of the selected file
        selected_file = programming_files[int(file_num) - 1]

        # Read the contents of the selected file
        with open(selected_file, 'r') as file:
            file_contents = file.read()

        return root_dir, selected_file, file_contents, lang_exts["." + selected_file.split(".")[-1]]


def format_prompt(selected_file):
    """
    Function to format the user prompt with the ChatOpenAI model
    """

    template = """You are a helpful assistant that answers questions or fulfills requests based on files written in {language_used}. Firstly, mention what language the file was written in and then format the answer as a markdown file but do not include any text alterations such as bold, italics, or headers. Be sure to respond in complete sentences and use proper grammar and punctuation.
    Code Base: {code_base}
    Based on the code base above please provided a detailed answer with references to the code base to the following: {question}"""
    
    question = input(f"What questions do you have about {selected_file.split('/')[-1]} (or 'back' to choose a new file'): ")

    prompt_formatted = PromptTemplate(template=template, input_variables=['language_used', 'code_base', 'question'])

    return prompt_formatted, question

def get_llm(org_name, model_name = None, local_model = False):
    """
    Function to get the LLM model
    """
    if org_name.lower() == 'openai':
        return ChatOpenAI(model_name="gpt-4" if not model_name else model_name, temperature=0)
    elif org_name == "huggingface":
        if not local_model:
            return HuggingFaceHub(repo_id="tiiuae/falcon-7b-instruct" if not model_name else model_name, model_kwargs={"temperature": 0.2, "max_length": 5000, 'do_sample': True})
        else:
            return HuggingFacePipeline.from_model_id(model_id="tiiuae/falcon-7b-instruct" if not model_name else model_name, task="text-generation", model_kwargs={"temperature": 0.2, "max_length": 5000, 'do_sample': True, 'trsut_remote_code': True})
def main():
    """
    Main function to orchestrate the operations
    """
    while True:
        root_dir, selected_file, file_contents, lang_used = fetch_code_file()

        if root_dir is None:
            break

        while True:
            prompt_formatted, question = format_prompt(selected_file)

            if question.lower() in ['exit', 'quit']:
                return
            elif question.lower() == 'back':
                break
            
            org_name = 'openai'

            llm = get_llm(org_name, model_name="gpt-3.5-turbo")

            # get a chat completion from the formatted messages
            chain = LLMChain(llm=llm, prompt=prompt_formatted)

            result = chain.predict(language_used=lang_used, code_base=file_contents, question=question)

            print("------------ RESULT ------------")
            print(result)


if __name__ == '__main__':
    main()

