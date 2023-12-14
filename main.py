from ai.completion.utility import utility
from ai.prompts.summarize import summarize

if __name__ == '__main__':

    summarizer = summarize.Summarizer(prompt_type="S")
    text = summarize.Summarizer.get_text()
    prompt = summarizer.get_prompt(text)

    specificPrompt = utility.AIUtility(prompt=prompt, temperature=0.7)
    specificPrompt.print_completion()