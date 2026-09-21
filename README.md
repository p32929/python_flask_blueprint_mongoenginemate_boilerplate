# python_flask_blueprint_mongoenginemate_boilerplate

A Python 3 + Flask + MongoDB boilerplate with a NestJS-style folder structure — controllers, services, DTOs and tests per module, plus a generator that scaffolds a full CRUD module for you.

The folder structure is greatly inspired by NestJS / Angular (2+) / Spring Boot etc.

## What's included

- **Flask blueprints** — one module per feature (`src/modules/<name>/`), each with its own controller, service, DTOs and test
- **MongoEngine + mongoengine-mate** — Mongoose-style queries, snake_cased
- **Pydantic request validation** with auto-generated API docs (Flask-Pydantic-Docs)
- **JWT auth** helpers
- **A CRUD generator** — `python generator.py` scaffolds a whole module
- **Docker + docker-compose** for running it with Mongo
- **Waitress** as the production server, `.env.example` for config
- **pytest** wired up

## How to run

Windows:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Linux/Mac:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and fill it in, then run `main.py`:

```bash
python main.py
```

Or with Docker:

```bash
docker-compose up
```

## Generate a CRUD module

```bash
python generator.py
```

## Run tests

```bash
python -m pytest
```

## Docs

1. The db queries are like https://mongoosejs.com/ but snake_cased. Example:

```python
UserSchema.col().any_mongoose_function()
```

2. API validations are done using: https://pypi.org/project/Flask-Pydantic-Docs/ ( For pydantic notations, see this too: https://pypi.org/project/Flask-Pydantic/ )

3. It follows the folder structure of https://nestjs.com/

## Thanks

To the Flask, MongoEngine and Pydantic maintainers — this is mostly glue on top of their work.

## License

MIT License — Copyright (c) Fayaz Bin Salam. See [LICENSE](LICENSE) for the full text.

## Contributing

Contributions are warmly welcomed and greatly appreciated! Whether it's a bug fix, new feature, or improvement, your input helps make this project better for everyone.

Before submitting a pull request, please:

1. Create an issue describing the feature or bug fix you'd like to work on
2. Wait for discussion and approval to ensure alignment with project goals
3. Fork the repository and create your feature branch
4. Submit your pull request with a clear description of changes

This approach helps avoid duplicate efforts and ensures smooth collaboration. Thank you for considering contributing!

## Share

Sharing this repository with your friends is just one click away from here

[![facebook](https://user-images.githubusercontent.com/6418354/179013321-ac1d1452-0689-493f-9066-940cf2302b6e.png)](https://www.facebook.com/sharer/sharer.php?u=https://github.com/p32929/python_flask_blueprint_mongoenginemate_boilerplate/)
[![twitter](https://user-images.githubusercontent.com/6418354/179013351-7d8d6d1c-4ce2-46ab-bef8-4c4765a1b888.png)](https://twitter.com/intent/tweet?url=https://github.com/p32929/python_flask_blueprint_mongoenginemate_boilerplate/)
[![tumblr](https://user-images.githubusercontent.com/6418354/179013343-3111f55a-3b90-40c7-8487-9777348672b0.png)](https://www.tumblr.com/share?v=3&u=https://github.com/p32929/python_flask_blueprint_mongoenginemate_boilerplate/)
[![pocket](https://user-images.githubusercontent.com/6418354/179013334-b095c45f-becf-49f4-9ee1-5a731a9b1f85.png)](https://getpocket.com/save?url=https://github.com/p32929/python_flask_blueprint_mongoenginemate_boilerplate/)
[![pinterest](https://user-images.githubusercontent.com/6418354/179013331-44cd9206-11b1-4b65-becb-5863b61c828f.png)](https://pinterest.com/pin/create/button/?url=https://github.com/p32929/python_flask_blueprint_mongoenginemate_boilerplate/)
[![reddit](https://user-images.githubusercontent.com/6418354/179013338-7416ae3f-73ba-4522-86e1-1374d7082d22.png)](https://www.reddit.com/submit?url=https://github.com/p32929/python_flask_blueprint_mongoenginemate_boilerplate/)
[![linkedin](https://user-images.githubusercontent.com/6418354/179013327-ca7b7102-1da8-4b1c-858f-1a6e5f21bd70.png)](https://www.linkedin.com/shareArticle?mini=true&url=https://github.com/p32929/python_flask_blueprint_mongoenginemate_boilerplate/)
[![whatsapp](https://user-images.githubusercontent.com/6418354/179013353-f477fa0b-3e6f-4138-a357-c9991b23ff88.png)](https://api.whatsapp.com/send?text=https://github.com/p32929/python_flask_blueprint_mongoenginemate_boilerplate/)

---

## Support

If you like my works and want to support me/my works, feel free to support or donate. My payment details can be found here: https://p32929.github.io/SendMoney2MeV1/

<!-- hire-block -->

---

## 💼 Need this customised — or need it yesterday?

I take fixed-price backend work on my own projects. No hourly billing, no surprise scope:

| | |
|---|---|
| **Drop-in integration** — I wire this into your codebase and hand you a PR that builds | **$45** · 3 days |
| **Priority bug fix or small feature** — jumps ahead of the free issue queue | **$95** · 72 hours |
| **Custom build** — branded, packaged and deployed, source yours | **$130** · 7 days |
| **A full app from scratch** | **from $350** · quoted first |

All prices and how to buy → **[p32929.github.io/hire](https://p32929.github.io/hire/)**  
Or buy through [Fiverr](https://www.fiverr.com/fayazbinsalam) (escrow, ID-verified, 5.0★) — safest for a first job.

Scoping and quotes are free: [open an issue](https://github.com/p32929/hire/issues/new) and describe the job.
