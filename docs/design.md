# Design notes

The API layer handles HTTP concerns, the model module validates data and creates domain
objects, and the repository isolates persistence. The current repository is in-memory and
does not survive restarts. Replace it with SQLAlchemy and PostgreSQL before claiming durable
persistence. Add authentication/authorization, migrations, pagination, rate limits, and
contract tests before production deployment.
