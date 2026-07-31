# Диагностика зрелости — модель

Основа: **BI Project Health Check** (метод Data Nature / Alex Barakov). Расширена **AI-readiness оверлеем** курса. Файл-эталон: `BI Project Health Check.xlsx`.

## Шкала оценки (0–4)

Базовая шкала (для большинства факторов):

| Балл | Значение |
|---|---|
| 0 | No — нет |
| 1 | Planned — запланировано |
| 2 | In Progress / Partially — частично |
| 3 | Completed, но нужны улучшения |
| 4 | Fully Completed & Optimized — сделано и оптимизировано |

Спец-шкалы (тот же 0–4): **Applicability** (Not Applicable → Highly Applicable), **User-count** (≤50 / ≤150 / ≤500 / 500+), **Business dependency** (High / Moderate / Low), **Disruption likelihood** (Very Likely / Somewhat / Unlikely).

По каждому фактору участник ставит текущую оценку **и 1Y-таргет** (цель на год). Разрыв (таргет − текущее) = приоритет.

## Уровни зрелости (band'ы для дашборда)

Средний балл категории → band: **Beginning (0–1) · Learning (1–2) · Developing (2–3) · Mastering (3–4)**.

## Визуализация зрелости (обязательно)

В `00-Диагностика` вставляй **бар-чарт зрелости по темам** (как в Data & Analytics Maturity Tool): горизонтальные бары 0–4 по 9 категориям + AI-readiness, с зонами Beginning/Learning/Developing/Mastering. Генерируй скриптом `references/make-maturity-svg.py` (впиши в `SCORES` само-оценку участника) → `assets/maturity.svg`, вставь `![Профиль зрелости по темам](assets/maturity.svg)`. Плюс блок «🧭 Фазы работы»: 🔎 AS-IS = блоки 1–2, 🛠️ TO-BE = 3–6, 🚀 Трансформация = 7.

## 9 категорий (Health Check) и их факторы

1. **Connection with business** (6): регистрация аналитических кейсов; интеграция в бизнес-процессы; согласование целей BI с бизнес-целями; определение целевых ролей-аудитории; структурирование бизнес-метрик (дерево метрик); отслеживание влияния на бизнес.
2. **Adoption and Satisfaction** (7): мониторинг использования BI (BI for BI); оценка adoption; вовлечённость бизнеса (>50% активных); опросы удовлетворённости; сбор фидбека; онбординг новых пользователей.
3. **BI Content management** (12): критерии приёмки; документированный процесс разработки; чек-лист тестирования/релиза; документация отчётов; сертификация контента с бизнесом; интеграция с глоссарием; архивация; отслеживание и улучшение времени загрузки; стайл-гайд; SLA здоровья контента.
4. **Self-Service BI Delivery** (8): баланс операционной модели (central + SSBI); консистентность методологии/инструментов; портал/канал коммуникации; передача и ревью контента; программа BI-чемпионов; learning paths; развитие сообщества; тренинги и менторство.
5. **Guided BI Service Delivery** (8): поддержка пользователей; обучение; совместные сессии анализа данных; доступность/исследуемость данных; мобильная оптимизация; usability-тестирование; анализ UX-поведения; улучшение навигации BI-портала.
6. **BI Platform Governance** (10): **semantic layer**; **metric store**; insights management; CI/CD; self-service ETL; мониторинг производительности; оптимизация запросов; процесс обновления платформы; интеграция с дата-каталогом; автоматизация подписок.
7. **Data Quality management** (6): автообновление отчётов; валидация данных; сертифицированные источники; документация источников; отслеживание изменений lineage; прозрачность свежести данных.
8. **BI security and compliance** (8): ролевой доступ; авто-идентификация ролей; workflow запросов доступа; интеграция с AD; аудиты безопасности; комплаянс (GDPR/HIPAA); оценка рисков; disaster recovery.
9. **Project Management** (8): система приоритизации; трекинг задач (Jira); Agile (Kanban/Scrum); матрица компетенций; операционные KPI; целеполагание команды; долгосрочный стратегический план BI; стандартизированный найм.

Расширенный блок (D&A / Data Governance maturity, ~83 фактора) — для Полного режима: Data sharing/democratization; **Data Governance** (sponsorship, stewardship, budget, policies, classification, metadata, catalog, roadmap); DQ management; Data security; **Data Architecture** (arch reviews, scalability, integrated governance, modern/cloud, real-time, **AI/ML**, **data mesh**, **data contracts**); Strategic leadership (D&A vision, exec involvement, investment, data literacy, ethics).

## 7 solution-категорий (кросс-срез)

Каждый фактор тегируется одной: **Business Alignment · Data Culture · Processes & Standards · User Engagement · Skills & Trainings · Tools & Automation · Efficiency Monitoring**. Второй дашборд считает зрелость в этом срезе — полезно, чтобы увидеть системный перекос (напр. сильные Tools, слабый User Engagement).

## AI-readiness оверлей (слой курса)

Поверх Health Check оцени AI-готовность (0–4 по тем же band'ам). Это 10-я условная категория:

- **Семантическое покрытие** — доля ключевых метрик с однозначным определением в semantic layer / metric store.
- **Trusted core** — доля запросов/отчётов на certified core-слое; наличие ownership/SLA/DQ на витринах.
- **Доменный контекст (ДБЗ)** — полнота доменной базы знаний: объекты, глоссарий, FAQ, примеры «вопрос→SQL», eval-кейсы (минимумы: ≥5/≥5/≥3/≥5/≥10).
- **Готовность процессов** к режиму «AI генерирует — человек проверяет»: есть ли verify-gate (BI Partner), kill-gates, eval-инфраструктура.
- **Агентная инфраструктура** — MCP к сервисам, реестр скиллов, judge-gate/guardrails, наблюдаемость (трейсинг).

## Диагноз цепочки зависимостей (ключевой вывод)

Проверь цепочку и найди, где рвётся первым:

```
Core-слой → сертификация метрик (semantic) → доменный контекст (ДБЗ)
        → точность AI (25% без grounding → 80% с ним) → self-service
```

Правило: **AI-фичи нельзя ставить раньше своего звена** — на грязных данных они выдают правдоподобный мусор и роняют доверие. Назови 2–3 самых дорогих разрыва — они станут приоритетом №1 в Action plan.

## Как диагностика питает стратегию

- Слабые **категории** (Beginning/Learning) → TO-BE-инициативы в соответствующих блоках Planner (2.x) и в Action plan (4).
- Перекос по **solution-категориям** → системная рекомендация (напр. «инструменты есть, adoption нет → занятие про User Engagement, а не про новый тул»).
- **Разрыв цепочки** → порядок в stack-rank (Governance → Trusted Data → AI-готовность → BI Content → Self-service).
- **1Y-таргеты** участника → измеримые цели в BI Vision (блок 5).
