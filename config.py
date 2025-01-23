import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """
    Configuration class to manage environment variables and settings.
    """
    NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
    NEO4J_USERNAME = os.getenv("NEO4J_USERNAME", "neo4j")
    NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY", "your-groq-api-key")

    @staticmethod
    def validate():
        """
        Validate required environment variables and settings.
        """
        missing = []
        if not Config.NEO4J_URI:
            missing.append("NEO4J_URI")
        if not Config.NEO4J_USERNAME:
            missing.append("NEO4J_USERNAME")
        if not Config.NEO4J_PASSWORD:
            missing.append("NEO4J_PASSWORD")
        if not Config.GROQ_API_KEY:
            missing.append("GROQ_API_KEY")

        if missing:
            raise EnvironmentError(f"Missing required environment variables: {', '.join(missing)}")
        else:
            print("Configuration validated successfully.")


