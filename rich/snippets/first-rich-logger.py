# First time using rich for logging — minimal setup, see if it works
from rich.console import Console
from rich.logging import RichHandler
import logging

# TODO: not sure if this is the correct way to wire it up
console = Console()
logging.basicConfig(
    level=logging.INFO,
    handlers=[RichHandler(console=console, rich_tracebacks=True)]
)

log = logging.getLogger("rich_logger")
log.info("Rich logging works — this is an info message")
log.warning("This is a warning — still works")
log.error("And this is an error — tracebacks should look nice")
