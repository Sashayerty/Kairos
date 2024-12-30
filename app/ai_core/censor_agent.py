from app.mistral_ai_initializer import mistral_ai_initializer


def censor(theme_from_user: str) -> str:
    json_example = """
    С темой все хорошо:
    {
        "data": True
    }
    Иначе:
    {
        "data": False
    }
    """
    prompt = f"""Привет! Ты агент-цензор. Твоя задача проверять тему пользователя. Тема должна быть не должна быть
    связана с 18+ контентом, правительством, религией, межнациональной рознью, опасными для жизни
    человека действиями, химикатами и т.п. Если тема никак не связана с перечисленным, то ты пропускаешь ее далее,
    иначе - не пропускаешь. Тема пользователя: {theme_from_user} Пример твоего ответа: {json_example}"""
    client = mistral_ai_initializer()
    response = client.message(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        temperature=0,
        response_format={
            "type": "json_object",
        },
    )
    return response
