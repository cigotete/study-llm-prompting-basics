from ai.completion.utility import utility
from ai.prompts.summarize import summarize

if __name__ == '__main__':

    summarizer = summarize.Summarizer(prompt_type="G")
    text = summarize.Summarizer.get_text()
    prompt = summarizer.get_prompt(text)

    genericPrompt = utility.AIUtility(prompt=prompt)
    genericPrompt.print_completion()