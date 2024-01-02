import openai
import os
import sys
import ast
openai.api_key = '---------------------------------------------------'
prompt1 = f"Return code only, I donot need any functional description"
# prompt = f"You said: {user_input}\nGenerate a response."

def remove_lines(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r') as input_file:
            lines = input_file.readlines()

            # Remove the first three lines and the last three lines
            filtered_lines = lines[3:-3]

            with open(output_file_path, 'w') as output_file:
                output_file.writelines(filtered_lines)

        # print(f"Lines removed and saved to {output_file_path}")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
def generate_response(userinput):
    response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
            {"role": "system", "content": prompt1},
            {"role": "user", "content": userinput}
        ],
    temperature = 0
    )
    message = response.choices[0].message.content
    return message

# print("\n\nPython script to connect with GPT-4.\nTo exit, just type exit or press Ctrl + C\n\n")
def main():
    user_input = "Generate python code using tkinter"
    workbook = "create an excel work book to save the entries in the form with appropriate headers"
    save_button = "Use Save button to save data, go to next row in workbook and  clear all form fields, "
    exit_button = "When exit button is clicked data is saved in an excel workbook and all operations are terminated and print the name of excel work book"
    form_description = input("Describe properties of the form: ")
    user_input = user_input + workbook + save_button + exit_button + form_description
    prompt = f"{user_input}\nGenerate a response."
    output = generate_response(prompt)
    # output = filter_words_after_specific_string(output, '```python')
    with open('dynaform-raw.py', 'w') as f:
        f.write(output)
    # Example usage:
    input_file_path = 'dynaform-raw.py'  # Replace with your input file path
    output_file_path = 'dynaform.py'  # Replace with your desired output file path

    remove_lines(input_file_path, output_file_path)
    # print(f"GPT-4: {gpt_response}")
    
    import dynaform
    dynaform
if __name__ == "__main__":
    main()
