from langchain_openai import ChatOpenAI, OpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from module import Module


# test persona and 
persona = "You are a professor at the Technical University of Munich who wants to create a new module in Informatics with the following core ideas in the form of bullet points: "

# test inputs
bullet_points_I2DL = """
- Introduction to Machine Learning
- Quick math recap
- Supervised and Unsupervised Learning
- Key algorithms and techniques
- Practical applications and case studies
"""
bullet_points_acn = """
- Advanced Computer Networking
- Internet protocols, protocol mechanisms and design techniques
- basics of networking and protocols will be revised
- weekly exercises, programming tasks
- No programming experience required, but recommended
- computer networks
"""


def generate_module_attribute(chain, chat):
    result = chain.invoke(chat)
    chat.append(AIMessage(content=result))
    return result

def loop(chain, chat, name):
    result = generate_module_attribute(chain, chat)
    print(f"""Are you satisfied with the following {name} description?
Enter 'yes' to continue generate the modules requirements.
Tell me what to correct otherwise.
""")
    print(result + '\n')

    while True:
        user_input = input().strip()
        print()
        chat.append(HumanMessage(content=user_input))
        if user_input.lower() == "yes":
            return result
        elif user_input == "":
            print("Do not send empty input.")
        else:
            result = generate_module_attribute(chain, chat)
            print(result + '\n')
            print("Enter 'yes' to continue, correct me otherwise.\n")

def generate_content_loop(chain, chat):
    chat.append(HumanMessage(content=f"Based on these ideas and what you know about the Advanced Computer Networking course of TUM, write a brief, maximally 50 word, free text of the modules content that is taught in the lecture."))
    result = loop(chain, chat, "Content")
    return result

def generate_prerequisites_loop(chain, chat):
    chat.append(HumanMessage(content=f"Keep the style of your previous response and write brief free text (NO LIST) of the recommended prerequisites for that module based on the bullet points."))
    result = loop(chain, chat, "Prerequisites")
    return result

def generate_learning_outcomes_loop(chain, chat):
    chat.append(HumanMessage(content=f"Keep the style of your previous response and write brief free text (NO LIST) about the learning outcomes for that module based on the bullet points."))
    result = loop(chain, chat, "Learning Outcomes")
    return result

def generate_learning_methods_loop(chain, chat):
    chat.append(HumanMessage(content=f"Keep the style of your previous response and write brief free text (NO LIST) about the learning methods for that module based on the bullet points."))
    result = loop(chain, chat, "Learning Methods")
    return result

def generate_media_used_loop(chain, chat):
    chat.append(HumanMessage(content=f"Keep the style of your previous response and write brief free text (NO LIST) of the media used for that module based on the bullet points."))
    result = loop(chain, chat, "Media Used")
    return result

def generate_reading_list_loop(chain, chat):
    chat.append(HumanMessage(content=f"Keep the style of your previous response and write brief reading list of that module based on the bullet points."))
    result = loop(chain, chat, "Reading List")
    return result

        
def generate_module_from_bullet_points(name, bullet_points):
    module = Module(title_en=name, description_bullet_points_en=bullet_points)
    client = ChatOpenAI(model="gpt-3.5-turbo")
    parser = StrOutputParser()
    chain = client | parser
    chat = []

    #create initial message
    chat.append(SystemMessage(content=f"{persona} {bullet_points}. The modules name is {name}. You answer only in free text, even with lists."))

    #generate content
    module.content_en = generate_content_loop(chain, chat)

    #generate prerequisites
    module.recommended_prerequisites_en = generate_prerequisites_loop(chain, chat)

    #generate learning outcomes
    module.intended_learning_outcomes_en = generate_learning_outcomes_loop(chain, chat)

    #generate learning methods
    module.teaching_and_learning_methods_en = generate_learning_methods_loop(chain, chat)

    #generate media used
    module.media_en = generate_media_used_loop(chain, chat)

    #generate reading list
    module.reading_list_en = generate_reading_list_loop(chain, chat)

    return module


def manual_main():
    print("What is the modules name?")
    name = input()
    print("Please enter a list of bullet points to describe your module. Enter 'done' if you want to start generating the modules description. Starting with the content.")
    bullet_points = []
    while True:
        user_input = input()
        print()
        if user_input.lower() == "q":
            break
        elif user_input.lower() == "help":
            print("Enter 'q' to quit")
        elif user_input.lower() == "done":
            generate_module_from_bullet_points(name, "\n".join(bullet_points))
            break
        else:
            bullet_points.append(user_input)
    

def main():
    # acn_test_module = generate_module_from_bullet_points("Advanced Computer Networking", bullet_points_acn)
    name = "Advanced Computer Networking"
    generate_module_from_bullet_points(name, "\n".join(bullet_points_acn))

if __name__ == "__main__":
    main()