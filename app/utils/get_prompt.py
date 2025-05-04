import yaml

def get_prompt(name):
    with open("app/prompts/prompt.yml", "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)
        return config[name]["prompt"]

argument_prompt= get_prompt("ARGUMENT_NODE_PROMPT")
rebuttal_prompt= get_prompt("REBUTTAL_NODE_PROMPT")