from dataclasses import dataclass
import os

@dataclass(frozen=True)
class PortfolioConfig():
    atlas_admin_user: str
    atlas_admin_pw: str
    atlas_db_name: str
    atlas_conn_str: str
    openai_api_key: str
    openai_embedding_model: str
    openai_chat_model: str

config = PortfolioConfig(
    atlas_admin_user=os.getenv("ATLAS_ADMIN_USER"),
    atlas_admin_pw=os.getenv("ATLAS_ADMIN_PW"),
    atlas_db_name=os.getenv("ATLAS_DB_NAME"),
    atlas_conn_str=os.getenv("ATLAS_CONN_STR"),
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_embedding_model=os.getenv("OPENAI_EMBEDDING_MODEL"),
    openai_chat_model=os.getenv("OPENAI_CHAT_MODEL")
)
