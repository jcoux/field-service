# Copyright (C) 2022 - OCA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import SUPERUSER_ID, api


def _pre_init_hook(cr):
    """Assign default inventory location to an existing fsm.location"""

    env = api.Environment(cr, SUPERUSER_ID, {})
    default_location_id = env.ref("stock.stock_location_customers").id

    cr.execute(
        """
        ALTER TABLE
            fsm_location
        ADD COLUMN IF NOT EXISTS
            inventory_location_id INTEGER;
        """
    )

    cr.execute(
        """UPDATE fsm_location SET inventory_location_id=%s;""", (default_location_id,)
    )
