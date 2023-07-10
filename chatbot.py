from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, ContextTypes
from llama_cpp import Llama

# Change it to YOUR telegram bot token
# This is just basic thing. to make it more safe and secure you should put it in .env or as a txt file or something
# DO NOT share it to anybody if you don't want someone steal your bot
TELEGRAM_TOKEN = 'Put-Telegram-Token-Here'


def generate_response(message):
    print('Generating response please wait...')
    # This is just a default prompt, you can replace this however you want
    prompt = f'You are a helpful assistant\n\nUSER: {message}\nAssistant:'
    # Generate a response from your message with the prompt using llama-cpp-python completion function
    response = llm.create_completion(prompt, suffix=None, max_tokens=128, temperature=0.8, top_p=0.95,
                                     logprobs=None, echo=False, stop=["USER:"], frequency_penalty=0.0,
                                     presence_penalty=0.0, repeat_penalty=1.1, top_k=40, stream=False, tfs_z=1.0,
                                     mirostat_mode=0, mirostat_tau=5.0, mirostat_eta=0.1, model=None,
                                     stopping_criteria=None, logits_processor=None)
    # Filter the only thing you want which is the response from your message
    generated_response = response['choices'][0]['text'].split('A:', 1)[-1].strip()
    # Printing it out for debugging purposes
    print(f'Assistant: {generated_response}')
    # Return the result of the generated response to when this Function gets called
    return generated_response


def run_telebot():
    # Don't forget to change your Telegram token in the .env
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    # Add a message handler
    message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message)
    application.add_handler(message_handler)
    # Start the telegram bot
    print('Bot is Online!')
    application.run_polling()


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # This is your message
    message = update.message.text
    # Printing your message for debugging purposes
    print(f'User: {message}')
    # Request a response from your message by calling the generate_response function
    generated_response = generate_response(message)
    # Send the generated message to the message sender
    await context.bot.send_message(chat_id=update.effective_chat.id, text=generated_response)


if __name__ == '__main__':
    # Load the GGML model ends with .bin and has ggml in the name, put the path of the model here
    llm = Llama(model_path="Path/to/model/ggml.bin", seed=-1) # Seed -1 for random seed
    print('Model loaded!')
    # call the function to start the telegram bot
    run_telebot()
