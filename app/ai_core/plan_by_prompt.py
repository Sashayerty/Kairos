from app.mistral_ai_initializer import mistral_ai_initializer


def plan(prompt_from_llm: str) -> str:
    """Функция для составления плана курса по промпту от llm

    Args:
        prompt_from_llm (str): Промпт от llm

    Returns:
        str: План dict в виде str
    """
    json_example = """
    {
        "1": "Как начать программировать",
        "1.1": "Азы и начала",
        "1.2": "Выбор языка",
        "2": "Основные языки программирования"
    }
    """
    prompt = f"""Привет! Ты профессиональный составитель планов для LLM.
    Тебе на вход передается промпт, по которому LLM должна составить курс, а твоя задача
    максимально правильно и рационально сделать план для нее же. Анализируй следующий
    пункт плана, опираясь на предыдущий. Промпт: {prompt_from_llm}.
    От тебя требуется только план и больше ничего: ни пояснений, ни ссылок на статьи, ни примеров проектов и тп.
    Не используй разметку md в своем ответе, ты пишешь для LLM.
    Пример твоего ответа: {json_example}(это пример!). У тебя также должны быть подпункты."""
    client = mistral_ai_initializer()
    result = client.message(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        temperature=0.2,
        response_format={
            "type": "json_object",
        },
    )
    return result
