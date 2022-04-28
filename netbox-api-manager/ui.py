def chech_if_null(value):
    try:
        value
    except Exception:
        value = "null"
    return value


def show_results(selection,results):

    if selection == '/dcim/cables/':
        space = "{:<5}{:<10}{:<15}{:<15}{:<15}{:<15}{:<15}"
        headers = "ID", "Type", "Dev A Name", "Dev A Port", "Dev B Name", "Dev B Port", "Status"
        print(space.format(*headers))
        for key in results:
            try:
                id = key["id"]
            except Exception:
                id = "null"
            try:
                type = key["type"]
            except Exception:
                type = "null"
            try:
                dev_a_name = key["termination_a"]["device"]["name"]
            except Exception:
                dev_a_name = "null"
            try:
                dev_a_port = key["termination_a"]["name"]
            except Exception:
                dev_a_port = "null"
            try:
                dev_b_name = key["termination_b"]["device"]["name"]
            except Exception:
                dev_b_name = "null"
            try:
                dev_b_port = key["termination_b"]["name"]
            except Exception:
                dev_b_port = "null"
            try:
                status = key["status"]["value"]
            except Exception:
                status = "null"

            print(space.format(
                id,
                type,
                dev_a_name,
                dev_a_port,
                dev_b_name,
                dev_b_port,
                status
            ))


    elif selection == '/dcim/devices/':
        space = "{:<5}{:<15}{:<20}{:<20}{:<15}"
        headers = "ID", "Dev Name", "Manufacturer", "Dev Role", "Site"
        print(space.format(*headers))
        for key in results:
            try:
                id = key["id"]
            except Exception:
                id = "null"
            try:
                dev_name = key["name"]
            except Exception:
                dev_name = "null"
            try:
                manufacturer = key["device_type"]["manufacturer"]["name"]
            except Exception:
                manufacturer = "null"
            try:
                dev_role = key["device_role"]["display"]
            except Exception:
                dev_role = "null"
            try:
                site = key["site"]["name"]
            except Exception:
                site = "null"

            print(space.format(
                id,
                dev_name,
                manufacturer,
                dev_role,
                site
            ))


    elif selection == '/dcim/interfaces/':
        space = "{:<10}{:<15}{:<15}{:<20}{:<15}{:<15}{:<15}"
        headers = "ID", "Dev Name", "Int Name", "Int Type", "Peer Dev", "Peer Port", "Cable"
        print(space.format(*headers))
        for key in results:
            try:
                id = key["id"]
            except Exception:
                id = "null"
            try:
                dev_name = key["device"]["name"]
            except Exception:
                dev_name = "null"
            try:
                int_name = key["name"]
            except Exception:
                int_name = "null"
            try:
                int_type = key["type"]["value"]
            except Exception:
                int_type = "null"
            try:
                peer_dev = key["connected_endpoint"]["device"]["display"]
            except Exception:
                peer_dev = "null"
            try:
                peer_port = key["connected_endpoint"]["name"]
            except Exception:
                peer_port = "null"
            try:
                cable = key["connected_endpoint"]["cable"]
            except Exception:
                cable = "null"

            print(space.format(
                id,
                dev_name,
                int_name,
                int_type,
                peer_dev,
                peer_port,
                cable
            ))

    elif selection == '/dcim/locations/':
        space = "{:<10}{:<15}{:<30}{:<15}"
        headers = "ID", "Site Name", "Location", "Device Count"
        print(space.format(*headers))
        for key in results:
            try:
                id = key["id"]
            except Exception:
                id = "null"
            try:
                site_name = key["site"]["name"]
            except Exception:
                site_name = "null"
            try:
                location = key["name"]
            except Exception:
                location = "null"
            try:
                counter = key["device_count"]
            except Exception:
                counter = "null"

            print(space.format(
                id,
                site_name,
                location,
                counter
            ))


    elif selection == '/dcim/manufacturers/':
        space = "{:<10}{:<25}{:<35}{:<15}"
        headers = "ID", "Manufacturer Name", "Description", "Device Count"
        print(space.format(*headers))
        for key in results:
            try:
                id = key["id"]
            except Exception:
                id = "null"
            try:
                name = key["name"]
            except Exception:
                name = "null"
            try:
                description = key["description"]
            except Exception:
                description = "null"
            try:
                counter = key["devicetype_count"]
            except Exception:
                counter = "null"

            print(space.format(
                id,
                name,
                description,
                counter
            ))


    elif selection == '/dcim/regions/':
        space = "{:<10}{:<15}"
        headers = "ID", "Region Name"
        print(space.format(*headers))
        for key in results:
            try:
                id = key["id"]
            except Exception:
                id = "null"
            try:
                name = key["name"]
            except Exception:
                name = "null"

            print(space.format(
                id,
                name
            ))


    elif selection == '/dcim/sites/':

        space = "{:<5}{:<15}{:<15}{:<15}{:<20}{:<35}{:<15}"
        headers = "ID", "Site Name", "Region", "Group", "Device Count", "Description", "Status"

        print(space.format(*headers))

        for key in results:
            try:
                id = key["id"]
            except Exception:
                id = "null"
            try:
                site_name = key["name"]
            except Exception:
                site_name = "null"
            try:
                region = key["region"]["name"]
            except Exception:
                region = "null"
            try:
                group_name = key["group"]["name"]
            except Exception:
                group_name = "null"
            try:
                device_count = key["device_count"]
            except Exception:
                device_count = "null"
            try:
                description = key["description"]
            except Exception:
                description = "null"
            try:
                status = key["status"]["label"]
            except Exception:
                status = "null"

            print(space.format(
                id,
                site_name,
                region,
                group_name,
                device_count,
                description,
                status
            ))


