/** @odoo-module **/

import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { Component, onWillStart } from "@odoo/owl";

export class AssetAssignmentDashboard extends Component {
    setup() {
        this.orm = useService("orm");
        this.state = {
            total: 0,
            assigned: 0,
            returned: 0,
            overdue: 0,
        };
        onWillStart(async () => {
            const result = await this.orm.call("asset.assignment", "get_dashboard_data", []);
            this.state.total = result.total;
            this.state.assigned = result.assigned;
            this.state.returned = result.returned;
            this.state.overdue = result.overdue;
        });
    }
}

AssetAssignmentDashboard.template = "asset_assignment.Dashboard";

registry.category("actions").add("asset_assignment_dashboard", AssetAssignmentDashboard);
