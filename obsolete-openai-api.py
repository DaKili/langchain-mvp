from openai import OpenAI

persona = "You are a professor at the Technical University of Munich who wants to create a new module in Informatics with the following core ideas in the form of bullet points: "
text_format_brief_free_text = "a brief (max. 50 words, preferably less) free text (no list)"
text_format_concept_list = "a concise list of concepts taught (max. 7 words per line, preferably less)"

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

def print_cost(name, usage):
    completion_token_cost = usage.completion_tokens
    prompt_token_cost = usage.prompt_tokens
    total_token_cost = usage.total_tokens
    print(f"{name} cost: {completion_token_cost}, Prompt Tokens: {prompt_token_cost}, Total Tokens: {total_token_cost}")

def create_prompt(prompt):
    client = OpenAI()
    return client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=150
    )

def generate_intended_learning_outcomes(name, bullet_points, text_format):
    prompt = f"""
    You are a {persona} who wants to create a new module in Informatics with the following core ideas: {bullet_points}
    Based on these ideas, write a brief (max. 50 words, preferably less) free text (no list) of {name} for that module.
    """
    response = create_prompt(prompt)
    print_cost(name, response.usage)
    result = response.choices[0].text.strip()
    return result

def generate_recommended_prerequisites(name, bullet_points, text_format):
    prompt = f"""
    You are a {persona} who wants to create a new module in Informatics with the following core ideas: {bullet_points}
    Based on these ideas, write {text_format} of beneficial prerequisites for that module. Keep this really short and only name things that are fundamental for this module, not things that will be taught.
    """
    response = create_prompt(prompt)
    print_cost(name, response.usage)
    result = response.choices[0].text.strip()
    return result

def generate_content(name, bullet_points, text_format):
    prompt = f"""
    You are a {persona} who wants to create a new module in Informatics with the following core ideas: {bullet_points}
    Based on these ideas, write {text_format} of the content for that module.
    """
    response = create_prompt(prompt)
    print_cost(name, response.usage)
    result = response.choices[0].text.strip()
    return result

def generate_teaching_methods(name, bullet_points, text_format):
    prompt = f"""
    You are a {persona} who wants to create a new module in Informatics with the following core ideas: {bullet_points}
    Based on these ideas, write {text_format} of the teaching and learning methods for that module.
    """
    response = create_prompt(prompt)
    print_cost(name, response.usage)
    result = response.choices[0].text.strip()
    return result

def generate_media(name, bullet_points, text_format):
    prompt = f"""
    You are a {persona} who wants to create a new module in Informatics with the following core ideas: {bullet_points}
    Based on these ideas, write {text_format} of the media for that module.
    """
    response = create_prompt(prompt)
    print_cost(name, response.usage)
    result = response.choices[0].text.strip()
    return result

def generate_reading_list(name, bullet_points, text_format):
    prompt = f"""
    You are a {persona} who wants to create a new module in Informatics with the following core ideas: {bullet_points}
    Based on these ideas, write {text_format} of the reading list for {name} that is taught at the Techincal University of Munich. Respond with ONLY the list of 1-3 pieces of literature. Preferably less.
    """
    response = create_prompt(prompt)
    print_cost(name, response.usage)
    result = response.choices[0].text.strip()
    return result

    # results = result.strip('\n\n').split('\n\n')

    # # Risky and temporary extraction of parts of the response. There is no guarantee that gpt prepends the lines with a descriptor. Also the order could be different if it wanted.
    # return Module(
    #     name,
    #     intended_learning_outcomes_en = results[0].split(':', 1)[1],
    #     recommended_prerequisites_en = results[1].split(':', 1)[1],
    #     content_en = results[2].split(':', 1)[1],
    #     teaching_and_learning_methods_en = results[3].split(':', 1)[1],
    #     media_en = results[4].split(':', 1)[1],
    #     reading_list_en = results[5] .split(':', 1)[1],
    #     description_bullet_points_en = bullet_points
    # )

def obsolete_generate_module_from_bullet_points(name, bullet_points, messages):
    # client = ChatOpenAI(model="gpt-3.5-turbo") # This yields worse results than the normal OpenAI API, even though langchain recommends it.
    # client = OpenAI(model="gpt-3.5-turbo-instruct") # Instruct seems more reliable, consistent and follows instructions more directly. The returned object lacks information though.
    client = ChatOpenAI(model="gpt-3.5-turbo")
    parser = StrOutputParser()
    # client = ChatOpenAI(model="gpt-3.5-turbo")
    
    # Individual messages consume way more tokens, not necessarily improving responses. They tend to get overly long and elaborate. They also take way more time than wrapping everything in one message.
    messages = [
        SystemMessage(content=f"{persona} {bullet_points}. Prepend every description with '<description name>:'"),
        HumanMessage(content=f"Based on these ideas, write a brief (max. 50 words, preferably less) free text (no list) of the intendes learning outcomes for that module."),
        HumanMessage(content=f"write a brief free text (NO LIST) of the recommended prerequisites for that module."),
        HumanMessage(content=f"write a brief free text (NO LIST) of the content for that module."),
        HumanMessage(content=f"write a brief free text (NO LIST) of the teaching and learning methods for that module."),
        HumanMessage(content=f"write a brief free text (NO LIST) of the media of that module."),
        HumanMessage(content=f"write a brief free text (NO LIST) of the reading list for that module. Max 3 books, preferably less.")
    ]
    print("tokens_from_messages: " + str(client.get_num_tokens_from_messages(messages)))
    # chain = client | parser
    result = client.invoke(messages)
    # result = chain.invoke(messages)
    print(result + "\n")