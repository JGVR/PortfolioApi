from dataclasses import dataclass
import os

@dataclass(frozen=True)
class PortfolioConfig():
    atlas_admin_user: str
    atlas_admin_pw: str
    atlas_cluster_name: str
    atlas_conn_str: str

config = PortfolioConfig(
    atlas_admin_user=os.getenv("ATLAS_ADMIN_USER"),
    atlas_admin_pw=os.getenv("ATLAS_ADMIN_PW"),
    atlas_cluster_name=os.getenv("ATLAS_CLUSTER_NAME"),
    atlas_conn_str=os.getenv("ATLAS_CONN_STR"),
)
