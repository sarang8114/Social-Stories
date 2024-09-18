from langchain.prompts import FewShotPromptTemplate, PromptTemplate

# Define examples
examples = [
    {
        "topic": "Waiting for My Turn",
        "story": "Oliver sometimes has to wait his turn to play. While waiting, he watches his friends and stays patient. When it's his turn, he gets excited but remembers to play nicely. Waiting can be hard, but Oliver knows everyone gets a turn."
    },
    {
        "topic": "Asking for Help",
        "story": "Ethan sometimes feels stuck when he doesn't know what to do. Instead of getting upset, he asks his teacher or a friend for help. Ethan learns that asking for help is a good way to solve problems quickly."
    },
    {
        "topic": "Brushing My Teeth",
        "story": "Ethan brushes his teeth every morning and night to keep them healthy. He uses his toothbrush, toothpaste, and water to clean his teeth. When he finishes, his mouth feels fresh and clean, and Ethan smiles brightly."
    }
]

# Create prompt templates
example_prompt = PromptTemplate(
    input_variables=["topic", "story"],
    template="User: {topic}\nAI: {story}"
)

# Enhanced prefix with additional instructions
prefix = (
    "Generate a story on the topic '{topic}' in about 50 words. "
    "The story must be written in third person, like the examples provided. "
    "Do not use first-person language such as 'I', 'me', or 'my'. "
    "The story should describe what 'children' or a specific child (e.g., 'Oliver', 'Ethan') does, "
    "rather than what 'I' do. "
    "The story must be a social story used to teach children with ASD about different social skills and manners "
    "related to the topic. Use language that is easy to understand for children aged 5-10. "
    "Keep the story simple and clear, avoiding complex words or phrases."
)

suffix = "User: {topic}\nAI: "

few_shot_prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix=prefix,
    suffix=suffix,
    input_variables=["topic"],
    example_separator="\n"
)
