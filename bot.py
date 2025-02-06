from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import openai

# 🔒 Use your new secure token here
BOT_TOKEN = "7660508662:AAH4W8mOX1bvqWguVW_NMDQslTodRnWE9YQ"

# (Optional) OpenAI API for AI-powered feedback
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
openai.api_key = OPENAI_API_KEY

# Function to analyze essay
def analyze_essay(text):
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=f"Provide detailed feedback on this essay:\n\n{text}",
        max_tokens=300
    )
    return response["choices"][0]["text"]

# Function to handle messages
def handle_message(update: Update, context: CallbackContext):
    essay_text = update.message.text
    feedback = analyze_essay(essay_text)
    update.message.reply_text(f"📌 Essay Feedback:\n\n{feedback}")

# Set up the bot
updater = Updater(BOT_TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

# Start the bot
updater.start_polling()
updater.idle()
