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