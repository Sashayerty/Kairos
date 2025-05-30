# :tada: Описание

Kairos - веб-приложение, написанное на `flask`. Основной идеей является сокращение времени пользователя на поиск информации и ее дальнейшее структурирование для обучения. Весь функционал, подразумевающий под собой создание промптов, планов, поиск в Интернете и т.п. реализован при помощи ИИ. В проекте используются модели от `Mistral`, в частности модель `mistral-large-latest`. В будущем планируется реализация поддержки локальных моделей `Ollama`.
Сам по себе проект является экосистемой продуктов по брендом `Kairos`. Одним из таких продуктов является `FastAPI` [версия](https://github.com/sashayerty/kairos-fastapi) RestAPI проекта.

ИИ обрабатывает запросы как на русском языке (так изначально задумывалось), так и на английском языке.

Пайплайн взаимодействия ИИ-агентов в проекте (ветка с поиском не работает, но функционал реализован):

```mermaid
flowchart TD
user(Пользователь)
course_input(Тема курса
Пожелания к курсу
Описание пользователя)
user --> course_input
censor(Агент-цензор)
course_input --> censor
prompt(Агент-промпт)
censor -->|Все плохо!| user
censor --> prompt
plan(Агент-план)
course(Агент-курс)
prompt -->|Промпт| plan
plan -->|План| course
prompt -->|Промпт| course
scraper([Web-scraper])
search([Агент-поисковик])
course_input --> search
search -->|Запрос| scraper
scraper -->|Данные для курса| course
course -->|Итоговый курс| user
```

## Планы

- Переход от `sqlalchemy` к `SQLModel`
- **β**: Поддержка локальных моделей `Ollama`
- Создание отдельного микросервиса для создания и решения тестов `kairos-test`
- Улучшение промптов
- **β**: Реализация агентов с помощью `LangChain/OpenAI`(для поддержки локальных моделей)
- Реализация `rag-системы` с данными из интернета или личной базой знаний
- Включение функции web-скрапинга
- Использование наработок Блума

`β` - есть в бета-версии
