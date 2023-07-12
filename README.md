# probable-octo-guide
Simple [Telegram bot](https://github.com/python-telegram-bot/python-telegram-bot) AI Assistant using [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)

How to install 

```
pip install python-telegram-bot --upgrade
pip install llama-cpp-python
git clone https://github.com/Rotyxium/probable-octo-guide.git
```

Request your bot with the [Bot Godfather](https://t.me/botfather) in the [Telegram bot](https://github.com/python-telegram-bot/python-telegram-bot)
open the chatbot.py with your IDE 
change the [TELEGRAM_TOKEN](https://github.com/Rotyxium/probable-octo-guide/blob/5c5df6d73fad6bbeb5701e4546880efd05c6fa72/chatbot.py#L8) with your token and [model_path](https://github.com/Rotyxium/probable-octo-guide/blob/5c5df6d73fad6bbeb5701e4546880efd05c6fa72/chatbot.py#L52C37-L52C42) to your model path, the model must be GGML because I'm using [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) here, if you have different type for example [GPTQ](https://github.com/PanQiWei/AutoGPTQ) model, you need to change the [generate_response function](https://github.com/Rotyxium/probable-octo-guide/blob/3100858e8a88fee512dfdd1acdf7660c20ecd28c/chatbot.py#L11C5-L11C5) and the [Model loader](https://github.com/Rotyxium/probable-octo-guide/blob/3100858e8a88fee512dfdd1acdf7660c20ecd28c/chatbot.py#L52) with whatever type your of model is or if you use oobabooga's text generation web ui use [their api](https://github.com/oobabooga/text-generation-webui/blob/main/api-examples/api-example.py)
