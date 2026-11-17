# python_flask_blueprint_mongoenginemate_boilerplate

A starter template for Python 3 + Flask + MongoDB APIs, with a tidy NestJS-style folder structure: a controller, service, DTOs and a test for every module. Flask leaves the structure up to you, which gets messy as an API grows. This gives you a clear layout from day one, plus a generator that scaffolds a full CRUD module for you.

The folder structure is inspired by NestJS, Angular and Spring Boot.

## What's included

1. **Flask blueprints** — one module per feature (`src/modules/<name>/`), each with its own controller, service, DTOs and test
2. **MongoEngine + mongoengine-mate** — Mongoose-style queries, snake_cased
3. **Pydantic request validation** with auto-generated API docs (Flask-Pydantic-Docs)
4. **JWT auth** helpers
5. **A CRUD generator** — `python generator.py` scaffolds a whole module
6. **Docker + docker-compose** for running it with Mongo
7. **Waitress** as the production server, `.env.example` for config
8. **pytest** wired up

## Run it

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

## Good to know

1. Database queries work like [Mongoose](https://mongoosejs.com/), but snake_cased. For example:

```python
UserSchema.col().any_mongoose_function()
```

2. Request validation uses [Flask-Pydantic-Docs](https://pypi.org/project/Flask-Pydantic-Docs/). For the Pydantic notation, see [Flask-Pydantic](https://pypi.org/project/Flask-Pydantic/).

3. The folder structure follows [NestJS](https://nestjs.com/).

## Thanks

To the Flask, MongoEngine and Pydantic maintainers — this is mostly glue on top of their work.

## License

MIT License — Copyright (c) Fayaz Bin Salam. See [LICENSE](LICENSE) for the full text.

## Contributing

Contributions are very welcome, thank you! Before you start on a pull request, please open an issue and tell me what you would like to add or change. That way we can agree on it first, and your time is not wasted on something that might not fit.

<p><a href="https://p32929.github.io/share/?repo=python_flask_blueprint_mongoenginemate_boilerplate"><picture><source media="(prefers-color-scheme: dark)" srcset="https://p32929.github.io/readme/footer-share-dark.svg"><img src="https://p32929.github.io/readme/footer-share-light.svg" width="50%" align="top" alt="Share this project with your friends in one click"></picture></a><a href="https://p32929.github.io/support/"><picture><source media="(prefers-color-scheme: dark)" srcset="https://p32929.github.io/readme/footer-support-dark.svg"><img src="https://p32929.github.io/readme/footer-support-light.svg" width="50%" align="top" alt="If you like my work and want to support me, feel free to support"></picture></a><br><a href="https://openstore.pfay.workers.dev/add"><picture><source media="(prefers-color-scheme: dark)" srcset="https://p32929.github.io/readme/footer-join-dark.svg"><img src="https://p32929.github.io/readme/footer-join-light.svg" width="100%" align="top" alt="Put your own apps on OpenStore: free, your listing lives in your own repo"></picture></a></p>
