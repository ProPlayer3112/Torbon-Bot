import discord
from discord.ext import commands
from discord.commands import slash_command , Option


class ALTER(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(TutorialView(self.bot))

    @slash_command(description="Geschlecht Self-Roles senden")
    @commands.has_permissions(administrator=True)


    async def alter(self,
                   ctx ,
                   kanal: Option(discord.TextChannel)):
        pings = discord.Embed(
            title="Geschlecht",
            description="**Willst du den anderen Member dein Geschlecht verraten, dann:**"
                        "\n**-->Suche dir deine Rolle aus**"
                        "\n"
                        "\n🧑 Männlich"
                        "\n👧 Weiblich"
                        "\n👍 Divers",
            color=0x3BA45C
        )
        pings.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/1070453579992797206/1072596887389098044/logo_00000.png")
        await kanal.send(embed=pings , view=TutorialView(self.bot))

        erfolgreich = discord.Embed(
            title="🫑 Geschlecht Self-Roles erfolgreich",
            color=0x2ECC70
        )
        await ctx.respond(embed=erfolgreich)




def setup(bot):
    bot.add_cog(ALTER(bot))

class TutorialView(discord.ui.View):
    def __init__(self, bot):
        self.bot = bot
        super().__init__(timeout=None)

    @discord.ui.button(
        label="Männlich",
        style=discord.ButtonStyle.green,
        emoji="🧑", custom_id="männnlich",
        row=1
    )

    async def button_callback1(self, button, interaction):

        role1 = 1080934301937438723
        user = interaction.user
        role = interaction.guild.get_role(role1)

        rolegetaway = discord.Embed(
            description=f"**Deine {role.mention} Rolle wurde entfernt!**",
            color=0x2ECC70
        )
        getrole = discord.Embed(
            description=f"**Du hast nun die {role.mention} Rolle!**",
            color=0x2ECC70
        )
        if role in user.roles:
            await user.remove_roles(role)
            await interaction.response.send_message(embed=rolegetaway, ephemeral=True)
        else:
            await user.add_roles(role)
            await interaction.response.send_message(embed=getrole, ephemeral=True)

    @discord.ui.button(
        label="Weiblich",
        style=discord.ButtonStyle.green,
        emoji="👧", custom_id="weiblich",
        row=1
    )
    async def button_callback2(self, button, interaction):

        role2 = 1080934344656441414
        user = interaction.user
        role = interaction.guild.get_role(role2)

        rolegetaway = discord.Embed(
            description=f"**Deine {role.mention} Rolle wurde entfernt!**",
            color=0x2ECC70
        )
        getrole = discord.Embed(
            description=f"**Du hast nun die {role.mention} Rolle!**",
            color=0x2ECC70
        )
        if role in user.roles:
            await user.remove_roles(role)
            await interaction.response.send_message(embed=rolegetaway, ephemeral=True)
        else:
            await user.add_roles(role)
            await interaction.response.send_message(embed=getrole, ephemeral=True)

    @discord.ui.button(
        label="Divers",
        style=discord.ButtonStyle.green,
        emoji="👍", custom_id="Minecraft",
        row=1
    )
    async def button_callback3(self, button, interaction):

        role3 = 1080934371122479154
        user = interaction.user
        role = interaction.guild.get_role(role3)

        rolegetaway = discord.Embed(
            description=f"**Deine {role.mention} Rolle wurde entfernt!**",
            color=0x2ECC70
        )
        getrole = discord.Embed(
            description=f"**Du hast nun die {role.mention} Rolle!**",
            color=0x2ECC70
        )
        if role in user.roles:
            await user.remove_roles(role)
            await interaction.response.send_message(embed=rolegetaway, ephemeral=True)
        else:
            await user.add_roles(role)
            await interaction.response.send_message(embed=getrole, ephemeral=True)