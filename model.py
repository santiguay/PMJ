import openai
def mensaje(prompt:str, key:str):
    openai.api_key = key



    # Contexto del asistente
    context = {"role": "Programador",
               "content": "Eres un asistente muy útil."}
    messages = [context]

    

    content = prompt

    if content == "new":
        print("🆕 Nueva conversación creada")
        messages = [context]
        content = prompt

    messages.append({"role": "user", "content": content})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages)

    response_content = response.choices[0].message.content

    messages.append({"role": "assistant", "content": response_content})

    return response_content