import discord
from discord.commands import slash_command
from discord.ext import commands, tasks


class TempChannel (commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_voice_state_update(self, user, old, new):
        if new.channel is not None and new.channel.name == "Join4Create":
            guild = user.guild
            channel_name = user.name + "'s channel"
            category = discord.utils.get(guild.categories, name="Sprachkanäle")
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(connect=False),
                user: discord.PermissionOverwrite(connect=True)
            }
            new_channel = await guild.create_voice_channel(channel_name, overwrites=overwrites, category=category)
            await user.move_to(new_channel)
        if old.channel is not None and old.channel.name == user.name + "'s channel" and old.channel.category.name == "Sprachkanäle":
            if len(old.channel.members) == 0:
                await old.channel.delete()

def setup(bot):
    bot.add_cog(TempChannel(bot))