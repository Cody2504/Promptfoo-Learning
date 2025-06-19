def create_prompt(context):
    vars = context['vars']
    provider = context['provider']

    # Dynamic prompt generation
    if vars.get('technical_audience'):
        return f"Provide a technical analysis of {vars['topic']}"
    else:
        return f"Explain {vars['topic']} for beginners"