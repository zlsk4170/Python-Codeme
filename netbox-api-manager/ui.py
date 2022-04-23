def show_results(selection,results):

    if selection == '/dcim/cables/':
        space = "{:<5}{:<10}{:<15}{:<15}{:<15}{:<15}{:<15}"
        headers = "ID", "Type", "Dev A Name", "Dev A Port", "Dev B Name", "Dev B Port", "Status"
        print(space.format(*headers))
        for key in results:
            print(space.format(
                key["id"],
                key["type"],
                key["termination_a"]["device"]["name"],
                key["termination_a"]["name"],
                key["termination_b"]["device"]["name"],
                key["termination_b"]["name"],
                key["status"]["value"]
            ))

    elif selection == '/dcim/devices/':
        space = "{:<5}{:<15}{:<20}{:<20}{:<15}"
        headers = "ID", "Dev Name", "Manufacturer", "Dev Role", "Site"
        print(space.format(*headers))
        for key in results:
            print(space.format(
                key["id"],
                key["name"],
                key["device_type"]["manufacturer"]["name"],
                key["device_role"]["display"],
                key["site"]["name"]
            ))

    elif selection == '/dcim/interfaces/':
        space = "{:<10}{:<15}{:<15}{:<20}{:<15}{:<15}{:<15}"
        headers = "ID", "Dev Name", "Int Name", "Int Type", "Peer Dev", "Peer Port", "Cable"
        print(space.format(*headers))
        for key in results:
            try:
                print(space.format(
                    key["id"],
                    key["device"]["name"],
                    key["name"],
                    key["type"]["value"],
                    key["connected_endpoint"]["device"]["display"],
                    key["connected_endpoint"]["name"],
                    key["connected_endpoint"]["cable"]
                ))
            except Exception:
                print(space.format(
                    key["id"],
                    key["device"]["name"],
                    key["name"],
                    key["type"]["value"],
                    "null",
                    "null",
                    "null"
                ))

    elif selection == '/dcim/locations/':
        space = "{:<10}{:<15}{:<30}{:<15}"
        headers = "ID", "Site Name", "Location", "Device Count"
        print(space.format(*headers))
        for key in results:
            print(space.format(
                key["id"],
                key["site"]["name"],
                key["name"],
                key["device_count"]
            ))


    elif selection == '/dcim/manufacturers/':
        space = "{:<10}{:<25}{:<35}{:<15}"
        headers = "ID", "Manufacturer Name", "Description", "Device Count"
        print(space.format(*headers))
        for key in results:
            print(space.format(
                key["id"],
                key["name"],
                key["description"],
                key["devicetype_count"]
            ))


    elif selection == '/dcim/regions/':
        space = "{:<10}{:<15}"
        headers = "ID", "Region Name"
        print(space.format(*headers))
        for key in results:
            print(space.format(
                key["id"],
                key["name"]
            ))


    elif selection == '/dcim/sites/':
        space = "{:<5}{:<15}{:<15}{:<15}{:<20}{:<35}{:<15}"
        headers = "ID", "Site Name", "Region", "Group", "Device Count", "Description", "Status"
        print(space.format(*headers))
        for key in results:
            print(space.format(
                key["id"],
                key["name"],
                key["region"]["name"],
                key["group"]["name"],
                key["device_count"],
                key["description"],
                key["status"]["label"]
            ))