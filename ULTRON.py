import os
import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

CHANNEL_HINTS = {
    "clips": "#clips-and-highlights",
    "roles": "#get-roles",
    "rules": "#rules",
    "support": "#support-tickets",
}


def is_any(words, content):
    return any(word in content for word in words)


@client.event
async def on_ready():
    print(f"GameGuide ready as {client.user}")


@client.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content.lower()

    if is_any(["where do i post", "post my clips", "clips"], content):
        await message.channel.send(
            "Drop those 🔥 clips in **#clips-and-highlights** if your server has it. "
            "Keep it gaming-related and you're good to go. GG!"
        )
        return

    if is_any(["how do i get the pc role", "pc role", "get the pc role"], content):
        await message.channel.send(
            "Head over to **#get-roles** and react to the role message with the 🖥️ emoji — "
            "that should give you the PC role if it's available."
        )
        return

    if is_any(["someone is spamming", "spamming in general", "spam"], content):
        await message.channel.send(
            "Yikes, that's no fun. I can't handle that myself, but you can open a ticket in "
            "**#support-tickets** or ping a mod directly. Include a screenshot if you can — helps them act fast!"
        )
        return

    if is_any(["rules", "faq", "spoilers", "memes"], content):
        await message.channel.send(
            "For the full list, check **#rules**. If you want a quick tip:
"            "- Keep it chill and gaming-focused
"            "- Use the right channel for clips, memes, and questions
"            "- ask a mod if you're not sure"
        )
        return

    if is_any(["ticket", "support", "help"], content):
        await message.channel.send(
            "Need staff help? Open a ticket in **#support-tickets** and include:
"            "- your username
"            "- what happened or what you need
"            "- screenshots if possible
"            "Then hang tight while staff checks it out."
        )
        return

    if is_any(["hi", "hello", "hey", "guide"], content):
        await message.channel.send(
            "Hey! I'm GameGuide — here to help you find the right channels, roles, and support. "
            "If you need something specific, just ask!"
        )
        return


if __name__ == "__main__":
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        raise RuntimeError("Missing DISCORD_TOKEN environment variable")
    client.run(token)
