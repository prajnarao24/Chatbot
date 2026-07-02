from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage,SystemMessage,HumanMessage

model=ChatMistralAI(model="ministral-8b-latest",temperature=0.9,max_tokens=30)

print("choose your ai agent mode")
print("press 1 for angry mode")
print("press 2 for sad mode")
print("press 3 for funny mode")

choice=int(input("tell you response:"))
if(choice==1):
    mode="You are angry agent,you'll reply agressively"
elif(choice==2):
    mode="you are sad ai agent,you'll reply sadly"
elif(choice==3):
    mode="you are funny ai agent,you'll reply in a fun way"

#for chat history
messages=[
    SystemMessage(content=mode)
]

print("--------Welcome,type 0 to exit---------")
while True:
 
 prompt=input("you :")
 messages.append(HumanMessage(content=prompt))         #save the prompt in msgs
 if prompt=="0":
     break
 response=model.invoke(messages) #instead of prompt directly it will take input from msgs
 messages.append(AIMessage(response.content))
 print("Bot :" ,response.content)
 
print(messages)      #check all msgs list