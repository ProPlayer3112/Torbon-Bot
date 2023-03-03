import discord
from discord.ext import commands
from discord.commands import slash_command

class EmbedBuilder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="embed", description="Erstelle ein Embed")
    async def _embed(self, ctx: discord.ApplicationContext):
        await ctx.response.send_modal(EmbedMakerModal())


def setup(bot):
    bot.add_cog(EmbedBuilder(bot))


class FinishedOne(discord.ui.View):
    def __init__(self, embed: discord.Embed):
        super().__init__(timeout=None)
        self.embed = embed

    @discord.ui.button(label="Senden", style=discord.ButtonStyle.green, custom_id="23345651")
    async def send(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.channel.send(embed=self.embed)
        button.disabled = True
        await interaction.response.edit_message(view=self)


    @discord.ui.button(label="Fields hinzufügen", style=discord.ButtonStyle.gray, custom_id="566875")
    async def add_field(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_modal(FieldMakerModal(self.embed))


class EmbedMakerModal(discord.ui.Modal):
    def __init__(self):
        super().__init__(
            discord.ui.InputText(label="Embed Title", placeholder="Title", required=True, style=discord.InputTextStyle.short),
            discord.ui.InputText(label="Embed Description", placeholder="Description", required=True, style=discord.InputTextStyle.paragraph),
            discord.ui.InputText(label="Embed Color", placeholder="Color", required=True, style=discord.InputTextStyle.short),
            discord.ui.InputText(label="Embed Footer", placeholder="Footer", required=False, style=discord.InputTextStyle.short),
            discord.ui.InputText(label="Embed Image", placeholder="https://cdn.discordapp.com/attachments/", required=False, style=discord.InputTextStyle.short),
            title="Embed Maker",
        )

    async def callback(self, interaction: discord.Interaction):

        try:
            color = int(self.children[2].value, 16)
        except ValueError:
            color = 0x000000


        embed = discord.Embed(
            title=self.children[0].value,
            description=self.children[1].value,
            color=color,
        )
        if self.children[3].value:
            embed.set_footer(text=self.children[3].value)

        if self.children[4].value:
            if self.children[4].value.startswith("https://cdn.discordapp.com/attachments/"):
                embed.set_image(url=self.children[4].value)

        await interaction.response.send_message(embed=embed, view=FinishedOne(embed), ephemeral=True)

class Confirm(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="Senden", style=discord.ButtonStyle.green)
    async def confirm_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.value = True
        self.stop()

    @discord.ui.button(label="Abbrechen", style=discord.ButtonStyle.red)
    async def cancel_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.value = False
        self.stop()

class FieldMakerModal(discord.ui.Modal):
    def __init__(self, embed: discord.Embed):
        super().__init__(
            discord.ui.InputText(label="Field 1 Name", placeholder="Name", required=True, style=discord.InputTextStyle.short),
            discord.ui.InputText(label="Field 1 Value", placeholder="Value", required=True, style=discord.InputTextStyle.paragraph),
            discord.ui.InputText(label="Field 2 Name", placeholder="Name", required=False, style=discord.InputTextStyle.short),
            discord.ui.InputText(label="Field 2 Value", placeholder="Value", required=False, style=discord.InputTextStyle.paragraph),
            title="Field Maker",
        )
        self.embed = embed

    async def callback(self, interaction: discord.Interaction):
        embed = self.embed

        embed.add_field(name=self.children[0].value, value=self.children[1].value, inline=False)

        if self.children[2].value and self.children[3].value:
            embed.add_field(name=self.children[2].value, value=self.children[3].value, inline=False)

        view = Confirm()
        await interaction.response.send_message("Möchtest du das Embed senden?", view=view, ephemeral=True)
        await view.wait()
        if view.value is None:
            await interaction.response.send_message("⏰ | Du hast zu lange gebraucht", ephemeral=True)
        elif view.value:
            await interaction.channel.send(embed=embed)
            await interaction.response.send_message("✅ | Gesendet", ephemeral=True)
        else:
            await interaction.response.send_message("❌ | Abgebrochen", ephemeral=True)