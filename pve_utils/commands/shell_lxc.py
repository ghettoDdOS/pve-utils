import click
from proxmoxer import ProxmoxAPI

from pve_utils.config import settings
from pve_utils.resources import ProxmoxNode


@click.command()
@click.argument("node_name")
@click.argument("host_name")
def create_lxc(node_name: str, host_name: str):
    """
    Creates proxmox LXC CT if is not exist
    1. host_name: Name of CT
    2. node_name: Name of Proxmox Node
    other settings provides with env
    """

    conn = ProxmoxAPI(
        settings.PROXMOX_URL,
        port=settings.PROXMOX_PORT,
        user=settings.PROXMOX_USER,
        password=settings.PROXMOX_PASSWORD,
        verify_ssl=settings.PROXMOX_VERIFY_SSL,
    )

    node_worker = ProxmoxNode(conn, node_name)
    ct = node_worker.get_lxc(host_name, create=True)
    ct.exec(["echo 1234"])


if __name__ == "__main__":
    create_lxc()
