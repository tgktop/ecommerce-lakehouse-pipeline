# E-Commerce & Supply Chain Lakehouse Pipeline

Welcome to the documentation portal for the E-Commerce & Supply Chain Lakehouse Pipeline. This repository implements an automated, modular ELT data pipeline and lakehouse architecture designed to ingest raw telemetry, transform it into a normalized Star Schema, run automated data quality assertions, and store it in partitioned Apache Parquet format.

## Documentation Index

To keep our repository organized and maintainable, our documentation has been separated into dedicated files within the `docs/` folder:

- **[Project Context & Goals](docs/context.md)** — Overview of the business problem, target audience, and engineering objectives.
- **[Setup & Installation Guide](docs/setup.md)** — Step-by-step instructions for setting up the environment, virtual environment, and dependencies on a Linux/Chromebook terminal.
- **[Architecture & Pipeline Design](docs/architecture.md)** — Deep dive into the 6-phase pipeline structure, star schema modeling, data quality gates, and partitioning strategy.

## 🔮 Future Roadmap & Scalability
* **BI & Visualization Layer:** Integrate a Streamlit or Apache Superset dashboard querying the partitioned Parquet lakehouse directly via DuckDB.
* **Orchestration:** Migrate local sequential execution to Apache Airflow or Prefect DAGs for automated daily scheduling.
* **Cloud Migration:** Transition raw and processed storage layers from local disk to AWS S3, utilizing AWS Glue and Athena for serverless querying.

---
*Built as a portfolio project showcasing modern data engineering standards and cloud-native lakehouse practices.*