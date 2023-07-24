"""Constants for the Vakio Atmosphere integration."""
from homeassistant.const import Platform

# Platform
PLATFORMS = [Platform.SENSOR]

DOMAIN = "vakio_atmosphere"

# Default consts.
DEFAULT_PORT = 1883
DEFAULT_TOPIC = "vakio"

# CONF consts.
CONF_HOST = "host"
CONF_PORT = "port"
CONF_USERNAME = "username"
CONF_PASSWORD = "password"
CONF_TOPIC = "topic"


# Errors.
ERROR_AUTH: str = "ошибка аутентификации"
ERROR_CONFIG_NO_TREADY: str = "конфигурация интеграции не готова"

CONNECTION_TIMEOUT = 5

# Atmosphere.
