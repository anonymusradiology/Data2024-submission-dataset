import openai

openai.api_key = "API_KEY"
model_name = "gpt-4"

with open("prompt.txt", "r") as f:
    prompt = f.read()


def process_report(text):
    content2system = "As a radiologist, your task involves analyzing radiology reports."
    content2user = prompt + """Here is the record you have to analyze: {}""".format(text)

    completion = openai.ChatCompletion.create(model=model_name, temperature=0, top_p=0, seed=0,
                                              messages=[{"role": "system", "content": content2system},
                                                        {"role": "user", "content": content2user}])

    return completion.choices[0].message["content"]


if __name__ == '__main__':
    with open("report_sample.txt", "r") as f:
        report_sample = f.read()

    print(process_report(report_sample))
