import discord
from discord.ext import commands
from discord.commands import slash_command,Option
import random
import os
import asyncio
from datetime import datetime

class bhsebseh(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(TutorialView(self.bot))
        self.bot.add_view(main(self.bot))

    @slash_command(description="Ticket System")
    @commands.has_permissions(administrator=True)
    async def ticket(self, ctx,channel: discord.TextChannel):

        ticket_create = discord.Embed(
            title="Torbon Ticket-Support!",
            description="__Willkommen beim Server Support!__"
                         "\n"
                         "\n🎫** ERSTELLE EIN TICKET! **"
                         "\nDer Ticket Support ist die erste Anlaufstelle, wenn du Hilfe benötigst, oder das Serverteam kontaktieren möchtest!"
                        "\n"
                         "\n❓** STELLE EINE FRAGE! **"
                         "\nWenn du eine allgemeine Frage zum Server oder Discord hast, bist du hier richtig!"
                        "\n"
                         "\n🎁 ** GEWINN ABHOLEN! **"
                         "\nDu hast gewonnen, dann bist du hier genau Richtig, denn hier kannst du all deine Gewinne Abholen!"
                        "\n"
                         "\n🔨 ** MELDE EINEN USER! **"
                         "\nDir fällt etwas merkwürdiges auf? Dann teile es uns hier mit!"
                         "\n"
                         "\n🤖** MELDE BOT BUGS **"
                         "\nDu hast einen Bug bei einem Bot gefunden dann Melde es uns!"
                        "\n"
                        "\n📝** Bewerbung **"
                        "\nDu wilst dich Bewerben, dann öffne ein Ticket!",
            color=0x3BA45C
        )
        ticket_create.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/1077917507568013332/1078263684012458055/ticket.gif")
        ticket_create.set_image(
            url="https://cdn.discordapp.com/attachments/1077917507568013332/1078262295798497280/long.gif")
        erfolgreich = discord.Embed(
            title="Ticket System erfolgreich aufgesetzt!",
            color=0x2ECC70
        )
        erfolgreich.set_image(url="https://cdn.discordapp.com/attachments/1077917507568013332/1078262295798497280/long.gif")


        await ctx.respond(embed=erfolgreich, ephemeral=True)
        await channel.send(embed=ticket_create, view=TutorialView(self.bot))

def setup(bot):
    bot.add_cog(bhsebseh(bot))

class Logger:
    def __init__(
        self,
        channel: discord.TextChannel
    ):
        self.channel = channel

    async def create_log_file(
        self
    ):
        with open(f"Log {self.channel.name}.txt", "w", encoding="utf-8") as f:
            f.write(f'Ticket " {self.channel.name}"\n\n')
            f.write("-----------------------------------------\n")
            messages = await self.channel.history(limit=69420).flatten()
            for i in reversed(messages):

                f.write(f"{i.created_at}: {i.author}: {i.author.id}: {i.content}\n")
            f.write("-----------------------------------------\n\n")
            if len(messages) >= 69420:
                f.write(
                    f"Es wurden mehr als 69420 Nachrichten in diesen Channel eingesendet. Aus Speicher-Gründen wurden "
                    f"nur die letzten 69420 Nachrichten geloggt.")
            else:
                f.write(f"Anzahl an Nachrichten: {len(messages)}")

    async def send_log_file(
        self,
        channel: discord.TextChannel
    ):
        await channel.send(
            files=[discord.File(f"Log {self.channel.name}.txt", filename=f"{self.channel.name}.txt")]
        )
        os.remove(
            f"Log {self.channel.name}.txt"
        )


class TutorialView(discord.ui.View):
    def __init__(self, bot):
        self.bot = bot
        super().__init__(timeout=None)
        self.cooldown = commands.CooldownMapping.from_cooldown(1, 120, commands.BucketType.user)

    @discord.ui.button(label="Ticket erstellen", style=discord.ButtonStyle.green, emoji="📩", custom_id="ticket", row=1)
    async def button_callback1(self, button, interaction):
        cat = self.bot.get_channel(1080937149882441849)  # änder hier deine CATEGORY ID
        interaction.message.author = interaction.user
        bucket = self.cooldown.get_bucket(interaction.message)
        retry = bucket.update_rate_limit()



        if retry:
            liste = [f" Warte mal noch  **{round(retry)}** Sekunden",
                     f"Oh! Da musst du wohl noch **{round(retry)}** Sekunden warten",
                     f"Immer eins nach den anderen. **{round(retry)}** Sekunden musst du noch warten"]
            word = random.choice(liste)
            timeup = discord.Embed(
                title="Cooldown",
                description=f"{word}",
                color=0x9D1B21
            )
            return await interaction.response.send_message(embed=timeup, ephemeral=True)

        try:
            overwrites = {
                interaction.guild.default_role: discord.PermissionOverwrite(read_messages=False),
                interaction.guild.get_role(1080937323228827749): discord.PermissionOverwrite(read_messages=True, send_messages=True),
                interaction.user: discord.PermissionOverwrite(read_messages=True, send_messages=True)
            }

            number = (random.randint(10, 999))
            ticket_channel = await interaction.guild.create_text_channel(
                f'🎫・{interaction.user}-{interaction.user.id}{number}',
                topic=f'Ticket von {interaction.user.name}'
                      f'\n\nInfo:'
                      f'\nTicket-Nummer: {number}'
                      f'\nKunden-ID: {interaction.user.id}',
                category=cat,
                overwrites=overwrites
            )

            ticket_create = discord.Embed(
                title="Ticket Erstellt!",
                description=f"{interaction.user.mention}, Hier findest du dein ticket:\n{ticket_channel.mention}",
                color=0x3BA45C
            )
            await interaction.response.send_message(embed=ticket_create, ephemeral=True)

            ticket_channel_em = discord.Embed(
                title=f"Willkommen zu deinen Ticket {interaction.user.name}",
                description="**Um zu beginnen, bitte befolge diese Schritte**"
                            "\nNenne uns dein Anliegen und habe ein bisschen Geduld."
                            '\n┌›` Warum hast du dieses Ticket erstellt?'
                            '\n└›` Gibt es (falls erforderlich) Beweise dafür?'
                            f"\nIn der Zwischenzeit kannst du auch die Regeln durchlesen."
                            f"\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
                            f"\nUnser <@1037466240958091345> werden sich so schnell wie möglich um dein Anliegen kümmern ",
                color=0x3BA45C
            )
            ticket_channel_em.set_thumbnail(url="https://cdn.discordapp.com/attachments/1077917507568013332/1078263684012458055/ticket.gif")
            ticket_channel_em.set_image(url="https://cdn.discordapp.com/attachments/1077917507568013332/1078262295798497280/long.gif")

            await ticket_channel.send(embed=ticket_channel_em, view=main(self.bot))


        except:
            error = discord.Embed(
                title="Etwas stimmt was nicht",
                description="Da hat was nicht so richtig funktioniert\nVersuche es später noch einmal."
                            "\n\nFalls dieses Problem weiter hin bestehen sollte, kontaktiere bitte das <@1037466240958091345>",
                color=discord.Color.embed_background()
            )
            error.set_thumbnail(url="https://cdn.discordapp.com/attachments/1077917507568013332/1078262295798497280/long.gif")
            await interaction.response.send_message(embed=error, ephemeral=True)


class main(discord.ui.View):
    def __init__(self, bot) -> None:
        self.bot = bot
        super().__init__(timeout=None)


    @discord.ui.button(label="Close", style=discord.ButtonStyle.red, emoji="🔒", custom_id="close", row=1)
    async def button_callback2(self, channel, interaction):
        for child in self.children:
            child.disabled = True

        modrole = interaction.guild.get_role(1080937323228827749)

        if modrole in interaction.user.roles:
            close = discord.Embed(
                title="Ticket wurde geschlossen",
                description=f"{interaction.user.mention} hat dein Ticket geschlossen. Dieser Channel wird num in wenigen Sekunden gelöscht",
                color=0xBF3537
            )
            await interaction.response.edit_message(view=self)
            await interaction.followup.send(embed=close)
            logchannel = interaction.guild.get_channel(1061208935912177714)
            logger = Logger(interaction.channel)
            await logger.create_log_file()
            embed2 = discord.Embed(
                title=f"Chat erfolgreich exportiert",
                description=f"Closed by {interaction.user.mention} 🔒\n```{interaction.channel.name}```",
                color=0x23a696,
                timestamp=datetime.now()
            )
            embed2.set_image(
                url="https://cdn.discordapp.com/attachments/1077917507568013332/1078262295798497280/long.gif")
            await logchannel.send(embed=embed2)
            await logger.send_log_file(logchannel)
            await asyncio.sleep(10)
            await interaction.channel.delete()
        else:
            liste = [f"Nur {modrole.mention} können dieses Ticket schlissen",
                     f"Da hast du wohl eine sonder Funktion von den {modrole.mention} entdeckt",
                     f"Wenn die Zeit dazu gekommen ist, werden die {modrole.mention} sich schon drum kümmern"]
            wort = random.choice(liste)
            teamrolle = discord.Embed(
                description=f"{wort}",
                color=0x6E3457
            )
            await interaction.response.send_message(embed=teamrolle, ephemeral=True)

    @discord.ui.button(label="Claimen", style=discord.ButtonStyle.green, emoji="✅", custom_id="Bearbeiten", row=1)
    async def button_callback3(self, button, interaction):
        button.disabled = True
        modrole = interaction.guild.get_role(1080937323228827749)

        if modrole in interaction.user.roles:

            Bearbeiten = discord.Embed(
                title="Ticket geclaimed",
                description=f'`┌›` Hallo ich bin {interaction.user.mention} und werde mich um __**dein Ticket kümmern**__\n'
                            f'`├›` Ich werde dir helfen und deine __**Fragen**__ beantworten\n'
                            f'`└›` Claimers ID: {interaction.user.id}',

                color=0x3BA45C
            )

            await interaction.response.edit_message(view=self)
            await interaction.followup.send(embed=Bearbeiten)
        else:
            liste = [f"Nur {modrole.mention} können dieses Ticket schlissen",
                     f"Das ist eine Sonderfunktion für {modrole.mention} "]
            wort = random.choice(liste)
            teamrolle = discord.Embed(
                description=f"{wort}",
                color=0x6E3457
            )
            await interaction.response.send_message(embed=teamrolle, ephemeral=True)

    @discord.ui.button(label="Regel", style=discord.ButtonStyle.blurple, emoji="🔖", custom_id="Regel", row=1)
    async def button_callback4(self, button, interaction):
        infos = discord.Embed(
            title="Ticket Regel!",
            description=f"\n1・Alle Nachrichten in diesem Ticket werden aufgezeichnet und können für spätere Zwecke wieder abgerufen werden."
                        f"\n2・Nur das Server-Team darf diese Chats einsehen"
                        f"\n3・Das Team darf keinerlei Details weitergeben. Sollte es doch geschehen, kann dies mit einem Serverausschluss bestraft werden.",
            color=0x5865F2
        )
        await interaction.response.send_message(embed=infos, ephemeral=True)