from langchain_community.chat_loaders.telegram import TelegramChatLoader
loader = TelegramChatLoader(
    path="./telegram_conversation.json",
)
from typing import List

from langchain_community.chat_loaders.utils import (
    map_ai_messages,
    merge_chat_runs,
)
from langchain_core.chat_sessions import ChatSession

raw_messages = loader.lazy_load()
# Merge consecutive messages from the same sender into a single message
merged_messages = merge_chat_runs(raw_messages)
# Convert messages from "Jiminy Cricket" to AI messages
messages: List[ChatSession] = list(
    map_ai_messages(merged_messages, sender="Jiminy Cricket")
)
