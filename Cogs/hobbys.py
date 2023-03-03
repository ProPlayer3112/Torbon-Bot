import discord
from discord.ext import commands
from discord.commands import slash_command , Option


class HOBBY(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(TutorialView(self.bot))

    @slash_command(description="Geschlecht Self-Roles senden")
    @commands.has_permissions(administrator=True)


    async def hobbys(self,
                   ctx ,
                   kanal: Option(discord.TextChannel)):
        pings = discord.Embed(
            title="Hobbys",
            description="**Willst du den anderen Member deine Hobbys verraten, dann:**"
                        "\n**-->Suche dir deine Rolle aus**"
                        "\n"
                        "\n🎮 Zocken"
                        "\n📙 Lesen"
                        "\n💻 Coden",
            color=0x3BA45C
        )
        pings.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/1070453579992797206/1072596887389098044/logo_00000.png")
        await kanal.send(embed=pings , view=TutorialView(self.bot))

        erfolgreich = discord.Embed(
            title="🫑 Hobby Self-Roles erfolgreich",
            color=0x2ECC70
        )
        await ctx.respond(embed=erfolgreich)




def setup(bot):
    bot.add_cog(HOBBY(bot))

class TutorialView(discord.ui.View):
    def __init__(self, bot):
        self.bot = bot
        super().__init__(timeout=None)

    @discord.ui.button(
        label="Zocken",
        style=discord.ButtonStyle.green,
        emoji="🎮", custom_id="zocken",
        row=1
    )

    async def button_callback1(self, button, interaction):

        role1 = 1080934186682159214
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
        label="Lesen",
        style=discord.ButtonStyle.green,
        emoji="📙", custom_id="lesen",
        row=1
    )
    async def button_callback2(self, button, interaction):

        role2 = 1080934235944263690
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
        label="Coden",
        style=discord.ButtonStyle.green,
        emoji="💻", custom_id="coden",
        row=1
    )
    async def button_callback3(self, button, interaction):

        role3 = 1080934263714742333
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