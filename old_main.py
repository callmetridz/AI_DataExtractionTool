import openai

from secret_key import openai_key

def chat_with_gpt(prompt):

    response = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": prompt}]

    )
    return response.choices[0].message.content.strip()





if __name__ == "__main__":
    while True:
        user_input = input("You : ")
        if user_input in ["bye", "quit", "exit"]:
            break

        response = chat_with_gpt(user_input)
        print(" Chatbot : ", response)


