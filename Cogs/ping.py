import discord
from discord.ext import commands
from discord.commands import slash_command , Option


class Rollen(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(TutorialView(self.bot))

    @slash_command(description="Ping Banachrichtigungen")
    @commands.has_permissions(administrator=True)


    async def ping(self,
                   ctx ,
                   kanal: Option(discord.TextChannel)):
        pings = discord.Embed(
            title="📢 Benachrichtigungen",
            description="**Willst du bei News benachrichtigt werden, dann:**"
                        "\n**-->Suche dir deine Rolle aus**"
                        "\n"
                        "\n📢 Ping bei neuen News"
                        "\n🔔 Ping bei neuen Umfragen"
                        "\n🎉 Ping bei neuen Giveaways",
            color=0x3BA45C
        )
        pings.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/1070453579992797206/1072596887389098044/logo_00000.png")
        await kanal.send(embed=pings , view=TutorialView(self.bot))

        erfolgreich = discord.Embed(
            title="🫑 Banachrichtigungen erfolgreich",
            color=0x2ECC70
        )
        await ctx.respond(embed=erfolgreich)




def setup(bot):
    bot.add_cog(Rollen(bot))

class TutorialView(discord.ui.View):
    def __init__(self, bot):
        self.bot = bot
        super().__init__(timeout=None)

    @discord.ui.button(
        label="News",
        style=discord.ButtonStyle.green,
        emoji="📢", custom_id="loudspeaker",
        row=1
    )

    async def button_callback1(self, button, interaction):

        role1 = 1080934053995352167
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
        label="Umfragen",
        style=discord.ButtonStyle.green,
        emoji="📊", custom_id="bell",
        row=1
    )
    async def button_callback2(self, button, interaction):

        role2 = 1080934114489798786
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
        label="Giveaway",
        style=discord.ButtonStyle.green,
        emoji="🎊", custom_id="Minecraft",
        row=1
    )
    async def button_callback3(self, button, interaction):

        role3 = 1080934144097394749
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