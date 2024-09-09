"""Custom types for esb_integration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.loader import Integration

    from .api import IntegrationESBApiClient
    from .coordinator import ESBDataUpdateCoordinator


type IntegrationESBConfigEntry = ConfigEntry[IntegrationESBData]


@dataclass
class IntegrationESBData:
    """Data for the Blueprint integration."""

    client: IntegrationESBApiClient
    coordinator: ESBDataUpdateCoordinator
    integration: Integration
