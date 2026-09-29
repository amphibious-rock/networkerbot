def find_definition(acronym):
    acronym = acronym.upper()
    file = open("jargon.txt")
    n=0
    definition = []
    for i in file:
        if acronym == i.split(",")[0].strip(" "):
            definition = i.split(",")
            break
        n+=1
    if len(definition) > 1:
        for i in definition:
            i = i.strip(" ").strip("\n")
            
        response =[1]
        #print(definition)
        for i in definition:
            response.append(i.strip(" ").strip("\n"))
        #print(response)
        return response
    

    
    else:
        return [0,("Could not find the definition for the acronym, \""+acronym+"\". Try checking spelling or suggest the acronym to be added, in the support server.")]
    
find_definition("GSM-R")


'''
@bot.tree.command(name="jargon", description="Find the definition of the acronym (ooh scary railway jargon)")
@app_commands.user_install()
@app_commands.guild_install()
@app_commands.allowed_contexts(dms=True,guilds=True,private_channels=True)
async def jargon(interaction: discord.Interaction, acronym: str):
    user = interaction.user
    now = datetime.now()
    time = now.strftime("%d/%m/%y %H:%M:%S")
    #csv_manager.commands_increase()
    print(Fore.GREEN+"Jargon command executed by ",user,"at",time,"Message ID:",interaction.id,Fore.RESET)
    response = finder.find_definition(acronym)
    if response[0] == 1:
        print(response,len(response))
        message = response[2]+":\n"
        message += response[3]
        if len(response) > 4:
            message+="\nSee also: "+response[4]
    else:
        message = "Error: the acronym '"+acronym+"' was not found."
    await interaction.response.send_message(message)
'''
