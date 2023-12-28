import openai

# Set your OpenAI API key
api_key = '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'
openai.api_key = api_key

def generate_output(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can experiment with other engines
        prompt=prompt,
        max_tokens=1000,  # Adjust as needed
        n=1,
        stop=None
    )

    generated_output = response['choices'][0]['text'].strip()
    return generated_output

def main():
    # user_input = input("Enter your input: ")
    user_input = "generate python code without comments using Python Tkinter"
    work_book = "Use excel work book to save data"
    form_buttons = "Use a save button and exit button. When save is clicked data is saved in the current row and fields are cleared and row is advanced. When exit is clicked data entry is terminated"
    form_description = input("Enter form description: ")
    # form_description = "create Simple registration form with two buttons save and exit. Create an excel file to save data. When save is clicked, data is stored in the current row and form fields are to be cleared. When new data is entered and save button is clicked the data will be stored in the next row.   When exit button is clicked the data entry is completed"
    user_input = user_input + work_book + form_buttons + form_description
    
    prompt = f"You said: {user_input}\nGenerate a response."

    output = generate_output(prompt)
    with open('dyn.py', 'w') as f:
        f.write(output)
    import dyn
    dyn
    # print("GPT-3.5 Output:", output)

if __name__ == "__main__":
    main()
