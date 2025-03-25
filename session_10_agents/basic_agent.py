import requests
import openai
import re


class ResearchAssistant:
    def __init__(self):
        self.client = openai.OpenAI()
        self.memory = [
            {"role": "system", "content": "You are a research assistant with access to web search and calculator tools. Be concise and factual in your responses."}
        ]

    def call_llm(self, prompt):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.memory + [{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content.strip()

    def web_search(self, query):
        url = "https://api.duckduckgo.com/"
        params = {"q": query, "format": "json", "no_html": 1}
        response = requests.get(url, params=params)
        data = response.json()
        return data.get("Abstract", "No results found")[:500]

    def calculate(self, expression):
        if not re.match(r'^[\d\s\+\-\*/\(\)\.]+$', expression):
            return "Invalid expression"
        result = eval(expression)
        return str(result)

    def reflect(self, task, previous_result=None):
        prompt = f"Task: {task}\n"
        if previous_result:
            prompt += f"Previous result: {previous_result}\n"
        prompt += "Reflect on the current state of the research. What have we learned? What should we do next?"
        reflection = self.call_llm(prompt)
        self.memory.append({"role": "assistant", "content": reflection})
        return reflection

    def plan(self, reflection):
        prompt = f"Based on this reflection: {reflection}\n" \
            "Plan the next single action to progress the research. " \
            "Choose one: [web_search:query], [calculate:expression], or [finalize:summary]"
        plan = self.call_llm(prompt, max_tokens=50)
        self.memory.append(
            {"role": "assistant", "content": f"Planned action: {plan}"})
        return plan

    def execute(self, plan):
        if "web_search:" in plan:
            query = plan.split("web_search:")[1].strip()
            result = self.web_search(query)
            self.memory.append(
                {"role": "tool", "content": f"Web search result for '{query}': {result}"})
            return result
        elif "calculate:" in plan:
            expression = plan.split("calculate:")[1].strip()
            result = self.calculate(expression)
            self.memory.append(
                {"role": "tool", "content": f"Calculation result for '{expression}': {result}"})
            return result
        elif "finalize:" in plan:
            summary = plan.split("finalize:")[1].strip()
            self.memory.append(
                {"role": "assistant", "content": f"Final summary: {summary}"})
            return summary
        return "Invalid plan"

    def research(self, task):
        previous_result = None

        while True:
            reflection = self.reflect(task, previous_result)
            plan = self.plan(reflection)
            result = self.execute(plan)
            if "finalize:" in plan:
                return result
            previous_result = result


agent = ResearchAssistant()
task = "Calculate the average global temperature increase from 1900 to 2020"
final_result = agent.research(task)
print(f"\nFinal Result: {final_result}")
