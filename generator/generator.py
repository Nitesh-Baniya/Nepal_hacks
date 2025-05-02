import requests

def generate_answer(requirement, evidence_chunks):
    """
    Use Flan-T5 (text2text-generation) to classify requirement satisfaction.
    Returns a string with [Satisfied/Not Satisfied/Missing] and an explanation.
    """

    big_chunk = ""
    for chunk in evidence_chunks:
        big_chunk += chunk

    prompt = (
    "You are a compliance assistant.\n"
    "1) First write the requirement at the beggining of the answer"
    "2) given the evidence, find if the requirement is: 'Satisfied' or 'Not Satisfied.\n"
    "3) explain in short why."
    "Here is an example for the format: " 
    '''
        **Requirement**:
        The organization shall determine:

        a) interested parties that are relevant to the information security management system;
        b) the relevant requirements of these interested parties;
        c) which of these requirements will be addressed through the information security management system.

        **Status**:
        Requirement: Satisfied

        **Reason**:

        * The requirement is satisfied because the organization has identified an "Information Security Committee" that will oversee the implementation and ongoing management of the information security program. This suggests a clear structure for involving interested parties in the process.
        * Although the text does not explicitly mention identifying relevant requirements, it does mention "security and compliance requirements", which implies that the organization has taken steps to identify these requirements. 
        * However, it is unclear if all identified requirements will be addressed through the information security management system.
    '''

    "Here is the requirement: \n"
    f"{requirement}\n\n"
    "Here is the evidence:\n"
    f"{big_chunk}\n\n"
    )
    #print(prompt)
    
    # print("***"*20)
    response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3.2",       # Use the same name you use in the CLI
        "prompt": prompt,
        "stream": False          # Set to True if you want to stream output
    }
)

    # print("***"*20)
    # Extract and print the generated response
    # print(response.json()["response"])
    

    return response.json()["response"] + f"\n\n**Target Policy**: {big_chunk}"