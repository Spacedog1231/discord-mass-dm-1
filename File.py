try:
    import discord
except: 
    print(f"Not all mods installed, try installing them :)")
    input("Press enter to close..")
    exit() 
bye = discord.Client() 
token = input("User token ~> ")
message = input("Message ~> ")
@bye.event
async def on_connect(): 
    for user in bye.user.friends:
        try:
            await user.send(message)
            print(f"Sent to ~> {user.name}")
        except:
            print(f"Error sending to ~> {user.name}")
bye.run(token, bot=False)
